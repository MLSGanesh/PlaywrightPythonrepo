import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

search_items = ['laptop','Gift Card','smartphone','monitor']

@pytest.mark.parametrize("item",search_items)
def test_search_item(item,playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item)  # we need to pass item name
    page.locator("input[value='Search']").click()

    # Assertion
    first_result=page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item, ignore_case=True)

