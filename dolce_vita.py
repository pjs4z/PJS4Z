import os
import subprocess
import sys

def main():
    source_dir = "source/dolce_vita"
    
    if not os.path.isdir(source_dir):
        print(f"Error: Directory '{source_dir}' does not exist.")
        sys.exit(1)

    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        
        if os.path.isfile(filepath):
            print(f"\n================================================================================")
            print(f"Processing: {filepath}")
            print(f"================================================================================\n")
            
            # Run dolce_code.py
            # print(f"--- Running dolce_code.py ---")
            # subprocess.run([sys.executable, "dolce_code.py", filepath])
            
            # Run obsidian_pipeline.py
            print(f"\n--- Running obsidian_pipeline.py ---")
            subprocess.run([sys.executable, "obsidian_pipeline.py", filepath])

if __name__ == "__main__":
    main()
