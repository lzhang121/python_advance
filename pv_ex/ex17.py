# -*- coding: utf-8 -*-
# @Time : 2024/12/23 20:58
# @Author : zhanglei
# @Email : zhanglei@bonree.com

import csv

# 文件路径设置
input_csv_file = "Excel_1.csv"  # 原始CSV文件路径
output_csv_file = "FM_Excel.csv"  # 保存符合条件记录的新CSV文件
search_key = "FM"  # 替换为你要搜索的关键字

# 打开输入CSV文件并读取内容
with open(input_csv_file, mode='r', encoding='utf-8') as infile, open(output_csv_file, mode='w', encoding='utf-8',
                                                                      newline='') as outfile:
	csv_reader = csv.reader(infile)
	csv_writer = csv.writer(outfile)

	# 读取表头并写入到新文件中
	headers = next(csv_reader)
	csv_writer.writerow(headers)

	# 遍历CSV内容
	matching_count = 0
	for row in csv_reader:
		# 检查每个字段是否包含关键字
		if search_key == row[0][:2]:
			csv_writer.writerow(row)  # 写入符合条件的行
			matching_count += 1

# 提示结果
if matching_count > 0:
	print(f"找到 {matching_count} 条符合关键字 '{search_key}' 的记录，已保存到 '{output_csv_file}'。")
else:
	print(f"没有找到包含关键字 '{search_key}' 的记录。")