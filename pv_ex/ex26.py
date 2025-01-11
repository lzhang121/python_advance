# -*- coding: utf-8 -*-
# @Time : 2025/01/08 17:30
# @Author : zhanglei
# @Email : zhspark@gmail.com
## 功能： 翻译pdf中英文，生成新的pdf

import re
from PyPDF2 import PdfReader
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter

def translate_pdf_to_new_pdf(input_pdf_path, output_pdf_path, font_path="SimSun.ttf"):
    try:
        # 注册中文字体
        pdfmetrics.registerFont(TTFont('SimSun', font_path))

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
                translated_text = translator.translate(text, src='en', dest='zh-cn').text

                # 使用注册的中文字体
                c.setFont('SimSun', 12)

                # 分段处理翻译内容，避免超出页面宽度
                lines = translated_text.split("\n")
                y = height - margin
                for line in lines:
                    wrapped_lines = [line[i:i+40] for i in range(0, len(line), 40)]
                    for wrapped_line in wrapped_lines:
                        if y < margin:
                            c.showPage()  # 创建新页面
                            c.setFont('SimSun', 12)
                            y = height - margin
                        c.drawString(margin, y, wrapped_line)
                        y -= 20

                # 创建新页面
                c.showPage()
        c.save()
        print(f"Translation completed! New PDF saved to {output_pdf_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

# 示例用法

if __name__ == "__main__":
    input_pdf_path = "/Users/zhanglei/Downloads/Value-of-Professional-Funds-Management.pdf"  # 输入 PDF 文件路径
    output_pdf_path = "translated_output.pdf"  # 输出翻译后的 PDF 文件路径
    font_path = "SimSun.ttf"  # 替换为你系统中的中文字体路径
    translate_pdf_to_new_pdf(input_pdf_path, output_pdf_path, font_path)