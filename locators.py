from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(4)

#By Id
element = driver.find_element(By.ID, 'twotabsearchtextbox')
print(element)

#By XPath
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

#By XPath, any tag
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")

#By XPath, multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @spellcheck='false']")
driver.find_element(By.XPATH, "//input[@spellcheck='false' and @tabindex='0']")

#By XPath, text()
driver.find_element(By.XPATH, "//h2[@text='Designer gifts for Mom]']")

