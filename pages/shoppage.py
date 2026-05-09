from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils
from .Checkout_Confirmation import Checkout_Confirmation


class ShopPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.XPATH, "//a[contains(text(), 'Shop')]")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_link = (By.XPATH, "//a[contains(text(), 'Checkout')]")

    def add_product(self, name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)
        print(len(products))

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == name:
                product.find_element(By.XPATH, "div[2]/button").click()

    def gotocart(self):
        self.driver.find_element(*self.checkout_link).click()
        order_validation = Checkout_Confirmation(self.driver)
        return order_validation