from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element(By.ID, 'book').click()
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x_element)
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(4)
    confirm = driver.switch_to.alert
    confirm.accept()

finally:
    time.sleep(5)
    driver.close()
    driver.quit()