from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()

try:
    driver.get("https://suninjuly.github.io/file_input.html")
    fields = driver.find_elements(By.XPATH, '//input[@type="text"]')
    for element in fields:
        element.send_keys("popopo228")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    print(os.path.abspath(os.path.dirname(__file__)))
    driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(file_path)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()


finally:
    time.sleep(5)
    driver.close()
    driver.quit()
