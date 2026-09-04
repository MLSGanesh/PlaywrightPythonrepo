from playwright.sync_api import Page,expect

def test_keyboardactions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1=page.locator("#input1")

    # focus on input1
    input1.focus()

    # Enter text in input 1
    page.keyboard.insert_text("Welcome")

    # Select the entire input given
    page.keyboard.press("Control+A")

    # Copy the selected input given
    page.keyboard.press("Control+C")

    # Press tab twice to move to input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # Paste the selected detail in input2
    page.keyboard.press("Control+V")

    # Press tab twice to move to input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # Paste the selected detail in input3
    page.keyboard.press("Control+V")

    # verify the values in input2 and input3
    input2 = page.locator("#input2")
    input3 = page.locator("#input3")
    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")

    page.wait_for_timeout(5000)