# -*- coding: utf-8 -*-
# @Time : 2025/01/01 12:54
# @Author : zhanglei
# @Email : zhspark@gmail.com
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    webkit = playwright.webkit
    iphone = playwright.devices["iPhone 6"]
    browser = await webkit.launch(headless=False)
    context = await browser.new_context(**iphone)
    page = await context.new_page()
    await page.goto("https://playwright.dev/python/docs/api/class-playwright")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())