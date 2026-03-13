import os
import PyPDF2
from docx import Document

MAX_FILE_SIZE = 600 * 1024  # 600 KB


def parse_resume(file_path):

    if not os.path.exists(file_path):
        return "Error: Resume file not found."

    file_size = os.path.getsize(file_path)

    if file_size > MAX_FILE_SIZE:
        return "Error: File size exceeds 600 KB limit."

    file_extension = file_path.split(".")[-1].lower()

    text = ""

    try:

        if file_extension == "pdf":
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text()

        elif file_extension == "docx":
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text

        else:
            return "Error: Only PDF or DOCX files are allowed."

        return text

    except Exception as e:
        return f"Error while reading resume: {str(e)}"