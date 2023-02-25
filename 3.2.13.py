from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def test(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block>.first_class>.first")
    input4.send_keys("555-12345678")
    input5 = browser.find_element(By.CSS_SELECTOR,".second_block>.second_class>.second")
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    return welcome_text


class TestAbs(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    def test1(self):
#        self.assertEqual(test(link1), "Congratulations! You have successfully registered!")
        self.assertEqual(test("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!")
        
    def test2(self):
#        self.assertEqual(test(link2), "Congratulations! You have successfully registered!")
        self.assertEqual(test("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!")
        
if __name__ == "__main__":
    unittest.main()


