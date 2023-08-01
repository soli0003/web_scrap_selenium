from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:4200/")

wait = WebDriverWait(driver, 10)

divs = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))

for div in divs:
  print(div.text) 
  print(div.get_attribute('innerHTML'))


driver.quit()