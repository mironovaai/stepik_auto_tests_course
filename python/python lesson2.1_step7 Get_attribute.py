import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/get_attribute.html")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, "img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    robotCheckbox.click()

    robotRadiobutton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    robotRadiobutton.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
    