from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("http://suninjuly.github.io/find_xpath_form")
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

finally:
    time.sleep(5)
    driver.close()
    driver.quit()
