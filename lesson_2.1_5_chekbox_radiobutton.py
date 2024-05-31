import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox.click()

    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()

    btn = browser.find_element(By.CLASS_NAME, 'btn')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()