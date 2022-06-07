from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration1.html"
    driver.get(link)

    #Ваш код, который заполняет обязательные поля
    field1 = driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    field1.send_keys("fewfew")
    field2 = driver.find_element(By.CSS_SELECTOR, 'input.second:required')
    field2.send_keys("few3232few")
    field3 = driver.find_element(By.XPATH, '//*[@class="form-control third"]')
    field3.send_keys("fewfe&^%w")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
