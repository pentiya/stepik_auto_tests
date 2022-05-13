'''
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

'''
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser=webdriver.Chrome()
    browser.get(link)
    button=browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split()
    answer = alert_text[-1]
    alert.accept()
    print(answer)

finally:
    time.sleep(10)
    browser.quit()




