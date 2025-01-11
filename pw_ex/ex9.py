# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:54
# @Author : ray
from PIL import Image, ImageEnhance


def add_transparent_logo_watermark(main_image_path, logo_image_path, output_path, position="bottom-right", transparency=128):
    """
    给图片添加透明 LOGO 水印。

    Args:
        main_image_path (str): 主图片路径。
        logo_image_path (str): LOGO 图片路径（PNG 格式，支持透明）。
        output_path (str): 输出图片路径。
        position (str): 水印位置，支持 "bottom-right", "top-left", "top-right", "bottom-left", "center"。
        transparency (int): LOGO 的透明度，范围 0-255，值越小越透明。
    """
    # 打开主图片和 LOGO 图
    main_image = Image.open(main_image_path).convert("RGBA")
    logo = Image.open(logo_image_path).convert("RGBA")

    # 调整 LOGO 的透明度
    alpha = logo.getchannel("A")  # 获取 LOGO 的透明度通道
    alpha = ImageEnhance.Brightness(alpha).enhance(
        transparency / 255.0)  # 按透明度调整
    logo.putalpha(alpha)

    # 调整 LOGO 大小（LOGO 宽度为主图片的 20%）
    logo_width = int(main_image.width * 0.2)
    logo_height = int((logo_width / logo.width) * logo.height)
    logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

    # 确定 LOGO 的位置
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
        raise ValueError(
            "Invalid position value. Choose from: bottom-right, top-left, top-right, bottom-left, center.")

    # 在主图上添加 LOGO
    transparent_layer = Image.new("RGBA", main_image.size, (0, 0, 0, 0))
    transparent_layer.paste(main_image, (0, 0))
    transparent_layer.paste(logo, (x, y), logo)  # 使用 LOGO 的透明度

    # 保存最终结果
    final_image = Image.alpha_composite(transparent_layer, transparent_layer)
    final_image = final_image.convert("RGB")  # 如果保存为 JPEG 需要转换为 RGB 格式
    final_image.save(output_path)
    print(f"透明水印添加完成，图片保存到：{output_path}")


def main():

    # 调用函数
    main_image_path = "pw_ex/images/example_ex3.png"  # 主图片路径
    logo_image_path = "pw_ex/logo.png"  # LOGO 图片路径（推荐透明 PNG）
    output_path = "pw_ex/images/example_ex3_with_logo.png"  # 输出图片路径

    add_transparent_logo_watermark(
        main_image_path, logo_image_path, output_path, position="bottom-right", transparency=128)


if __name__ == '__main__':
    main()
