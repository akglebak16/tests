from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
def calc(x_element):
  return str(math.log(abs(12*math.sin(int(x_element)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    driver.get(link)
    x_element = driver.find_element(By.ID, 'input_value').text
    y = calc(x_element)
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.ID, 'robotCheckbox').click()
    robot = driver.find_element(By.ID, 'robotsRule')
    driver.execute_script("return arguments[0].scrollIntoView(true);", robot)
    #скролит до нужного элемента
    robot.click()
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    driver.close()
    driver.quit()