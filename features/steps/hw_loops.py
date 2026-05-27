from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup browser (runs once per scenario)
def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

    # ✅ reusable wait
    context.wait = WebDriverWait(context.driver, 10)


@given("User opens Target homepage")
def open_target(context):
    context.driver.get("https://www.target.com/")

    # wait until search box is loaded
    context.wait.until(
        EC.presence_of_element_located((By.ID, "search"))
    )


@when('User searches for "{product}"')
def search_product(context, product):

    search_box = context.wait.until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    search_box.send_keys(product)
    search_box.submit()

    # wait until results load (product cards appear)
    context.wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@data-test,'productCard')]")
        )
    )


@then('Search results for "{product}" should be displayed')
def verify_results(context, product):

    result = context.wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{product}')]")
        )
    )

    assert result.is_displayed(), f"{product} results not displayed"


# Cleanup after scenario
def after_scenario(context, scenario):
    context.driver.quit()