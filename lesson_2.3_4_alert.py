from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    x_ans = math.log(abs(12*math.sin(int(x))))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x_ans)

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()