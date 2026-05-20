from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome in Incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Open Target homepage
    driver.get("https://www.target.com/")
    driver.maximize_window()
    time.sleep(5)

    # 2. Click Account button
    account_btn = driver.find_element(By.XPATH, "//button[@aria-label='Account']")
    account_btn.click()
    time.sleep(3)

    # 3. Click Sign In button from side navigation
    signin_nav_btn = driver.find_element(
        By.XPATH, "//button[@aria-label='Account, sign in']"
    )
    signin_nav_btn.click()
    time.sleep(5)

    # 4. Verify Sign In page opened
    signin_text = driver.find_element(
        By.XPATH, "//h1[contains(text(),'Sign in or create account')]"
    )

    signin_btn = driver.find_element(
        By.XPATH, "//button[contains(text(),'Sign in')]"
    )

    print("Sign In page opened successfully.")
    print("Text found:", signin_text.text)

except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(3)
    driver.quit()