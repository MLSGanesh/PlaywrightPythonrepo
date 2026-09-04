# prerequisite for Asynchrounous execution
# install pytest-asyncio
# command pip install pytest-asyncio

# async is used when programming language is in asynchronous nature, execution steps will have happen irrespective of above/dependent steps
# This is very important when using playwright with javascript or type script as they are asynchronous in nature.
# not mandatory for playwright+pytest as they supports both sync and async nature.
# this approach is useful when doing API testing.

# from playwright.sync_api import Page, expect, Playwright
from playwright.async_api import async_playwright, Page, expect, Playwright
import pytest
from pytest_playwright.pytest_playwright import browser

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        mypage = await browser.new_page()
        await mypage.goto("https://rahulshettyacademy.com/AutomationPractice/")
        await expect(mypage).to_have_url("https://rahulshettyacademy.com/AutomationPractice/")


# pytest day18-pw/test_playwright_async.py -s -v --headed