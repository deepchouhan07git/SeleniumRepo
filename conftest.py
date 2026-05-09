import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        option = Options()
        option.add_argument("--incognito")
        driver = webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    # Go to the URL
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver
    driver.close()

# Hook to take SS for failed testcase
import pytest
from datetime import datetime
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            file_name = f"screenshots/{test_name}_{timestamp}.png"

            driver.save_screenshot(file_name)

            # Attach to pytest-html report
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(file_name))
            else:
                report.extra = []
                from pytest_html import extras
                report.extra.append(extras.image(file_name))