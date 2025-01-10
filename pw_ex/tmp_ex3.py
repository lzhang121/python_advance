# -*- coding: utf-8 -*-
# @Time : 2025/01/01 19:42
# @Author : zhanglei
# @Email : zhspark@gmail.com
import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    #print(playwright.devices['iPhone 12'])
    iphone_12 = playwright.devices['iPhone 12']
    browser = await playwright.webkit.launch(headless=False)
    context = await browser.new_context(
        **iphone_12,
    )

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())





