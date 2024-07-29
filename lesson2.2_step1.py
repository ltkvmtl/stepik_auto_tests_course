from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.XPATH, '//span[@id="num1"]')
    x = int(x1_element.text)
    y1_element = browser.find_element(By.XPATH, '//span[@id="num2"]')
    y = int(y1_element.text)
    summa = (x + y)
    s5 = str(summa)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()