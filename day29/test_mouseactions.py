import pytest
from playwright.sync_api import Page,expect

@pytest.mark.skip
def test_mouse_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pointme=page.locator(".dropbtn")
    pointme.hover()

    # laptops=page.locator(".dropdown-content a").nth(1) # using index
    laptops = page.locator(".dropdown-content a:nth-child(2)")  # using index in css

    laptops.hover()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_rightclick(page:Page):
    page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

    button_r=page.locator(".context-menu-one")
    button_r.click(button="right")  # performs right click action. actions are left, right and middle

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_doubleclick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    v_field= page.locator("#field2")
    expect(v_field).to_have_value("")

    d_button=page.locator("button[ondblclick='myFunction1()']")
    d_button.dblclick()   # to perform double click

    expect(v_field).to_have_value("Hello World!")

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_draganddrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    # Approach 1: manual drop using hover()
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    # Approach 2: Prefferable
    source.drag_to(target)

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_draganddrop_assgn(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")

    dg_1 = page.locator("#credit2")
    dp_1 = page.locator("#bank li")

    dg_2 = page.locator("#fourth a").first
    dp_2 = page.locator('#amt7 li')

    dg_3 = page.locator("#credit1 a")
    dp_3 = page.locator('#loan li')

    dg_4 = page.locator("#fourth a").nth(1)
    dp_4 = page.locator("#amt8 li")

    dg_1.drag_to(dp_1)
    dg_2.drag_to(dp_2)
    dg_3.drag_to(dp_3)
    dg_4.drag_to(dp_4)

    page.wait_for_timeout(5000)

    # assert message
    perfect = page.locator("a:has-text('Perfect!')")
    expect(perfect).to_be_visible()

    page.wait_for_timeout(5000)

def test_espn_cric(page:Page):
    page.goto("https://www.cricinfo.com/")
    page.locator("#onetrust-accept-btn-handler").click()
    live_scores=page.locator("a[title='Live Cricket Score']")
    live_scores.is_visible()
    live_scores.hover()

    results=live_scores.locator("li[title='Live Cricket Match Results']")
    results.click()
    page.wait_for_timeout(5000)