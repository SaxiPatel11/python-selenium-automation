from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome in Incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Launch browser
driver = webdriver.Chrome(options=chrome_options)

# Open Stack Overflow Create Account page
driver.get("https://stackoverflow.com/users/signup")
driver.maximize_window()

# Wait for page to load
time.sleep(3)

# Locate elements
display_name = driver.find_element(By.ID, "display-name")
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")
signup_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_link = driver.find_element(By.LINK_TEXT, "Log in")

# Enter test data
display_name.send_keys("Test User")
email.send_keys("testuser123@gmail.com")
password.send_keys("Password123!")

# Verify elements are displayed
print("Display Name field displayed:", display_name.is_displayed())
print("Email field displayed:", email.is_displayed())
print("Password field displayed:", password.is_displayed())
print("Sign Up button displayed:", signup_button.is_displayed())
print("Login link displayed:", login_link.is_displayed())

# Optional: Click Sign Up button
# signup_button.click()

# Wait to observe
time.sleep(5)

# Close browser
driver.quit()