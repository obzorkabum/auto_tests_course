import selenium.common.exceptions as selex
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()
link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"
#комментарии
'''
Это могло быть решением, но тогда мы нарушаем пункт 3 - "уникальность селекторов" (неповторимость,
как твой идентификационный номер в паспорте)

def onlyrequired(br):
    elements = br.find_elements(By.CSS_SELECTOR, "[required]")
    for element in elements:
        element.send_keys("gl go next")
'''
#комментарии

def filluniqueinputs(br):
    # Ошибка вылетит строчкой ниже, т.к. данного плейсхолдера попросту не существует на форме 2
    input1 = br.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys(fake.first_name())
    input2 = br.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys(fake.last_name())
    input3 = br.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys(fake.email())

try:

    browser = webdriver.Chrome()
    browser.get(link1)
    # Ваш код, который заполняет обязательные поля
    #здесь и будет ошибка во второй форме, смотри функцию выше ↑
    filluniqueinputs(browser)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #можешь раскомментить строчку ниже, чтобы глянуть данные, если интересно
    # time.sleep(5)
    button.click()
    # ждем загрузки страницы
    time.sleep(3)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!"==welcome_text

#благодаря обработчику ошибок программа закроется со статусом 0, теперь можно посмотреть ошибку и личный комментарий)
except selex.NoSuchElementException as ex:
    print(ex)
    print("Такого элемента нет 🤡")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()