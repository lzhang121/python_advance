# -*- coding: utf-8 -*-
# @Time : 2025/01/01 12:49
# @Author : zhanglei
# @Email : zhspark@gmail.com
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://playwright.dev/python/docs/api/class-playwright")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())