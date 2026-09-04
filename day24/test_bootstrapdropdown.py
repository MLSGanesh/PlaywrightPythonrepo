import pytest
from playwright.sync_api import Page,expect

def test_orangeDashboard(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # login steps
    page.locator('input[name="username"]').fill("Admin")
    page.locator('input[name="password"]').fill("admin123")
    page.locator('button[type="submit"]').click()

    page.wait_for_timeout(5000)

    # Click on PIM
    page.get_by_text("PIM").click()

    # click on job title dropdown
    page.locator('form i').nth(3).click() # this will open all options from dropdown
    page.wait_for_timeout(5000)

    # capture all options from dropdown
    options= page.locator("div[role='listbox'] span")

    count=options.count()  # get the count of options
    print("Number of options: ",count)

    expect(options).to_have_count(count)  # assertion for counting the options

    # print all the options
    print("All the options from the dropdown: ",options.all_text_contents())

    # Print all the options text using loop
    for i in range(count):
        print(options.nth(i).text_content())

    # select/click on specific option
    for i in range(count):
        text=options.nth(i).text_content()
        if text=="Sales":
            print("Matching....")
            options.nth(i).click()
            break

    page.wait_for_timeout(5000)
