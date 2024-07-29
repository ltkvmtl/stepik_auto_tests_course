from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(z):
  return str(math.log(abs(12*math.sin(int(z)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option = browser.find_element(By.XPATH, '//button')
    option.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    z2_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    z_element = z2_element.text
    z = z_element
    y = calc(z)
    input1 = browser.find_element(By.XPATH, '//input')
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()