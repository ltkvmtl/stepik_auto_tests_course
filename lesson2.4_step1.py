from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(z):
  return str(math.log(abs(12*math.sin(int(z)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element(By.ID, "book")
button.click()

button2 = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

z2_element = browser.find_element(By.ID, "input_value")
z_element = z2_element.text
z = z_element
y = calc(z)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button2.click()
time.sleep(10)