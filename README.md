# Offline PDF Tool

A lightweight, fully offline PDF utility built in Python using PyQt6.

Supports both CLI and GUI interfaces with proper architecture, validation, and structured error handling.

---

## Features (v0.2)

- Merge multiple PDFs in the order selected
- Timestamp-based output naming
- Structured input validation with clear error messages
- Clean Command-Line Interface (CLI)
- Desktop GUI built with PyQt6
- Filename-only display in GUI (stores full path internally)
- Fully offline operation (no uploads, no external services)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/barnil/offline-pdf-tool
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

### CLI Mode

To merge PDFs using the command line:

```bash
python cli.py file1.pdf file2.pdf
```

If the files are not in the same directory, provide the full path:

```bash
python cli.py /path/to/file1.pdf /path/to/file2.pdf
```

### Example CLI Output

```bash
Your pdfs were successfully merged. The output: merged_YYYYMMDD_HHMMSS.pdf
```

The merged file will be saved in the current working directory.

---

### GUI Mode

To launch the graphical interface:

```bash
python gui.py
```

Steps:

1. Click **Select PDFs**
2. Choose two or more PDF files
3. Click **Merge PDFs**
4. The merged file will be generated in the current directory

The status label will display validation errors or success messages.

---

## Project Structure

```bash
offline-pdf-tool/
├── pdf_core.py        # Backend logic (validation + merging)
├── cli.py             # Command-line interface
├── gui.py             # PyQt6 graphical interface
├── requirements.txt
└── README.md
```

---

## Architecture

The project follows a clean separation of concerns:

- `pdf_core.py` contains pure backend logic
- `cli.py` handles terminal interaction
- `gui.py` handles graphical interaction

Both CLI and GUI use the same backend engine.

---

## Roadmap

Planned improvements:

- PDF splitting
- Remove / reorder selected files in GUI
- Image to PDF conversion
- Drag-and-drop file support
- Save-as dialog for output location
- Packaged macOS `.app` build
- Windows support