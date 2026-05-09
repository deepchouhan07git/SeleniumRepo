import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.shoppage import ShopPage
from pages.loginpage import LoginPage

test_file_path = "../data/test_e2eframework.json"
with open(test_file_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize('test_list_items', test_list)
def test_e2e(browserInstance, test_list_items):
    driver = browserInstance

    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    shoppage = loginpage.signin(test_list_items["userEmail"], test_list_items["userPass"])
    print(shoppage.getTitle())
    shoppage.add_product(test_list_items["productName"])
    order_validation = shoppage.gotocart()
    order_validation.checkout()
    order_validation.select_address()
    order_validation.purchase()
    order_validation.validate_order()
