from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    driver.find_element(By.CLASS_NAME, 'trollface').click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
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
