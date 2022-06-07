import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   link = "http://suninjuly.github.io/math.html"
   driver.get(link)
   x_element = driver.find_element(By.CSS_SELECTOR, '#input_value').text
   y = calc(x_element)
   driver.find_element(By.ID, 'answer').send_keys(y)
   driver.find_element(By.ID, 'robotCheckbox').click()
   driver.find_element(By.ID, 'robotsRule').click()
   driver.find_element(By.XPATH, '//*[@type="submit"]').click()

finally:
    time.sleep(5)
    driver.close()
    driver.quit()