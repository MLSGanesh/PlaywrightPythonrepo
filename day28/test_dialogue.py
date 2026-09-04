import pytest
from playwright.sync_api import sync_playwright,Page,expect
from scipy.signal import periodogram


@pytest.mark.skip
def test_simple_dialogue(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Approach 1
    # registering an event by creating a function to handle dialog/alert. alert is called as dialog in python
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog)
    page.wait_for_timeout(5000)
    page.locator("#alertBtn").click()    # clicking the button
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_simple_dialogue2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Approach 2: using lambda

    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(5000)
    page.locator("#alertBtn").click()    # clicking the button
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_confirmation_dialogue(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # page.on("dialog",lambda dialog:dialog.accept())
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(3000)
    page.locator("#confirmBtn").click()    # clicking the button
    page.wait_for_timeout(5000)
    text= page.locator("#demo").inner_text()
    print("Output Dialogue:", text)
    # expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")

def test_prompt_dialogue(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept("MLS"))
    # page.on("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(3000)
    page.locator("#promptBtn").click()    # clicking the button
    page.wait_for_timeout(5000)
    text= page.locator("#demo").inner_text()
    print("Output Dialogue:", text)
    # expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("Hello MLS! How are you today?")