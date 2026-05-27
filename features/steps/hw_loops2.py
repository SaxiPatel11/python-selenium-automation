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


@given("User opens Target product page")
def open_product_page(context):
    context.driver.get(
        "https://www.target.com/p/women-s-smocked-blouse-universal-thread-red/-/A-95081560"
    )
    time.sleep(5)


@then("User selects each available color and verifies selection")
def select_colors(context):

    driver = context.driver

    # Locate all color buttons (swatches)
    colors = driver.find_elements(
        By.XPATH,
        "//button[contains(@aria-label,'color') or contains(@data-test,'swatch')]"
    )

    print("Total colors found:", len(colors))

    for i in range(len(colors)):
        # Re-fetch each time to avoid stale element issue
        colors = driver.find_elements(
            By.XPATH,
            "//button[contains(@aria-label,'color') or contains(@data-test,'swatch')]"
        )

        color = colors[i]
        color_name = color.get_attribute("aria-label")

        print("Selecting color:", color_name)

        # Click color
        color.click()
        time.sleep(2)

        # Verify selection (active state)
        selected = color.get_attribute("aria-pressed") or color.get_attribute("class")

        assert (
            "selected" in selected or selected == "true"
        ), f"Color not selected properly: {color_name}"

        print("Verified:", color_name)


def after_scenario(context, scenario):
    context.driver.quit()