import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link="https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:

    browser.get(link)
    but = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    but.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x=browser.find_element(By.ID,"input_value")
    x=calc(x.text)

    input=browser.find_element(By.ID,"answer")
    input.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()