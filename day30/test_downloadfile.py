import os
from playwright.sync_api import Page, expect

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("Welcome")
    page.locator("#generateTxt").click()

    # Approach 1: registering an event
    # def handle_download(download):
    #     download.save_as("downloads/testfile.txt")
    #
    # page.on("download",handle_download)

    # Approach 2: lambda
    page.on("download",lambda download:download.save_as("downloads/testfile.txt"))

    page.locator("#txtDownloadLink").click()

    page.wait_for_timeout(5000)

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")
    else:
        print("File doesn't exist")