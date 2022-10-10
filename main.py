from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

# STEP1 Click on login button
time.sleep(5)
login_button = driver.find_element(By.CSS_SELECTOR, "div.Mx\(28px\).Mx\(8px\)--m a")
login_button.click()

# STEP2　Choose to log in with Facebook
time.sleep(5)
fb = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb.click()

# STEP3 Change the window
base_window = driver.window_handles[0]
google_window = driver.window_handles[1]
driver.switch_to.window(google_window)

# STEP4 Login to facebook
time.sleep(3)
mail = driver.find_element(By.NAME, "email")
mail.send_keys(EMAIL)
password = driver.find_element(By.NAME, "pass")
password.send_keys(PASSWORD)
fb_login = driver.find_element(By.NAME, "login")
fb_login.click()

# STEP5 Change the window
time.sleep(3)
driver.switch_to.window(base_window)

# STEP6 Turn off redundant notifications
time.sleep(3)
location = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div/div/div[3]/button[1]')
location.click()
time.sleep(3)
notice = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div/div/div[3]/button[1]')
notice.click()
time.sleep(3)
cookie = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie.click()

# STEP7 n times not like
time.sleep(5)
for _ in range(10):
    try:
        not_like = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[2]/button')
        not_like.click()
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
