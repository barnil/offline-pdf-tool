from datetime import datetime #for timestamp in pdf naming
from pypdf import PdfWriter #for writing the pdfs
from pypdf import PdfReader #for reading the pdfs
from pathlib import Path #for path operations

def validate_inputs(files):

    #an empty list was initialised to include the errors so that it can be reported to the user
    errors = []

    #first error check to see if the user has added at least 2 pdfs
    if len(files) < 2:
        errors.append("Please ensure that you add at least 2 pdfs")

    #this loop will go over the rest of the errors
    for file in files:

        extension = (file.suffix).lower() #to make the comparison more easier as the pdf extension may be upper or lowercase

        if not file.exists():
            errors.append(f"{file} doesn't exist") #checks if the file exists itself    
        elif not file.is_file():
            errors.append(f"{file} is not a file") #checks if it a file or a folder
        elif extension != ".pdf":
            errors.append(f"{file} is not a pdf") #checks if the file is a pdf or not

    return errors

def merge_pdfs(files, output_path):
    writer = PdfWriter()

    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, 'wb') as f:
        writer.write(f)

    writer.close()

def generate_timestamped_filename():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    output_path = Path(f"merged_{timestamp}.pdf")

    return output_path