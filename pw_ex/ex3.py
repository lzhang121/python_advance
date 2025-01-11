# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:54
# @Author : zhanglei
# @Email : zhspark@gmail.com
from PIL import Image


def add_watermark(main_image_path, logo_image_path, output_path, position="bottom-right"):
    """
    给图片添加水印（LOGO）。
    
    Args:
        main_image_path (str): 主图片路径。
        logo_image_path (str): 水印 LOGO 图片路径。
        output_path (str): 输出图片路径。
        position (str): 水印位置，支持 "bottom-right", "top-left", "top-right", "bottom-left", "center"。
    """
    # 打开主图和 LOGO 图
    main_image = Image.open(main_image_path).convert("RGBA")
    logo = Image.open(logo_image_path).convert("RGBA")
    
    # 调整 LOGO 大小（可选，根据主图大小调整比例）
    logo_width = int(main_image.width * 0.2)  # LOGO 宽度为主图的 20%
    logo_height = int((logo_width / logo.width) * logo.height)
    logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)  # 替换 ANTI_ALIAS
    
    # 创建一个透明层
    transparent = Image.new("RGBA", main_image.size, (0, 0, 0, 0))
    transparent.paste(main_image, (0, 0))
    
    # 计算 LOGO 位置
    if position == "bottom-right":
        x = main_image.width - logo.width - 10
        y = main_image.height - logo.height - 10
    elif position == "top-left":
        x, y = 10, 10
    elif position == "top-right":
        x = main_image.width - logo.width - 10
        y = 10
    elif position == "bottom-left":
        x, y = 10, main_image.height - logo.height - 10
    elif position == "center":
        x = (main_image.width - logo.width) // 2
        y = (main_image.height - logo.height) // 2
    else:
        raise ValueError("Invalid position value. Choose from: bottom-right, top-left, top-right, bottom-left, center.")
    
    # 将 LOGO 粘贴到透明层上
    transparent.paste(logo, (x, y), logo)
    
    # 合并图层并保存
    result = Image.alpha_composite(transparent, transparent)
    result = result.convert("RGB")  # 如果需要保存为非透明格式（如 JPEG）
    result.save(output_path)
    print(f"水印添加完成，保存至：{output_path}")


def main(flag):
    # 调用函数
    main_image_path = "images/example_ex3.png"  # 主图路径
    logo_image_path = "transparent_logo.png"        # 水印 LOGO 图路径
    output_path = "images/output_image.jpg"    # 输出图片路径
    add_watermark(main_image_path, logo_image_path, output_path, position="bottom-right")


if __name__ == '__main__':
    main(True)