from ast import Assert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.wonga.pl/")

print(driver.title) 

assert driver.title == 'Pożyczki online - szybkie i na raty - lepsze niż chwilówki przez Internet | Wonga'
git init

driver.close()