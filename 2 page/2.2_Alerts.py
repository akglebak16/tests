from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get("http://suninjuly.github.io/alert_accept.html")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x_element)
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()




finally:
    time.sleep(5)
    driver.close()
    driver.quit()
