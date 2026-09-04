import pytest
from playwright.sync_api import Page, expect

def test_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    name_field=page.locator("#name")

    # visibility of element and enabled or not
    expect(name_field).to_be_visible()
    expect(name_field).to_be_enabled()

    # check the attributes of the element
    expect(name_field).to_have_attribute("maxlength","15")

    # get an attribute of the element
    max_length=name_field.get_attribute("maxlength")
    print("Maximum length of inputbox:", max_length)

    # fill the text in input box
    name_field.fill("MLS Ganesh")

    # get entered value from input box
    enteredvalue=name_field.input_value()
    print("Entered Value: ",enteredvalue)

# pytest day22/test_inputbox.py -s -v --headed