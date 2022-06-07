#Допустим, на странице https://www.degreesymbol.net/ мы хотим найти ссылку с текстом "Degree symbol in Math" и перейти по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код:

#link = browser.find_element_by_link_text("Degree Symbol in Math")
#link.click()
#А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:

#link = browser.find_element_by_partial_link_text("Math")
#link.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_link_text")

# linke = str(math.ceil(math.pow(math.pi, math.e)*10000))
# print(int(linke))
link = driver.find_element(By.LINK_TEXT, '224592')
link.click()

in1 = driver.find_element(By.NAME, 'first_name')
in1.send_keys("fewf")
in2 = driver.find_element(By.NAME, 'last_name')
in2.send_keys("fewsss")
in3 = driver.find_element(By.NAME, 'firstname')
in3.send_keys("fewfe")
in4 = driver.find_element(By.ID, 'country')
in4.send_keys("fewffew")
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
