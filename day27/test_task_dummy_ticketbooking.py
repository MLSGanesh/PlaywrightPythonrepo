import pytest
from playwright.sync_api import Page,expect

def select_date_of_birth(page,birth_year,birth_month,birth_day):
    # select year
    page.locator(".ui-datepicker-year").select_option(birth_year)
    # select month
    page.locator(".ui-datepicker-month").select_option(birth_month)
    # select date
    date_cells=page.locator("table[class='ui-datepicker-calendar'] tbody td").all()
    for cell in date_cells:
        if cell.text_content()==birth_day:
            cell.click()
            break

def select_date(page,required_year,required_month,required_day):
    # select year
    page.locator(".ui-datepicker-year").select_option(required_year)
    # select month
    page.locator(".ui-datepicker-month").select_option(required_month)
    # select date
    date_cells=page.locator("table[class='ui-datepicker-calendar'] tbody td").all()
    for cell in date_cells:
        if cell.text_content()==required_day:
            cell.click()
            break

def test_dummy_tbooking(page:Page):
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

    # expect(page).to_have_title("")
    page.locator("input[id='product_549']").click()

    firstname=page.locator("#travname")
    firstname.fill("Lokesh Satya Ganesh")
    lastname = page.locator("#travlastname")
    lastname.fill("Medisetti")

    birth_year="1992"
    birth_month="Jun"
    birth_day="26"
    dob=page.locator("input[id='dob']")
    dob.click()
    select_date_of_birth(page,birth_year,birth_month,birth_day)

    dob_value= dob.input_value()
    print("DOB Value: ",dob_value)
    # expect(dob_value).to_have_value('26/06/1992')

    # select sex
    page.locator("#sex_1").check()
    expect(page.locator("#sex_1")).to_be_checked()

    # check Add more passenger checkbox
    page.locator("#addmorepax").check()
    expect(page.locator("#addmorepax")).to_be_checked()

    # Trip type
    page.locator("#traveltype_1").check()
    expect(page.locator("#traveltype_1")).to_be_checked()

    # from city
    page.locator("#fromcity").fill("Hyderabad")
    page.locator("#tocity").fill("Sydney")
    expect(page.locator("#fromcity")).to_have_value('Hyderabad')
    expect(page.locator("#tocity")).to_have_value('Sydney')

    # select departure date
    required_year= "2026"
    required_month= "Dec"
    required_day= "20"
    page.locator("#departon").click()
    select_date(page,required_year,required_month,required_day)

    # verify departure date
    depart_date=page.locator("#departon").input_value()
    print("Departure Date: ",depart_date)
    # expect(depart_date).to_have_value("20/12/2026")

    # Additional info
    page.locator("#notes").fill("Need Visa asap")
    expect(page.locator("#notes")).to_have_value('Need Visa asap')



    page.wait_for_timeout(5000)


