import pytest
from playwright.sync_api import expect,Page
import re

# using xpath

# def test_handle_dynamic_elements(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
    # xpaths
    # //button[text()='START' or text()='STOP']
    # //button[@name='START' or @name='STOP']
    # //button[contains(@name,'st')]
    # //button[starts-with(@name,'st')]

    # for i in range(5):
    #     button = page.locator("//button[text()='START' or text()='STOP']")
    #     button.click()
    #     page.wait_for_timeout(5000)

# using css
    # css selectors
    # button[name='START'],button[name='STOP']
    # button[name^='st']  # equals to starts-with() in xpath
    # button[name*='st']  # equals to contains() in xpath

# def test_handle_dynamic_elements(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     for i in range(5):
#         button = page.locator("button[name^='st']")
#         button.click()
#         page.wait_for_timeout(5000)

# using playwright locator......

def test_handle_dynamic_elements(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    for i in range(5):
        button = page.get_by_role("button",name=re.compile(r'ST.*'))
        button.click()
        page.wait_for_timeout(5000)

# pytest day21/test_dynamicxpaths.py -s -v --headed

