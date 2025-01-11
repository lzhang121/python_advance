# -*- coding: utf-8 -*-
# @Time : 2025/01/01 12:51
# @Author : zhanglei
# @Email : zhspark@gmail.com
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example_tmp_ex1.png")
browser.close()

playwright.stop()