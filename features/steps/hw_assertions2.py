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


@given("User opens Target Circle page")
def open_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    time.sleep(4)


@then('There should be 2 storycards under "Unlock added value"')
def verify_storycards(context):

    # Locate the section heading first
    section = context.driver.find_element(
        By.XPATH,
        "//*[contains(text(),'Unlock added value')]"
    )

    # Find storycards relative to the section
    storycards = context.driver.find_elements(
        By.XPATH,
        "//*[contains(text(),'Unlock added value')]/following::div[contains(@data-test,'storycard')]"
    )

    count = len(storycards)

    print("Storycards found:", count)

    assert count == 2, f"Expected 2 storycards but found {count}"


def after_scenario(context, scenario):
    context.driver.quit()