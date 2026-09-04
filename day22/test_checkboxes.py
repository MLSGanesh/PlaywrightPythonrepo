import pytest
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select specific checkbox
    sunday=page.get_by_label("Sunday")

    # visibility of element and enabled or not
    expect(sunday).to_be_visible()
    expect(sunday).to_be_enabled()

    # checkbox should not be checked/selected by default
    expect(sunday).not_to_be_checked()

    # select/check radio button: Action
    sunday.check()

    # checkbox should be checked/selected
    expect(sunday).to_be_checked()
    page.wait_for_timeout(5000)

    # Count number of checkboxes # here css/xpath can't be used as the group of elements fetched can't be return as list. And assertions can't be used on text content in python and can only be used on elements
    # step 1:
    days= ['Sunday', 'Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes=[]

    # step 2:
    # for day in days:
    #     checkbox=page.get_by_label(day)
    #     checkboxes.append(checkbox)

    checkboxes=[page.get_by_label(day) for day in days]
    print("Total number of checkboxes:", len(checkboxes))

    # 3. select all checkboxes and assert each check box is selected
    # for checkbox in checkboxes:
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()
    # page.wait_for_timeout(5000)
    #
    # # 4. Uncheck last three checkboxes
    # for checkbox in checkboxes[-3:]:
    #     checkbox.uncheck()
    #     expect(checkbox).not_to_be_checked()
    # page.wait_for_timeout(5000)
    #
    # # Toggle checkboxes: check the unchecked ones and uncheck the checked ones
    # for checkbox in checkboxes:
    #     if checkbox.is_checked():
    #         checkbox.uncheck()
    #         expect(checkbox).not_to_be_checked()
    #     else:
    #         checkbox.check()
    #         expect(checkbox).to_be_checked()
    # page.wait_for_timeout(5000)
    #
    #
    # # Randomly check checkboxes - check 1,3,6 checkboxes
    # indexes = [1,3,6]
    #
    # for i in indexes:
    #     checkboxes[i].check()
    #     expect(checkboxes[i]).to_be_checked()
    #
    # page.wait_for_timeout(5000)

    # select checkbox based on label/input value
    weekday= "Friday"

    for label in days:
        if label==weekday:
            check_box=page.get_by_label(label)
            check_box.check()
            expect(check_box).to_be_checked()

    page.wait_for_timeout(5000)



# pytest day22/checkboxes.py -s -v --headed