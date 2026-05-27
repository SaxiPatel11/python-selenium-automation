from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


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


@when("User selects the first product")
def select_product(context):
    products = context.driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'/p/')]"
    )
    products[0].click()
    time.sleep(3)


@when("User adds the product to cart")
def add_to_cart(context):
    add_button = context.driver.find_element(
        By.XPATH,
        "//button[contains(.,'Add to cart')]"
    )
    add_button.click()
    time.sleep(3)


@then("Cart should contain at least 1 item")
def verify_cart(context):
    # Open cart
    cart_icon = context.driver.find_element(
        By.XPATH,
        "//a[@data-test='@web/CartLink']"
    )
    cart_icon.click()
    time.sleep(3)

    # Check cart items OR quantity indicator
    items = context.driver.find_elements(
        By.XPATH,
        "//div[contains(@data-test,'cartItem')]"
    )

    # Alternative check (fallback)
    count = len(items)

    print("Cart items found:", count)

    assert count >= 1, "Cart is empty - item not added"


def after_scenario(context, scenario):
    context.driver.quit()