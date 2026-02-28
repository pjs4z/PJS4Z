import argparse
import logging
import sys
from pathlib import Path

# Attempt to import the parser from the previous script
try:
    from pdf_parser import SOTADocumentParser, chunk_for_rag
except ImportError:
    print("ERROR: Could not import 'pdf_parser.py'. "
          "Please ensure the previous code is saved as 'pdf_parser.py' in the same directory.")
    sys.exit(1)

# Configure logging for the CLI
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def process_pdf(pdf_path: Path, output_dir: Path, top_margin: float, bottom_margin: float, do_chunk: bool):
    """Processes a single PDF file and writes the Markdown (and optionally tests chunking)."""
    logging.info(f"Processing: {pdf_path.name}")
    
    try:
        # 1. Initialize the SOTA Parser
        parser = SOTADocumentParser(
            pdf_path=str(pdf_path),
            top_margin_pct=top_margin,
            bottom_margin_pct=bottom_margin
        )
        
        # 2. Generate pristine Markdown
        clean_markdown = parser.to_markdown()
        
        if not clean_markdown.strip():
            logging.warning(f"No text extracted from {pdf_path.name}. (Might be a scanned image-only PDF).")
            return
            
        # 3. Save Markdown File
        md_filename = output_dir / f"{pdf_path.stem}.md"
        md_filename.write_text(clean_markdown, encoding='utf-8')
        logging.info(f"Success: Saved Markdown to -> {md_filename}")
        
        # 4. Handle RAG Chunking Demonstration
        if do_chunk:
            logging.info(f"Running hierarchy-aware chunking on {pdf_path.name}...")
            chunks = chunk_for_rag(clean_markdown)
            
            if chunks:
                logging.info(f"Generated {len(chunks)} semantic chunks.")
                # Safely grab a sample chunk to display (try to grab one from the middle)
                sample_idx = min(2, len(chunks)-1) if len(chunks) > 0 else 0
                sample = chunks[sample_idx]
                
                print("\n" + "="*60)
                print(f"--- RAG CHUNK SAMPLE FOR: {pdf_path.name} ---")
                print(f"Metadata Context : {sample.metadata}")
                print(f"Content Snippet  : {sample.page_content[:200]}...\n")
                print("="*60 + "\n")
            
    except Exception as e:
        logging.error(f"Failed to process {pdf_path.name}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="SOTA PDF-to-Markdown CLI. Converts single PDF files or entire directories into "
                    "hierarchically perfect Markdown using TOC-injection and CropBox junk removal."
    )
    
    # Mutually exclusive group: You must provide EITHER a single file OR a directory
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "-f", "--file", 
        type=str, 
        help="Path to a single PDF file to process."
    )
    input_group.add_argument(
        "-d", "--dir", 
        type=str, 
        help="Path to a directory containing PDF files to batch process."
    )
    
    # Optional Output Directory
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="./source/markdown", 
        help="Directory to save the resulting .md files. Defaults to './output'."
    )
    
    # Tuning margins for CropBox (Junk removal)
    parser.add_argument(
        "--top-margin", 
        type=float, 
        default=0.08, 
        help="Percentage of the top page to crop out (removes running headers). Default: 0.08 (8%%)"
    )
    parser.add_argument(
        "--bottom-margin", 
        type=float, 
        default=0.08, 
        help="Percentage of the bottom page to crop out (removes page numbers). Default: 0.08 (8%%)"
    )
    
    # Chunking Flag
    parser.add_argument(
        "-c", "--chunk", 
        action="store_true", 
        help="If flagged, also runs the hierarchy-aware chunker demonstration and prints a sample."
    )

    args = parser.parse_args()

    # Create output directory if it doesn't exist
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # -----------------------------------------
    # Execution Logic: Single File vs Directory
    # -----------------------------------------
    if args.file:
        target_path = Path(args.file)
        if not target_path.exists() or not target_path.is_file():
            logging.error(f"The input file '{target_path}' does not exist.")
            sys.exit(1)
        if target_path.suffix.lower() != '.pdf':
            logging.error(f"The file '{target_path.name}' is not a PDF.")
            sys.exit(1)
            
        logging.info("Starting single-file execution...")
        process_pdf(target_path, output_dir, args.top_margin, args.bottom_margin, args.chunk)

    elif args.dir:
        target_path = Path(args.dir)
        if not target_path.exists() or not target_path.is_dir():
            logging.error(f"The directory '{target_path}' does not exist.")
            sys.exit(1)
            
        # Find all PDFs (case-insensitive extension match)
        pdf_files = list(target_path.glob("*.pdf")) + list(target_path.glob("*.PDF"))
        if not pdf_files:
            logging.warning(f"No PDF files found in directory '{target_path}'.")
            sys.exit(0)
            
        logging.info(f"Starting batch execution. Found {len(pdf_files)} PDFs in '{target_path}'...")
        for pdf_file in pdf_files:
            process_pdf(pdf_file, output_dir, args.top_margin, args.bottom_margin, args.chunk)
            
    logging.info("All tasks completed.")

if __name__ == "__main__":
    main()