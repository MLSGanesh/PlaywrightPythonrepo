import time

from playwright.sync_api import Page,expect

def test_example(page:Page):
    page.goto("https://books-pwakit.appspot.com")
    page.locator("#input").fill("Welcome")  # CSS
    # page.locator('book-app').get_by_role("textbox",name="Search Books").fill("Welcome") # Selectors Hub selection
    # page.get_by_role("searchbox", name="Search Books").fill("Welcome")  # Direct
    time.sleep(5)
