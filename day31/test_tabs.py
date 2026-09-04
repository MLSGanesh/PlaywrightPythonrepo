import pytest
from playwright.sync_api import sync_playwright,Playwright,expect

@pytest.mark.skip
def test_multiple_tabs(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parentpage=context.new_page()

    parentpage.goto("https://testautomationpractice.blogspot.com/")
    # register an event to handle tabs using lambda

    parentpage.on("page",lambda page:page.wait_for_load_state())
    parentpage.locator('button[onclick="myFunction()"]').click()        # or use 'button:has-text('New Tab')'
    parentpage.wait_for_timeout(5000)

    all_pages=context.pages
    print("Number of tabs/pages: ", len(all_pages))
    print("Title of Parent Page:", all_pages[0].title())
    print("Title of Child Page:", all_pages[1].title())

    childpage=all_pages[1]
    print("URL of child page:", childpage.url)

    context.close()
    browser.close()

def test_multiple_Orange_tabs(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parentpage=context.new_page()

    parentpage.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # create an event using lambda
    parentpage.on("page",lambda page:page.wait_for_load_state())
    parentpage.locator('a[href="http://www.orangehrm.com"]').click()
    parentpage.wait_for_timeout(5000)

    all_pages=context.pages
    print("Number of Pages:", len(all_pages))
    for tab in all_pages:
        print("URL:", tab.url)

    print("Title of Parent Page:",all_pages[0].title())
    print("Title of Child Page:", all_pages[1].title())

    childpage=all_pages[1]
    print("URL of child page:",childpage.url)


