import pytest
from playwright.sync_api import sync_playwright, Playwright, expect, Page


# direct approach (not recommended): inject user login with url

# https://the-internet.herokuapp.com/basic_auth

# https://admin:admin@the-internet.herokuapp.com/basic_auth

@pytest.mark.skip
def test_auth_popup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("text=Congratulations")).to_be_visible()


# using context: we can pass user and pwd along with context
def test_authPopup_context(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={"username":"admin","password":"admin"})
    page=context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("text=Congratulations")).to_be_visible()
