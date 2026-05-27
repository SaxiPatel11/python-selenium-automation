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

# When User clicks on the cart icon
cart_icon = driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']")
cart_icon.click()
time.sleep(3)

# Then verify "Your cart is empty" message is displayed
empty_cart_message = driver.find_element(By.XPATH, "//*[contains(text(),'Your cart is empty')]")

if empty_cart_message.is_displayed():
    print("Test Passed: 'Your cart is empty' message is displayed")
else:
    print("Test Failed")

# Close browser
time.sleep(5)
driver.quit()