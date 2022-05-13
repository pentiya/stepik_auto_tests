'''
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

'''
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser=webdriver.Chrome()
    browser.get(link)
    button=browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    button.click()

    current_window = browser.current_window_handle
    print("current_window", current_window)
    new_window = browser.window_handles[1]                      
    browser.switch_to.window(new_window)


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




