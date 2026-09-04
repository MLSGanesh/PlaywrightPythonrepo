from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import datetime

def test_screenshots(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # timestamp=str(int(time.time()))   # package is time
    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # package is datetime (prefferable)
    # Page screenshot (partially/visible)

    # page.screenshot(path="screenshots/homepage.png")
    # page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    # Full page screenshot
    # page.screenshot(path=f"screenshots/homepage_{timestamp}.png",full_page=True)

    # Element or specific section of the page screenshot
    logo=page.locator(".header-logo")
    logo.screenshot(path=f"screenshots/logo_{timestamp}.png")

    featuredproducts=page.locator(".product-grid.home-page-product-grid")
    featuredproducts.screenshot(path=f"screenshots/products_{timestamp}.png")