'''
valid data login success : pass
valid data login unsuccess : fail

invalid data login success : fail
invalid data login unsuccess : pass
'''

login_test_data= [("mlsganesh72@gmail.com","Mls123","Valid"),("satyaganesh72@gmail.com","Mls123","Invalid"), ("mlsganesh72@gmail.com","Mls23","Invalid"),("satyaganesh72@gmail.co","Mls123","Invalid")]

import pytest
from playwright.sync_api import sync_playwright, Playwright, Page, expect


@pytest.mark.parametrize("email,password,validity",login_test_data)
def test_login(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    # fill the login form
    page.locator(".email").fill(email) # enter email
    page.locator(".password").fill(password)  # enter Password
    page.locator("input[value='Log in']").click()

    # validation
    if validity=="Valid":
        logout_button=page.locator("a[href='/logout']")
        expect(logout_button).to_be_visible(timeout=5000)
    else:
        error_msg=page.locator(".validation-summary-errors")
        expect(error_msg).to_be_visible(timeout=5000)  # checking error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login") # checking URL