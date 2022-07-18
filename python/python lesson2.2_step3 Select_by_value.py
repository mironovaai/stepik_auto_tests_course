import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/selects1.html")

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text 
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    result = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))  

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
    