import pytest
from playwright.sync_api import sync_playwright, Playwright, expect


def test_popups(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True,snapshots=True)
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # def handle_popup(popup):
    #     popup.wait_for_load_state()
    #
    # page.on("popup",handle_popup)

    page.on("popup", lambda popup:popup.wait_for_load_state())

    page.locator("#PopUp").click()
    page.wait_for_timeout(5000)

    all_popups=context.pages
    print("Total number of pages in browser:", len(all_popups))

    # capture urls of all pages
    for pw in all_popups:
        print("URLs of all pages:", pw.url)
        title = pw.title()
        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(5000)
            expect(pw).to_have_title("Installation | Playwright")
            pw.close()  # close popup/window

        page.wait_for_timeout(5000)

        context.tracing.stop(path="day31/trace.zip")
        context.close()
        browser.close()

# pytest day31/test_popups.py --headed --reruns 3 --reruns-delay 2