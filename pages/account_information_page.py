from playwright.sync_api import Page


class AccountInformationPage:
    URL = "https://automationexercise.com/signup"

    def __init__(self,page: Page):
        self.page = page
        self.gender_input = page.locator('#id_gender1')
        self.name_input = page.locator('[data-qa="name"]')
        self.email_input = page.locator('[data-qa="email"]')
        self.password_input = page.locator('[data-qa="password"]')
        self.birth_day_input = page.locator('#uniform-days')
        self.birth_month_input = page.locator('#uniform-months')
        self.birth_years_input = page.locator('#uniform-years')
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.address_input = page.locator('[data-qa="address"]')
        self.country_input = page.locator('#country')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_input = page.locator('[data-qa="mobile_number"]')
        self.submit_button = page.locator('[data-qa="create_account"]')


    def navigate(self):
        self.page.goto(self.URL)


    def account_information(self, password, day, month, year):
        self.gender_input.check()
        self.password_input.fill(password)
        self.birth_day_input.select_option(day)
        self.birth_month_input.select_option(month)
        self.birth_years_input.select_option(year)

    def address_information(self, first, last, address,country, state, city, zipcode, mobile,):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.address_input.fill(address)
        self.country_input.select_option(country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_input.fill(mobile)

    def submit(self):
        self.submit_button.click()