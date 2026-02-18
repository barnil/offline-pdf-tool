# Offline PDF Tool

A lightweight, fully offline PDF utility built in Python for macOS.

Currently supports merging multiple PDFs via CLI with proper validation and structured error handling.

---

## Features (v0.1)

- Merge multiple PDFs in the order provided
- Timestamp-based output naming
- Input validation with clear error messages
- Clean CLI interface
- Fully offline operation

---

## Installation

1. Clone the repository:

```bash
git clone hhttps://github.com/barnil/offline-pdf-tool
cd offline-pdf-tool
```

2. (Recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

To merge PDFs:

```bash
python main.py file1.pdf file2.pdf
```

If the files are not in the same directory, provide the full path:

```bash
python main.py /path/to/file1.pdf /path/to/file2.pdf
```

### Example Output

```bash
Your pdfs were successfully merged. The output: merged_YYYYMMDD_HHMMSS.pdf
```

The merged file will be saved in the current working directory.

---

## Roadmap

Planned improvements:

- PDF splitting
- Image to PDF conversion
- GUI version
- Packaged macOS application
- Potential Windows support