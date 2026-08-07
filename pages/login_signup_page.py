from playwright.sync_api import Page

class LoginSignupPage:
    URL = "https://automationexercise.com/login"

    def __init__(self,page: Page):
        self.page = page
        self.signup_name_input = page.locator('[data-qa="signup-name"]')
        self.signup_email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.login_password_input = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.error_visible = page.get_by_text("Your email or password is incorrect!")

    def navigate(self):
        self.page.goto(self.URL)


    def signup(self, username, email):
        self.signup_name_input.fill(username)
        self.signup_email_input.fill(email)
        self.signup_button.click()



    def login(self, email, password):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def is_error_visible(self):
        return self.error_visible.is_visible()