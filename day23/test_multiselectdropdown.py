import pytest
from playwright.sync_api import Page,expect

def test_multi_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from dropdown - 3 ways
    # page.locator("#colors").select_option(["Red","Green","Blue"]) # by label
    # page.locator("#colors").select_option(label=["Red", "Green", "White"])  # by label

    # page.locator("#colors").select_option(value=["Red", "Yellow", "White"])  # by value
    # page.locator("#colors").select_option(index=[3,1,6])  # by index

    dropdown_options=page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)

    options = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options)

    for option in options:
        print(option)

    page.wait_for_timeout(5000)


