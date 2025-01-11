# -*- coding: utf-8 -*-
# @Time : 2025/01/08 14:58
# @Author : zhanglei
# @Email : zhspark@gmail.com
import re
from PyPDF2 import PdfReader
from googletrans import Translator

def translate_pdf_to_chinese(pdf_path, output_path):
    # Step 1: Read the PDF file
    try:
        reader = PdfReader(pdf_path)
        translator = Translator()
        translated_content = ""

        # Step 2: Extract text from each page and translate
        for page in reader.pages:
            text = page.extract_text()
            if text is not None and text.strip():
                # Translate English to Chinese
                text = re.sub(r"\t", " ", text)
                trans = translator.translate(str(text), src='en', dest='zh-cn')
                translated_text = trans.text
                translated_content += translated_text + "\n\n"

        # Step 3: Save the translated content to a new file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)
        print(f"Translation completed! Translated content saved to {output_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
pdf_path = "/Users/zhanglei/Downloads/Value-of-Professional-Funds-Management.pdf"  # Replace with your input PDF file path
output_path = "translated_output.txt"  # File to save the translated content
translate_pdf_to_chinese(pdf_path, output_path)