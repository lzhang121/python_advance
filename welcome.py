# -*- coding: utf-8 -*-
# @Time : 2024/12/26 22:47
# @Author : zhanglei
# @Email : zhspark@gmail.com

def welcome(fn):
	def wrapper(*args, **kwargs):
		print("func elcome")
		result = fn(*args, **kwargs)
		return result

	return wrapper

@welcome
def my_fun(message: str):
	print("func my_func")
	print(f"Hello {message} ")


if __name__ == "__main__":
	my_fun("Jack")