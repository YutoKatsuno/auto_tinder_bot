from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
DRIVER_PATH = os.environ["DRIVER_PATH"]
URL = os.environ["URL"]

# Initialize selenium
chrome_service = service.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)


time.sleep(3)
login_button = driver.find_element(By.CSS_SELECTOR, "div.Mx\(28px\).Mx\(8px\)--m a")
login_button.click()

time.sleep(3)
google_login = driver.find_element(By.CSS_SELECTOR, "div.My\(10px\) button")
google_login.click()
time.sleep(5)
google_mail = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
google_mail.send_keys(EMAIL)
