import pytest
import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", 
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_math(link):
    browser = webdriver.Chrome()
    browser.get(link)
    textarea = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    answer = str(math.log(int(time.time())))
    textarea.click()
    textarea.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    result = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints.ember-view.lesson__hint").text
    assert result == "Correct!"
    f"Answer '{result}' is incorrect"







