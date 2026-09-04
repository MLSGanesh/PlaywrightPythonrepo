'''
1) tag & id:       tag#id
2) tag & class:    tag.class
3) tag & attribute: tag[attribute=value]
4) tag, class & attribute: tag.class[attribute=value]
'''

import pytest
from playwright.sync_api import Playwright, Page, expect

def test_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # tag & id
    search_box=page.locator("input#small-searchterms")
    search_box.fill("Trackpants")
    page.locator("#small-searchterms").fill("T Shirts") # even without tag user can identify the element
    page.wait_for_timeout(5000)

    # tag & class
    reg = page.locator("a.ico-register")
    # page.locator("input.search-box-text ui-autocomplete-input").fill("Shirts")
    # page.locator("input.search-box-text").fill("Shirts")
    page.locator(".search-box-text").fill("Shirts") # even without tag user can identify the element
    page.wait_for_timeout(5000)

    # tag & attribute
    # page.locator("input[name=q]").fill("Pants")
    page.locator("[name=q]").fill("Pants")
    page.wait_for_timeout(5000)

    # tag, class & attribute
    # page.locator("input.search-box-text[name=q]").fill("Trackpants")
    # page.locator("input.search-box-text[value='Search store']").fill("Trackpants")
    page.locator(".search-box-text[value='Search store']").fill("Trackpants")


# pytest day20/test_csslocators.py -s -v --headed
