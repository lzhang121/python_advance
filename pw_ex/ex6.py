# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:54
# @Author : ray
from PIL import Image


def make_logo_transparent(logo_path, output_path, transparency=128):
    """
    将 LOGO 图片调整为透明效果。
    
    Args:
        logo_path (str): 输入 LOGO 图片路径。
        output_path (str): 输出图片路径。
        transparency (int): 透明度值，范围 0-255，越小越透明。
    """
    # 打开 LOGO 图像
    logo = Image.open(logo_path).convert("RGBA")
    
    # 获取 LOGO 的像素数据
    pixels = logo.load()
    
    # 遍历 LOGO 的每个像素，调整透明度
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, b, a = pixels[x, y]  # 获取当前像素的 RGBA 值
            # 仅调整非完全透明像素的透明度
            if a > 0:
                pixels[x, y] = (r, g, b, transparency)
    
    # 保存结果
    logo.save(output_path, format="PNG")
    print(f"透明 LOGO 保存到: {output_path}")



def main():
    # 调用函数
    logo_path = "logo.png"         # 原始 LOGO 图片路径
    output_path = "transparent_logo.png"  # 输出路径
    make_logo_transparent(logo_path, output_path, transparency=128)  # 128 表示 50% 透明



if __name__ == '__main__':
    main()