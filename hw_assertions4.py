from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()


@given("User opens Target Help page")
def open_help_page(context):
    context.driver.get("https://help.target.com/help")
    time.sleep(4)


@then("Main UI elements should be visible")
def verify_help_ui(context):

    driver = context.driver

    # 1. Page header / logo
    header = driver.find_element(By.TAG_NAME, "header")

    # 2. Search box
    search_box = driver.find_element(By.XPATH, "//input[@type='search' or @placeholder]")

    # 3. Help categories section (common container)
    categories = driver.find_elements(By.XPATH, "//a | //button")

    # 4. Help title (fallback text check)
    title = driver.find_element(By.XPATH, "//*[contains(text(),'Help')]")

    # Assertions (basic validation)
    assert header.is_displayed(), "Header not visible"
    assert search_box.is_displayed(), "Search box not visible"
    assert len(categories) > 0, "Help categories not found"
    assert title.is_displayed(), "Help page title not visible"

    print("UI Verification Passed")


def after_scenario(context, scenario):
    context.driver.quit()