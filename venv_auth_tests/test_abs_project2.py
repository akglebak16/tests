import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def pizda(link):
    driver = webdriver.Chrome()
    driver.get(link)
    field1 = driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    field1.send_keys("fewfew")
    field2 = driver.find_element(By.CSS_SELECTOR, 'input.second:required')
    field2.send_keys("few3232few")
    field3 = driver.find_element(By.XPATH, '//*[@class="form-control third"]')
    field3.send_keys("fewfe&^%w")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    time.sleep(2)
    driver.quit()
    return welcome_text


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("Congratulations! You have successfully registered!",
                         pizda("http://suninjuly.github.io/registration1.html"),
                         "Registration Failed")


    def test_2(self):
        welcome_text = pizda("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!",
                         pizda("http://suninjuly.github.io/registration1.html"),
                         "Registration Failed")


if __name__ == "__main__":
    unittest.main()

# class TestAll(unittest.TestCase):
#     def test_first_link(self):
#         self.assertEquals(test(link1), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')
#
#     def test_first_link2(self):
#         self.assertEquals(test(link2), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')
#
# if __name__ == "__main__":
#         unittest.main()

# from selenium import webdriver
# import time
# import unittest
# from selenium.webdriver.common.by import By
#
# link1 = "http://suninjuly.github.io/registration1.html"
# link2 = "http://suninjuly.github.io/registration2.html"
#
# def reg(link):
#
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
#     input3.send_keys("test@test.ru")
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR,"button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     return browser.find_element(By.TAG_NAME,"h1").text
#
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#
# class TestAll(unittest.TestCase):
#     def test_first_link(self):
#         self.assertEquals(reg(link1), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')
#
#     def test_first_link2(self):
#         self.assertEquals(reg(link2), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')
#
# if __name__ == "__main__":
#         unittest.main()