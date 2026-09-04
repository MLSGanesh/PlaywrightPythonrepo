'''
import: openpyxl
using 'pip install openpyxl'
'''
import openpyxl
import pytest
from playwright.sync_api import Page, expect

# reading data from excel
login_data=[]
workbook=openpyxl.load_workbook("testdata/data.xlsx")
sheet=workbook.active             # if multiple sheets are there then use syntax 'worksheet["sheetname"]'

# reading data from excel sheet using for loop
for row in sheet.iter_rows(min_row=2,values_only=True):
    email,password,validity=row
    login_data.append((str(email or ""),str(password or ""), str(validity or "")))
workbook.close()

@pytest.mark.parametrize("email,password,validity", login_data)
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