from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    sum = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum))
    
    btn = browser.find_element(By.CLASS_NAME, 'btn')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()