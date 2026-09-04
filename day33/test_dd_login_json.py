'''
valid data login success : pass
valid data login unsuccess : fail

invalid data login success : fail
invalid data login unsuccess : pass
'''

import pytest
from playwright.sync_api import Page, expect
import json

# read json file
file=open("testdata/data.json","r")
login_data=json.load(file)

@pytest.mark.parametrize("email,password,validity",[
    (data["email"],data["password"],data["valid"]) for data in login_data
])
def test_login_json(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    # fill the login form
    page.locator(".email").fill(email) # enter email
    page.locator(".password").fill(password)  # enter Password
    page.locator("input[value='Log in']").click()

    # validation
    if validity=="valid":
        logout_button=page.locator("a[href='/logout']")
        expect(logout_button).to_be_visible(timeout=5000)
    else:
        error_msg=page.locator(".validation-summary-errors")
        expect(error_msg).to_be_visible(timeout=5000)  # checking error message
        expect(page).to_have_url("https://demowebshop.tricentis.com/login") # checking URL