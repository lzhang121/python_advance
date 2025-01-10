# -*- coding: utf-8 -*-
# @Time : 2025/01/01 12:52
# @Author : zhanglei
# @Email : zhspark@gmail.com
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    iphone = playwright.devices["iPhone 6"]

    browser = webkit.launch(headless=False)
    context = browser.new_context(**iphone)
    print(context)
    page = context.new_page()
    page.goto("https://playwright.dev/python/docs/api/class-playwright")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)