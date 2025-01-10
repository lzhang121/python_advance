# -*- coding: utf-8 -*-
# @Time : 2025/01/08 17:15
# @Author : zhanglei
# @Email : zhspark@gmail.com
import re
from PyPDF2 import PdfReader
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def translate_pdf_to_new_pdf(input_pdf_path, output_pdf_path):
    try:
        # 初始化 PDF 阅读器和翻译器
        reader = PdfReader(input_pdf_path)
        translator = Translator()

        # 创建新的 PDF 文件
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        width, height = letter
        margin = 40

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            text = re.sub(r"\t", " ", text)
            if text.strip():
                # 翻译文本
                translated_text = translator.translate(text, src='en', dest='ja').text
                print("==",translated_text)
                # 分段处理翻译内容，避免超出页面宽度
                lines = translated_text.split("\n")
                y = height - margin
                for line in lines:
                    wrapped_lines = [line[i:i+90] for i in range(0, len(line), 90)]
                    for wrapped_line in wrapped_lines:
                        if y < margin:
                            c.showPage()  # 创建新页面
                            y = height - margin
                        c.drawString(margin, y, wrapped_line)
                        y -= 14

                # 创建新页面
                c.showPage()
        c.save()
        print(f"Translation completed! New PDF saved to {output_pdf_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

# 示例用法
input_pdf_path = "/Users/zhanglei/Downloads/Value-of-Professional-Funds-Management.pdf"  # 输入 PDF 文件路径
output_pdf_path = "translated_output.pdf"  # 输出翻译后的 PDF 文件路径
translate_pdf_to_new_pdf(input_pdf_path, output_pdf_path)