import pytest
from playwright.sync_api import Page,expect

def test_radio_buttons(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_radio=page.locator("#male")

    # visibility of element and enabled or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    # Male radio button should not be checked/slected by default
    expect(male_radio).not_to_be_checked()

    # select/check radio button: Action
    male_radio.check()

    # Male radio button should be checked/selected
    expect(male_radio).to_be_checked()