import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://github.com/login")
    time.sleep(5)
    
    usrF = driver.find_element(by=By.NAME, value="login")
    usrF.send_keys("aaa")
    time.sleep(5)
    pasF = driver.find_element(by=By.NAME, value="password")
    pasF.send_keys("123")
    time.sleep(5)


    # pwd = driver.find_element(by=By.NAME, value="pwd")
    # pwd.send_keys("123")
    # driver.implicitly_wait(2.5)
    # submit_button = driver.find_element(by=By.NAME, value="Submit")

    # driver.implicitly_wait(2.5)
    # submit_button.click()
    # driver.implicitly_wait(2.5)
    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"
    # print(message.text)
    # driver.quit()


test_eight_components()