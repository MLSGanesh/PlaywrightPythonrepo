# Page object class should have only elements and Action methods
# we shouldn't add any validations in page object classes, and validations should be present only in test cases

from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page = page     # to make the page fixture of constructor as class variable we are storing 'page' into class variable as 'self.page'
        self.login_link=self.page.locator("#login2") # and to make every variable as class variable storing them as "self.<variable>"
        self.user_input=self.page.locator("#loginusername")
        self.password_input=self.page.locator("#loginpassword")
        self.login_button=self.page.locator('button[onclick="logIn()"]')

    # Action methods
    def click_login_link(self):
        self.login_link.click()

    def enter_username(self,username):
        self.user_input.fill("")  # to clear the existing usernames if any are present
        self.user_input.fill(username)

    def enter_password(self,password):
        self.password_input.fill("")
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    # Action method can be called as single method
    def perform_login(self,username,password):
        self.login_link.click()
        self.user_input.fill("")  # to clear the existing usernames if any are present
        self.user_input.fill(username)
        self.password_input.fill("")
        self.password_input.fill(password)
        self.login_button.click()
