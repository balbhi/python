
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
time.sleep(3)
search_box=driver.find_element(By.ID,'small-searchhterms')
search_driver.send_keys('hi')
driver.find_element(By.XPATH,"////*[@id=small-searchterms]").click()


import time
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


dirver=webdriver.Chrome()
dirver.get('https://www.google.com/')
dirver.maximize_window()
time.sleep(5)
dirver.close()