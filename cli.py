import sys #for CLI lines
from pathlib import Path
from pdf_core import validate_inputs, merge_pdfs, generate_timestamped_filename

def main():
    raw_arguments = sys.argv[1:]
    files = [Path(arg) for arg in raw_arguments]

    errors = validate_inputs(files)
    if errors:
        for error in errors:
            print(error)
        sys.exit()

    output_path = generate_timestamped_filename()

    try:
        merge_pdfs(files, output_path)
        print(f"Your pdfs were successfully merged. The output: {output_path.name}")
    except Exception as e:
        print("There was an error during merging:", e)
        sys.exit()

if __name__ == "__main__":
    main()
