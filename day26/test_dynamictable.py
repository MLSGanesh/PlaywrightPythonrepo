import pytest
import re
from playwright.sync_api import sync_playwright,Page,expect

# @pytest.mark.skip
def test_verify_chrome_cpu(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table=page.locator("table.table tbody")

    # Get all rows from the table
    rows=table.locator("tr").all()

    cpu_load=""
    for row in rows:
        browser_name=row.locator("td").nth(0).inner_text()
        if browser_name=="Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome: ",cpu_load)
            break

    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)

# @pytest.mark.skip
def test_cpu_percentage(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table#taskTable tbody")

    # Get all rows from the table
    rows = table.locator("tr").all()

    cpu_load = ""
    for row in rows:
        browser_name = row.locator("td").nth(0).inner_text()
        if browser_name == "Chrome":
            cpu_load = row.locator("td:has-text('%')").inner_text()
            # cpu_load = row.locator("td",has_text="%").inner_text()

            print("CPU % of Chrome: ", cpu_load)
            break

    expect(page.locator("strong.chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)

def test_firefox_memory(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table#taskTable tbody")

    # Get all rows from the table
    rows = table.locator("tr").all()

    memory_load = ""
    for row in rows:
        browser_name = row.locator("td").nth(0).inner_text()
        if browser_name == "Firefox":
            memory_load = row.locator("td",has_text=re.compile("MB$")).inner_text()
            print("Memory size of Firefox: ", memory_load)
            break

    expect(page.locator("strong.firefox-memory")).to_contain_text(memory_load)

    page.wait_for_timeout(5000)

def test_network_speed(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table#taskTable tbody")

    # Get all rows from the table
    rows = table.locator("tr").all()

    network_speed = ""
    for row in rows:
        browser_name = row.locator("td").nth(0).inner_text()
        if browser_name == "Chrome":
            network_speed = row.locator("td",has_text='Mbps').inner_text()
            print("Network Speed of Chrome: ", network_speed)
            break

    expect(page.locator("strong.chrome-network")).to_contain_text(network_speed)

    page.wait_for_timeout(5000)

def test_disk_space(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table#taskTable tbody")

    # Get all rows from the table
    rows = table.locator("tr").all()

    disk_space = ""
    for row in rows:
        browser_name = row.locator("td").nth(0).inner_text()
        if browser_name == "Firefox":
            disk_space = row.locator("td",has_text='MB/s').inner_text()
            print("Disk Space of Firefox: ", disk_space)
            break

    expect(page.locator("strong.firefox-disk")).to_contain_text(disk_space)

    page.wait_for_timeout(5000)