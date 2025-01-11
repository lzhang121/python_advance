# -*- coding: utf-8 -*-
# @Time : 2024/12/25 19:05
# @Author : zhanglei
# @Email : zhanglei@bonree.com
from googletrans import Translator

# 初始化翻译器
translator = Translator()

# 要翻译的英文文本
text = """
This feature enables you to review groups of budget periods and the budget periods of which they are comprised.
Overview lists display existing budget period groups
List filters allow you to narrow your focus
Detail displays provide insight into each group and the group content (individual budget periods, ranges of individual budget periods, parent budget period groups, child budget period groups)
Drill-down to individual objects (budget period object pages) provides flexible navigation and a 360° view of this group
"""

# 执行翻译：从英语到日语
translated = translator.translate(text, src='en', dest='ja')

# 输出翻译结果
print(f"Original: {text}")
print(f"Translated: {translated.text}")