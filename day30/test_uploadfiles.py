import pytest
from playwright.sync_api import Page,expect

@pytest.mark.skip
def test_singlefileupload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Upload single file
    page.locator("#singleFileInput").set_input_files("uploads/Prompt.txt")
    page.locator("button:has-text('Upload Single File')").click()

    # Validation
    msg=page.locator("#singleFileStatus")
    expect(msg).to_contain_text("Prompt.txt")

    page.wait_for_timeout(5000)

def test_uploadmultiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Upload single file
    files=["uploads/New Microsoft Excel Worksheet.xlsx","uploads/Prompt.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()

    # Validation
    msg=page.locator("#multipleFilesStatus")
    expect(msg).to_contain_text("Prompt.txt")
    expect(msg).to_contain_text("New Microsoft Excel Worksheet.xlsx")

    page.wait_for_timeout(5000)
