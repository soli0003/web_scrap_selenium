import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def yad2():
    driver = webdriver.Chrome()

    driver.get("https://myplace.co.il/en/apartments-for-rent/")

    # title = driver.title
    # assert title == "Web form"

    driver.implicitly_wait(2.5)
    time.sleep(6)
    ads_section = driver.find_element(by=By.CLASS_NAME, value="pr_li")
    # add = driver.find_element(by=By.CLASS_NAME, value="pic")
    ad= ads_section.find_element(by=By.CLASS_NAME, value="pr_main")
    ad1= ad.find_element(by=By.CLASS_NAME, value="pr_link")
    ad1.click()
    time.sleep(1)
    adcitymain= ad1.find_element(by=By.CLASS_NAME, value="projects_properties_info")
    adcitytable= adcitymain.find_element(by=By.TAG_NAME, value="table")
    time.sleep(4)
    print(adcitytable.text)
    
    
yad2()