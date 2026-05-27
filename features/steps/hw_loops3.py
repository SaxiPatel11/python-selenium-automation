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
def open_homepage(context):
    context.driver.get("https://www.target.com/")
    time.sleep(4)


@when('User searches for "{product}"')
def search_product(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_box.submit()
    time.sleep(5)


@then("Each product should have a name and an image")
def validate_products(context):

    driver = context.driver

    # Locate product cards
    products = driver.find_elements(
        By.XPATH,
        "//div[contains(@data-test,'productCard')]"
    )

    print("Total products found:", len(products))

    assert len(products) > 0, "No products found on search results page"

    for index, product in enumerate(products):

        # Product name (usually link text inside card)
        names = product.find_elements(By.XPATH, ".//a[contains(@href,'/p/')]" )

        # Product image
        images = product.find_elements(By.XPATH, ".//img")

        assert len(names) > 0, f"Product {index} missing name"
        assert len(images) > 0, f"Product {index} missing image"

        # Additional validation
        assert names[0].is_displayed(), f"Product {index} name not visible"
        assert images[0].is_displayed(), f"Product {index} image not visible"

        print(f"Product {index+1} validated")


def after_scenario(context, scenario):
    context.driver.quit()