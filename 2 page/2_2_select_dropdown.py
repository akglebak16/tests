from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")

try:
    x = driver.find_element(By.ID, 'num1').text
    y = driver.find_element(By.ID, 'num2').text
    z = int(x) + int(y)
    print(z)
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(z))
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    driver.close()
    driver.quit()
