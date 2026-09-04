import pytest
from playwright.sync_api import Page, expect

def test_xpath_locators(page: Page):
    # Launch URL
    page.goto("https://demowebshop.tricentis.com/")

    # 1. Absolute XPath (full xpath)   : Not recommended
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    # 2. Releative XPath: //tagname[@attribute='value']]
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

    # 3. xpath with contains()
    products=page.locator("//h2//a[contains(@href,'computer')]")
    products_count = products.count()
    print("Products Count: ",products_count)
    expect(products).to_have_count(products_count)

    print("First Computer: ",products.first.text_content())
    print("Last Computer: ", products.last.text_content())
    print("N-th Computer: ", products.nth(2).text_content()) #nth() takes index from 0

    product_titles=products.all_text_contents()
    print("Product Titles: ",product_titles)

    print("Printing Product titles using looping statement....")
    for i in product_titles:
        print(i)

    # 4. xpath with starts-with()
    building_products=page.locator("//h2//a[starts-with(@href,'/build')]")
    print("Count of building products: ",building_products.count())
    expect(building_products).to_have_count(building_products.count())

    # 5. xpath with text() - text is representing inner text of the element
    # <input text="xyz">
    # <input name="abc">welcome</input> "here welcome is inner text"

    reg_link=page.locator("//a[text()='Register']")
    expect(reg_link).to_be_visible()

    # 6. xpath with last()
    google_plus_link = page.locator("//div[@class='column follow-us']//li[last()]") # //div[@class='column follow-us']//li[5]
    expect(google_plus_link).to_be_visible()
    expect(google_plus_link).to_have_text("Google+")

    # 6. xpath with position()
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_be_visible()
    expect(twitter_link).to_have_text("Twitter")

