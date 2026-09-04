from playwright.sync_api import Playwright, Page, expect

def test_login_error_message(page: Page):
    """
    Test to verify that the login error message is displayed
    when invalid credentials are provided.
    """
    # Navigate to the login page
    page.goto("https://www.google.com")  # Replace with your actual login URL
    assert page.title() == "Google"  # Replace with the expected title of your login page
    # Enter invalid credentials