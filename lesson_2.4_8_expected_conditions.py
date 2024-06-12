import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
book = browser.find_element(By.CLASS_NAME, 'btn')
book.click()

x = browser.find_element(By.ID, 'input_value').text
x_ans = math.log(abs(12*math.sin(int(x))))

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(x_ans)

submit = browser.find_element(By.ID, 'solve')
submit.click()

time.sleep(10)
browser.quit()
