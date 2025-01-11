# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:54
# @Author : ray
from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(image_path, output_path, watermark_text, font_path='simhei.ttf'):
    # 打开图片并转换为RGBA模式
    image = Image.open(image_path).convert("RGBA")

    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(image)

    # 字体的格式
    try:
        fontstyle = ImageFont.truetype(font_path, 30)  # 调整字体和大小
    except IOError:
        print(f"字体文件 {font_path} 未找到，请确认路径是否正确")
        return

    # 获取文本的边界框
    left, top, right, bottom = draw.textbbox((0, 0), watermark_text, font=fontstyle)
    textwidth = right - left
    textheight = bottom - top

    # 文字位置，颜色和透明度
    width, height = image.size
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), watermark_text, font=fontstyle, fill=(0, 0, 0, 0))  # 黑色文字，半透明

    # 保存带有水印的图片，注意保存时指定PNG格式以保留透明度
    image.save(output_path, format="PNG")


def batch_add_watermark(folder_path, watermark_text, font_path='simhei.ttf'):
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg')):  # 检查文件扩展名
            file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(folder_path, 'watermarked_' + filename)
            add_watermark(file_path, output_file_path, watermark_text, font_path)
            print(f'Added watermark to {filename}')
            
            
def main():
    folder_path = 'images'
    watermark_text = ''
    batch_add_watermark(folder_path, watermark_text)


if __name__ == '__main__':
    main()