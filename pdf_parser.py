import fitz  # PyMuPDF
import re
import difflib
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SOTADocumentParser:
    """
    Implements Strategy A (The "TOC-First" Injection) and Junk Removal.
    Updated to filter specific watermarks and shift the header hierarchy.
    """
    
    def __init__(self, pdf_path: str, top_margin_pct: float = 0.08, bottom_margin_pct: float = 0.08):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        # Margins to crop out "junk" like running headers and page numbers
        self.top_margin_pct = top_margin_pct 
        self.bottom_margin_pct = bottom_margin_pct
        
        # Extract the Ground Truth Taxonomy
        self.toc_skeleton = self._build_toc_skeleton()
        
    def _build_toc_skeleton(self) -> Dict[int, List[Dict[str, Any]]]:
        """
        Extracts the internal Table of Contents (Bookmarks).
        Maps 0-indexed page numbers to the expected headers on that page.
        """
        toc = self.doc.get_toc() # Returns: [level, title, physical_page_number]
        skeleton: Dict[int, List[Dict[str, Any]]] = {}
        
        if not toc:
            logging.warning("No TOC/Bookmarks found! Strategy A requires PDF metadata. "
                            "Extraction will fall back to flat text without hierarchy.")
            return skeleton
            
        for level, title, page_num in toc:
            page_idx = page_num - 1  # Convert to 0-indexed for PyMuPDF page handling
            
            if page_idx not in skeleton:
                skeleton[page_idx] = []
                
            skeleton[page_idx].append({
                'level': level,
                'title': title.strip(),
                'matched': False
            })
            
        logging.info(f"Extracted TOC Skeleton: Found headers spanning {len(skeleton)} distinct pages.")
        return skeleton

    def _clean_text(self, text: str) -> str:
        """
        Removes mid-sentence line breaks common in PDF extraction, 
        and strips out unwanted watermarks.
        """
        # 1. Strip out all references to "OceanofPDF.com" (case-insensitive)
        text = re.sub(r'(?i)oceanofpdf\.com', '', text)
        
        # 2. Remove standard line breaks
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text.strip()

    def _is_header_match(self, block_text: str, toc_title: str) -> bool:
        """
        Determines if a PDF text block matches a TOC entry using exact and fuzzy matching.
        """
        norm_block = self._clean_text(block_text).lower()
        norm_title = self._clean_text(toc_title).lower()

        # If block is totally empty (e.g., was just a watermark that got scrubbed)
        if not norm_block:
            return False

        # 1. Substring Match
        if norm_title in norm_block:
            if len(norm_block) <= len(norm_title) + 30:
                return True

        # 2. Fuzzy Matching to account for slight OCR discrepancies
        if abs(len(norm_block) - len(norm_title)) < 25:
            similarity = difflib.SequenceMatcher(None, norm_title, norm_block).ratio()
            if similarity > 0.85:
                return True

        return False

    def to_markdown(self) -> str:
        """
        Processes the document page by page, applying CropBox to remove junk, 
        and injecting strict header taxonomy based on the TOC skeleton.
        """
        markdown_pages = []
        pending_toc = [] # Tracks headers that visually spill over to the next page

        for page_idx in range(len(self.doc)):
            page = self.doc[page_idx]
            rect = page.rect
            
            # --- JUNK REMOVAL: CropBox Logic ---
            clip_rect = fitz.Rect(
                rect.x0,
                rect.y0 + (rect.height * self.top_margin_pct),
                rect.x1,
                rect.y1 - (rect.height * self.bottom_margin_pct)
            )

            blocks = page.get_text("blocks", clip=clip_rect)
            
            # Filter for pure text blocks (type 0) and sort logically (top-to-bottom)
            text_blocks = [b for b in blocks if b[6] == 0]
            text_blocks.sort(key=lambda b: (b[1], b[0]))

            # Fetch expected headers for this page + any missed from previous pages
            expected_headers = pending_toc + self.toc_skeleton.get(page_idx, [])
            pending_toc = [] 

            page_md_blocks = []

            for block in text_blocks:
                block_text = self._clean_text(block[4])
                
                # If the block was ONLY a watermark, it's now empty. Skip it entirely.
                if not block_text:
                    continue
                
                is_header = False

                # --- DETERMINISTIC TAXONOMY INJECTION ---
                for header in expected_headers:
                    if not header['matched'] and self._is_header_match(block_text, header['title']):
                        
                        # SHIFT HIERARCHY: Level 1 becomes H2 (##), Level 2 becomes H3 (###)
                        shifted_level = header['level'] + 1
                        md_prefix = '#' * shifted_level
                        
                        page_md_blocks.append(f"{md_prefix} {header['title']}")
                        
                        header['matched'] = True
                        is_header = True
                        break
                
                if not is_header:
                    page_md_blocks.append(block_text)
            
            pending_toc = [h for h in expected_headers if not h['matched']]
            
            # DETERMINISTIC FAILSAFE (Forces missed headers at the top of the page)
            for header in self.toc_skeleton.get(page_idx, []):
                if not header['matched'] and header in pending_toc:
                    # Apply the exact same shifted hierarchy here
                    shifted_level = header['level'] + 1
                    md_prefix = '#' * shifted_level
                    
                    page_md_blocks.insert(0, f"{md_prefix} {header['title']}")
                    header['matched'] = True
                    pending_toc.remove(header)

            if page_md_blocks:
                markdown_pages.append("\n\n".join(page_md_blocks))

        return "\n\n".join(markdown_pages)

# ==========================================
# RAG PIPELINE INTEGRATION
# ==========================================
def chunk_for_rag(markdown_text: str):
    """
    Demonstrates Langchain splitting using the new H2/H3 shifted hierarchy.
    """
    from langchain_text_splitters import MarkdownHeaderTextSplitter

    # Updated to reflect the newly shifted taxonomy
    headers_to_split_on = [
        ("##", "H2_Section"),
        ("###", "H3_Subsection"),
        ("####", "H4_Sub_Subsection"),
    ]

    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False 
    )
    
    chunks = splitter.split_text(markdown_text)
    logging.info(f"Chunking Complete: Generated {len(chunks)} hierarchy-aware chunks.")
    return chunks

# --- Execution Example ---
if __name__ == "__main__":
    PDF_FILE = "your_book.pdf" # <-- Replace with your target PDF
    OUTPUT_MD = "parsed_clean_book.md"
    
    try:
        parser = SOTADocumentParser(pdf_path=PDF_FILE, top_margin_pct=0.08, bottom_margin_pct=0.08)
        clean_markdown = parser.to_markdown()
        
        with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
            f.write(clean_markdown)
        logging.info(f"Success: Saved pristine Markdown to {OUTPUT_MD}")
        
        rag_chunks = chunk_for_rag(clean_markdown)
        
        if rag_chunks:
            print("\n--- Example SOTA Chunk ---")
            print(f"Metadata Context: {rag_chunks[2].metadata if len(rag_chunks) > 2 else rag_chunks[0].metadata}")
            print(f"Content Sample  : {rag_chunks[2].page_content[:150]}...\n")
            
    except Exception as e:
        logging.error(f"Execution failed: {e}")