from selenium import webdriver 
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("https://book24.ru/product/blagoslovenie-nebozhiteley-tom-1-6065707/")
    # добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "button.b24-btn._large._block").click()
    browser.get("https://book24.ru/product/tagar-tom-1-6109356/")
    # добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "button.b24-btn._large._block").click()
    # открываем страницу второго товара
    # открываем корзину
 #   browser.find_element(By.CSS_SELECTOR, "a.header-cart.header__cart.smartLink").click()
    browser.get("https://book24.ru/personal/cart/")
    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, "div.basket-list-desktop__item")
    print (goods)
    # проверяем, что количество товаров равно 2
   # assert len(goods) == 2

finally: 
    browser.get("https://book24.ru/product/blagoslovenie-nebozhiteley-tom-1-6065707/")
