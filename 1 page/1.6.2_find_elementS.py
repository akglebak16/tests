from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера

try:
    driver.get("https://liquider.eu/9-e-papierosy")
    driver.find_element(By.XPATH, '//*[@id="category"]/div[2]/div/button/span[2]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div/div[1]/article[1]/div/div[1]/div[4]/a/img').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@class="btn btn-primary add-to-cart"]').click()
    print("первый товар добавлен")

    driver.get("https://liquider.eu/9-e-papierosy")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div/div[1]/article[11]/div/div[1]/div[1]/h3/a').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@class="btn btn-primary add-to-cart"]').click()
    print("второй товар добавлен")

    driver.get("https://liquider.eu/9-e-papierosy")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div/div[1]/article[4]/div/div[1]/div[1]/h3/a').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@class="btn btn-primary add-to-cart"]').click()
    print("третий товар добавлен")

    driver.get("https://liquider.eu/9-e-papierosy")
    driver.find_element(By.XPATH, '//*[@id="_desktop_cart"]/div/div/div[1]/a/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="_desktop_cart"]/div/div/div[2]/div/div[2]/div[5]/a').click()
    goods = driver.find_elements(By.XPATH, '//div[@class="product-title"]')
    print("Товаров в корзине:", len(goods))
    assert len(goods) == 3


finally:
    time.sleep(1)
    driver.close()
    driver.quit()

