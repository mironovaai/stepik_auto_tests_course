from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

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

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
