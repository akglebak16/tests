import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, "something went wrong")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, "something went wrong")
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
