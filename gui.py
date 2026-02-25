from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QFileDialog, QListWidgetItem
from PyQt6.QtCore import Qt
import sys
from pathlib import Path
from pdf_core import validate_inputs, merge_pdfs, generate_timestamped_filename

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Offline PDF Tool")
    window.resize(400, 380)

    layout = QVBoxLayout()
    window.setLayout(layout)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(15)

    button = QPushButton("Select PDFs")
    layout.addWidget(button)

    file_list = QListWidget()
    layout.addWidget(file_list)

    secondbutton = QPushButton("Merge PDFs")
    layout.addWidget(secondbutton)
    layout.addStretch()

    label = QLabel("No File Selected")
    layout.addWidget(label)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    selected_files = []

    def select_files():
        files, _ = QFileDialog.getOpenFileNames(
            window,
            "Select PDF Files",
            ".",
            "PDF Files (*.pdf)"
        )

        nonlocal selected_files
        selected_files = files

        if files:
            file_list.clear()
            for file in files:
                name = Path(file).name
                item = QListWidgetItem(name)
                item.setData(Qt.ItemDataRole.UserRole, file)
                file_list.addItem(item)

            label.setText(f"{len(files)} file(s) were selected")
        else:
            file_list.clear()
            selected_files = []
            label.setText("No file selected")

    button.clicked.connect(select_files)

    def merge_selected():
        if len(selected_files) < 2:
            label.setText("Please select at least 2 PDFs")
            return
        
        path_of_selected_files = [Path(f) for f in selected_files]

        errors = validate_inputs(path_of_selected_files)
        
        if errors:
            label.setText(errors[0])
            return
        
        name = generate_timestamped_filename()
        
        try:
            merge_pdfs(path_of_selected_files, name)
            label.setText(f"Merged as {name.name}")
        except Exception:
            label.setText("Error during merging")

    secondbutton.clicked.connect(merge_selected)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()