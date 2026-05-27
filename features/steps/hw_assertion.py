from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup browser (runs once per scenario)
def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()


@given("User opens Target homepage")
def open_target(context):
    context.driver.get("https://www.target.com/")
    time.sleep(3)


@when('User searches for "{product}"')
def search_product(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_box.submit()
    time.sleep(3)


@then('Search results for "{product}" should be displayed')
def verify_results(context, product):
    results = context.driver.find_element(
        By.XPATH,
        f"//*[contains(text(), '{product}')]"
    )
    assert results.is_displayed(), f"{product} results not displayed"


# Cleanup after scenario
def after_scenario(context, scenario):
    context.driver.quit()