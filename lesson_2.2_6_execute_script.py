from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import log, sin

link = 'https://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text

    res = log(abs(12*sin(int(x))))

    btn = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    # browser.execute_script("window.scrollBy(0, 100);")
    btn.click()
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)
    
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    
    robotrule = browser.find_element(By.ID, 'robotsRule')
    robotrule.click()

    btn.click()

finally:
    time.sleep(10)
    browser.quit()