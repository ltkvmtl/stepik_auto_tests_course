from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(z):
  return str(math.log(abs(12*math.sin(int(z)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    z2_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    z_element = z2_element.text
    z = z_element
    y = calc(z)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)
    option2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
    option3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()