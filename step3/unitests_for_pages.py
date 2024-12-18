import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()
link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"


def initialize_browser(link):
    browser = webdriver.Chrome()
    browser.get(link)
    return browser

def filluniqueinputs(br):
    input1 = br.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys(fake.first_name())
    input2 = br.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys(fake.last_name())
    input3 = br.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys(fake.email())

def click_submit(browser):
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

def get_welcome_text(browser):
    time.sleep(3)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    return welcome_text_elt.text

def close_browser(browser):
    time.sleep(3)
    browser.quit()

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        browser = initialize_browser(link1)
        filluniqueinputs(browser)
        click_submit(browser)
        text = get_welcome_text(browser)
        self.assertEqual(text, "Congratulations! You have successfully registered!", "Конечный результат не получен")

    def test_registration2(self):
        browser = initialize_browser(link2)
        filluniqueinputs(browser)
        click_submit(browser)
        text = get_welcome_text(browser)
        self.assertEqual(text, "Congratulations! You have successfully registered!", "Конечный результат не получен")

if __name__ == "__main__":
    unittest.main()