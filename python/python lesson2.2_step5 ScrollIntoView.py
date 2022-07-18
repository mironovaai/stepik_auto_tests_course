import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()
link = ("http://SunInJuly.github.io/execute_script.html")

try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    y = math.log(abs(12*math.sin(x)))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    robotCheckbox.click()

    robotRadiobutton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    robotRadiobutton.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
