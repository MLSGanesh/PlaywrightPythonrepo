from playwright.sync_api import sync_playwright, expect, Playwright


# Browser ---> context ----> page(s)
def test_browsercontext(playwright:Playwright):
    # chromium=playwright.chromium
    # browser=chromium.launch()

    browser=playwright.chromium.launch(headless=False)  # created browser
    context=browser.new_context()   # created context
    page1 = context.new_page()   # created page1
    page2 = context.new_page()   # created page2

    # by creating multiple pages user can work on different urls at a time, where as using one page only one url can be handled at a time(by replacing the earlier one)

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(5000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://selenium.dev/")
    page2.wait_for_timeout(5000)
    expect(page2).to_have_title("Selenium")