'''
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. 
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. 
Ваш код и для нее тоже ﻿должен пройти успешно.

Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", 
перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку! 

'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1").text
    print("num1=", num1)
    num2 = browser.find_element_by_css_selector("#num2").text
    print("num2=", num2)
    num = int(num1) + int(num2)
    print("num=",num,"str_num",str(num))

    select = Select(browser.find_element_by_tag_name("#dropdown"))

#    select.select_by_value(str(num))
    select.select_by_visible_text(str(num))

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

