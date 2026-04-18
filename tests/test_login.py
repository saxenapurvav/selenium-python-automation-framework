from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
print(driver.current_url)   # debug

time.sleep(5)   # IMPORTANT (increase wait)

# Login steps
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type= 'submit']").click()
print(driver.title)

message = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in message

# Logout (IMPORTANT PART)
logout_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius"))
)
logout_button.click()

# Validation (after logout)
message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))
).text

assert "You logged into a secure area!" in message
print("Login Test Passed")
print("Logout message:", message)

driver.quit()
