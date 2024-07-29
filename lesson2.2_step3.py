from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@name="email"]')
    input3.send_keys("abc@abc.com")

    # Отправляем заполненную форму
    element = browser.find_element(By.XPATH, '//input[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '123.txt')
    element.send_keys(file_path)
    
    element2 = browser.find_element(By.CSS_SELECTOR, "button")
    element2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()