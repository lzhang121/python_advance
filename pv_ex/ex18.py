# -*- coding: utf-8 -*-
# @Time : 2024/12/23 21:33
# @Author : zhanglei
# @Email : zhanglei@bonree.com
import requests
import re

# 发起请求
url = 'https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps(\'FMAVCH01\')/S29PCE'  # 替换为目标URL
response = requests.get(url)
print(response.status_code)

# 检查响应是否成
if response.status_code == 200:
	# 使用正则表达式匹配目标文本
	print(response.text)
	match = re.search(r'<span id="__xmlview5--allReleases-labelText" class="sapMSelectListItemText">(.*?)</span>',
	                  response.text)

	# 检查是否匹配到
	if match:
		# 提取匹配的文本
		result = match.group(1)
		print("匹配到的文本:", result)
	else:
		print("未找到匹配的文本")
else:
	print("请求失败，状态码:", response.status_code)