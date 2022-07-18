from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
    for element in elements:
        element.send_keys("Мой ответ")
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
