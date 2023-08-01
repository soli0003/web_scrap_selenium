from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

driver.get("https://www.realtor.ca/map#ZoomLevel=11&Center=43.708087%2C-79.376385&LatitudeMax=43.90407&LongitudeMax=-79.02551&LatitudeMin=43.51146&LongitudeMin=-79.72726&Sort=6-D&PGeoIds=g30_dpz89rm7&GeoName=Toronto%2C%20ON&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&Currency=CAD")

try:
  ads = driver.find_elements(By.CLASS_NAME, "smallListingCardImage")
  print(len(ads))
except NoSuchElementException:
  print("No ads found")

driver.quit()

def main():
  # code to execute

    if __name__ == "__main__":
        main()