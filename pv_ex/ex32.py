# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:39
# @Author : zhanglei
# @Email : zhspark@gmail.com
# def my_generator(limit):
#     counter = 0
#     while counter < limit:
#         counter += 1
#         yield counter  # 使用 yield 暂停并返回当前值
#
# if __name__ == "__main__":
# 	# 使用
# 	gen = my_generator(5)
# 	print(dir(gen))
# 	for value in gen:
# 	    print(value)

# ## 读大文件
# def read_large_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line.strip()  # 每次返回一行内容
#
# if __name__ == "__main__":
# 	for line in read_large_file("translated_output.txt"):
# 	    print(line)

if __name__ == "__main__":
	gen_exp = (x * x for x in range(5))
	for value in gen_exp:
	    print(value)