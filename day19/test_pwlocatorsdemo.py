'''
1) page.get_by_alt_text()
2) page.get_by_text()
3) page.get_by_role()
4) page.get_by_label()
5) page.get_by_placeholder()
6) page.get_by_title()
7) page.get_by_test_id()
'''
import time
import pytest
import re
from playwright.sync_api import Playwright, Page, expect

# def test_verify_pwlocators(page:Page):
#     page.goto("https://demo.nopcommerce.com/")
#     time.sleep(5)
#     page.wait_for_timeout(5000)
#     # page.get_by_alt_text()
#     logo = page.get_by_alt_text("nopCommerce demo store")
#     expect(logo).to_be_visible()
#     page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
#     time.sleep(5)

# def test_verify_pwlocators(page:Page):
#     page.goto("http://localhost/opencart/upload/")
#     time.sleep(5)
#     page.wait_for_timeout(5000)
#
#     # 1) page.get_by_alt_text()
#     logo = page.get_by_alt_text("Your Store")
#     expect(logo).to_be_visible()
#     print(logo)
#
#     # 2) page.get_by_text()
#     feature = page.get_by_text("Featured")
#     expect(feature).to_be_visible()
#     print(feature)
#
#     # 3) page.get_by_role()
#     search=page.get_by_role("textbox",name="search")
#     expect(search).to_be_visible()
#     page.wait_for_timeout(5000)
#     search.fill("Mobile")
#     sbutton=page.get_by_role("button", name="")
#     sbutton.click()
#
#     # 4) page.get_by_label()
#     page.wait_for_timeout(5000)
#     criteria=page.get_by_label("Search Criteria")
#     expect(criteria).to_be_visible()
#     print(criteria)
#
#     # 5) page.get_by_placeholder()
#     mobile_search=page.get_by_placeholder("Keywords")
#     mobile_search.fill("Tablets")
#     search_button=page.get_by_role("button",name="Search")
#     search_button.click()
#     page.wait_for_timeout(5000)
#
#     # 6) page.get_by_title()
#     my_account_title = page.get_by_title("My Account")
#     expect(my_account_title).to_be_visible()
#
#     # 7) page.get_by_test_id()
#     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
#     id = page.get_by_test_id("profile-name")
#     expect(id).to_have_text("John Doe")
#     mail = page.get_by_test_id("profile-email")
#     expect(mail).to_have_text("john.doe@example.com")
#     page.wait_for_timeout(5000)


def test_orangeDashboard(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    uname = page.get_by_placeholder("Username")
    expect(uname).to_be_visible()
    uname.fill("Admin")
    pwd = page.get_by_placeholder("Password")
    expect(pwd).to_be_visible()
    pwd.fill("admin123")
    login=page.get_by_role("button",name="Login")
    login.click()
    page.wait_for_timeout(5000)
    dashboard = page.get_by_role("heading",name="Dashboard")
    expect(dashboard).to_be_visible()
    print(dashboard)




# def test_popup(page:Page):
#     page.goto("https://www.espncricinfo.com/")
#     page.wait_for_timeout(2)
#     page.get_by_role("button", name="Accept All").click()
#     page.wait_for_timeout(2)
#
#     # 1) page.get_by_alt_text()
#     logo = page.get_by_alt_text("Cricinfo")
#     expect(logo).to_be_visible()
#     print(logo)
#
#     # 2) page.get_by_text()
#     livescore=expect(page.get_by_text("Live Scores")).to_be_visible()  # full text
#     expect(page.get_by_text("Live S")).to_be_visible()  # partial text
#     expect(page.get_by_text(re.compile(".*Live.*"))).to_be_visible()  # regular expression
#     print(livescore)
#
#     # 3) page.get_by_role()



# def test_verify_pwlocators(page:Page):
#     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
#     # page.goto("https://www.sreenidhirajakrishnan.com/practice")
#     page.wait_for_timeout(5000)
#     # 1) page.get_by_alt_text()
#     logo = page.get_by_alt_text("First slide")
#     # expect(logo).to_be_visible()
#
#     # 2) page.get_by_text()
#     expect(page.get_by_text("Practice Page")).to_be_visible() #full text
#     expect(page.get_by_text("Practice Pa")).to_be_visible()  # partial text
#     # expect(page.get_by_text(re.compile(".*Practice.*"))).to_be_visible()  # regular expression
#
#     # 3) page.get_by_role()
#     home=page.get_by_role("button",name="Home")
#     expect(home).to_be_visible()
#     # page.wait_for_timeout(5000)
#     # home.click()
#
#     # 4) page.get_by_label()
#     label= page.get_by_label("Suggession Class Example")
#     expect(label).to_be_visible()
#     print(label)
#
#     # 5) page.get_by_placeholder()



# testautomationpractice.blogspot.com
# pytest day19/test_pwlocatorsdemo.py -s -v --headed