from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

browser = webdriver.Chrome()

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        element = browser.find_element(By.CSS_SELECTOR, "div.first_block  input.first")
        element.send_keys("Мой ответ")
        element = browser.find_element(By.CSS_SELECTOR, "div.first_block  input.second")
        element.send_keys("Мой ответ")
        element = browser.find_element(By.CSS_SELECTOR, "div.first_block  input.third")
        element.send_keys("Мой ответ") 
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed!")
        
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        element = browser.find_element(By.CSS_SELECTOR, "div.first_block  input.first")
        element.send_keys("Мой ответ")
        element = browser.find_element(By.CSS_SELECTOR, "div.first_block  input.second")
        element.send_keys("Мой ответ")
        element = browser.find_element(By.CSS_SELECTOR, "div.first_block  input.third")
        element.send_keys("Мой ответ")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed!")
        
if __name__ == "__main__": unittest.main()

time.sleep(10)
browser.quit()
