import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create the driver instance
driver = webdriver.Chrome() 

# Now the driver is ready to use
button = driver.find_element(By.NAME, "Home")
try:
  button = driver.find_element(By.NAME, "Home") 
except NoSuchElementException:
  print("Element not found, retrying")
  time.sleep(5)
  button = driver.find_element(By.NAME, "Home")

if button is None:
  print("Element still not found after retry")
else: 
  button.click()