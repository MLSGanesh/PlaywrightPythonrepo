from playwright.sync_api import Page
from playwright.sync_api import sync_playwright, expect

def test_comparisionofmethods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    products=page.locator(".product-title") # 6 products

    # 1) inner_text() vs text_content()

    # print("Using inner text()====>", products.nth(1).inner_text()) # returns actual text
    # print("Using text content()====>", products.nth(1).text_content()) # returns content with spl chars and spaces

    # count = products.count()
    # for i in range(count):
    #     product_name = products.nth(i).text_content()
        # print(product_name)
        # print(product_name.strip()) # strip is used to trim the spl chars and spaces appear for text_content()
        # product_name = print(products.nth(i).inner_text())
        # print(product_name)

    # 2) all_inner_texts() vs all_text_contents()
    # product_names = products.all_inner_texts()
    # product_names = products.all_text_contents()
    # print(product_names)
    # product_names_trimmed = [text.strip() for text in product_names]  # strip is used to trim the spl chars and spaces appear for all_text_contents()
    # print(product_names_trimmed)

    # 3) all()
    product_locators = products.all()
    # print(product_locators[0].inner_text())
    # for product_loc in product_locators:
    #     print(product_loc.inner_text())

    for i in range(len(product_locators)):
        print(product_locators[i].inner_text())
