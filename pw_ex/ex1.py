# -*- coding: utf-8 -*-
# @Time : 2025/01/01 12:48
# @Author : zhanglei
# @Email : zhspark@gmail.com

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/docs/api/class-playwright")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)