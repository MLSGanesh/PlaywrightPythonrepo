from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import browser


def test_verifyPUrl(page:Page):
    page.goto("https://www.google.com/") # passing url
    expect(page).to_have_url("https://www.google.com/") # expected url

def test_verifyPageUrl(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    myurl = page.url
    print("Url of the application", myurl)
    expect(page).to_have_url("https://rahulshettyacademy.com/AutomationPractice/")

def test_verifyUrl(page:Page):
    page.goto("https://www.espncricinfo.com/")
    expect(page).to_have_url("https://www.espncricinfo.com/")

def test_verifyTitle(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    mytitle = page.title()
    print("Tile of the application", mytitle)
    # expect(page).to_have_title("Selenium, API Testing, Software Testing & More QA Tutorials  | Rahul Shetty Academy")

def test_verifyPTitle(page:Page):
    page.goto("https://www.google.com/")  # passing url
    page.wait_for_timeout(5000)
    mytitle = page.title()
    print(mytitle)
    # expect(page).to_have_title("Google")  # expected tile

# pytest day18-pw/test_playwright.py::test_verifyTitle -s -v --headed
# pytest day18-pw/test_playwright.py -s -v --headed --browser firefox
# pytest day18-pw/test_playwright.py -s -v --headed --browser firefox --browser chromium --browser webkit
# pytest day18-pw/test_playwright.py -s -v --headed --browser firefox --browser chromium --browser webkit -n 3
# pytest day18-pw/test_playwright.py -s -v --headed --browser firefox --browser chromium --browser webkit -n=3
# pytest day18-pw/test_playwright.py -s -v --headed --browser firefox --browser chromium --browser webkit --numprocesses 3
# pytest day18-pw/test_playwright.py::test_verifyPTitle -s -v --headed --browser-channel msedge
