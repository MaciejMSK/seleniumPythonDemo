




from ast import Assert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://commitquality.com/practice-iframe")

print(driver.title) 

assert driver.title == 'CommitQuality - Test Automation Demo'

driver.close()