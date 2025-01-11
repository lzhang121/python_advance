# -*- coding: utf-8 -*-
# @Time : 2025/01/09 20:30
# @Author : zhanglei
# @Email : zhspark@gmail.com
from appscript import app, k

# 打开 Excel 应用
excel = app('Microsoft Excel')

# 创建一个新的工作簿
workbook = excel.make(new=k.document, with_properties={})