from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils
from .shoppage import ShopPage


class LoginPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.userpass_input = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")

    def signin(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.userpass_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        shoppage = ShopPage(self.driver)
        return shoppage
