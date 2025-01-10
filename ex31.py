# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:33
# @Author : zhanglei
# @Email : zhspark@gmail.com
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self  # 迭代器的 `__iter__` 方法返回自身

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration  # 没有更多元素时，抛出异常

if __name__ == "__main__":
	# 使用
	iterator = MyIterator(5)
	for value in iterator:
	    print(value)


