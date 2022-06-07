from selenium import webdriver
import time
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(1)
    driver.close()
    driver.quit()


