import os
import subprocess
import sys

def main():
    source_dir = "source/inputs"
    
    if not os.path.isdir(source_dir):
        print(f"Error: Directory '{source_dir}' does not exist.")
        sys.exit(1)

    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        
        if os.path.isfile(filepath):
            print(f"\n================================================================================")
            print(f"Processing: {filepath}")
            print(f"================================================================================\n")
            
            subprocess.run([sys.executable, "docs/ontology-engineering/bfo-1.py", filepath])
            subprocess.run([sys.executable, "docs/ontology-engineering/bfo-2.py", filepath])

if __name__ == "__main__":
    main()
