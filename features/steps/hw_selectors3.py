from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome in Incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Launch browser
driver = webdriver.Chrome(options=chrome_options)

# Given User opens Target homepage
driver.get("https://www.target.com/")
driver.maximize_window()
time.sleep(3)

# When User clicks on the Sign In button
sign_in_btn = driver.find_element(By.XPATH, "//span[text()='Sign in']")
sign_in_btn.click()
time.sleep(2)

# And User clicks Sign In from the right side navigation menu
side_sign_in = driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]")
side_sign_in.click()
time.sleep(3)

# Then verify Sign In form is displayed
sign_in_form = driver.find_element(By.XPATH, "//*[contains(text(),'Sign in or create account')]")

if sign_in_form.is_displayed():
    print("Test Passed: Sign In form opened successfully")
else:
    print("Test Failed")

# Close browser
time.sleep(5)
driver.quit()