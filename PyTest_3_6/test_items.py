from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_button_exists(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "No cart button"
