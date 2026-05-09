from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_Confirmation:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_link = (By.XPATH, "//button[normalize-space()='Checkout']")
        self.country = (By.CSS_SELECTOR, "input[id='country']")
        self.checkbox = (By.XPATH, "//label[@for='checkbox2']")
        self.purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.text_msg = By.XPATH, "//div[@class='alert alert-success alert-dismissible']"

    def checkout(self):
        self.driver.find_element(*self.checkout_link).click()

    def select_address(self):
        self.driver.find_element(*self.country).send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(*self.checkbox).click()

    def purchase(self):
        self.driver.find_element(*self.purchase_button).click()

    def validate_order(self):
        success_msg = self.driver.find_element(*self.text_msg).text
        print(success_msg)
        assert "Success!" in success_msg