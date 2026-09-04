import pytest
from playwright.sync_api import expect, Page

from loginpage import LoginPage
from homepage import HomePage
from cartpage import CartPage

@pytest.mark.parametrize("username, password, product_name",[("mlsg", "Mls123", "Nexus 6")])

def test_user_can_login_and_add_product_to_cart(page:Page,username,password,product_name):
    page.goto("https://demoblaze.com/index.html")

    # Login
    login_page=LoginPage(page) # creating an object for LoginPage for calling methods from it
    login_page.click_login_link()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()


    # Homepage
    home_page=HomePage(page)
    # page.wait_for_load_state()
    home_page.add_product_to_cart(product_name)
    page.wait_for_timeout(5000)
    home_page.go_to_cart()
    page.wait_for_timeout(5000)

    # Cart Page
    cart_page=CartPage(page)
    product_in_cart=cart_page.check_product_in_cart(product_name)
    expect(product_in_cart).to_be_visible()




