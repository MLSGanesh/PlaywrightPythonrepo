from playwright.sync_api import Page

class CartPage:
    def __init__(self,page:Page):
        self.page=page
        # CSS Selector to select all product name cells in the cart table
        self.product_names_locator= "#tbodyid tr td:nth-child(2)"

    def check_product_in_cart(self,product_name):
        products=self.page.locator(self.product_names_locator)
        count=products.count()

        for i in range(count):
            name=products.nth(i).text_content().strip()
            if name==product_name:
                return products.nth(i) # returning product

        return None