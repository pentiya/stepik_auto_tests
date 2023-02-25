'''
Задание: составные сообщения об ошибках
Для закрепления материала реализуйте проверку самостоятельно. 

Вам дана функция test_input_text,  которая принимает два значения: 
expected_result — ожидаемый результат, и 
actual_result — фактический результат. 
Обратите внимание, input использовать не нужно!

Функция должна проверить совпадение значений с помощью оператора assert и, 
в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 

Важно! Формат ошибки должен точно совпадать с приведенным в примере, 
чтобы его засчитала проверяющая система! 

Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" 
и протестируйте ваш код на разных введенных значениях, 
проверьте вывод вашей функции на разных парах. 
Обрабатывать ситуацию с пустым или невалидным вводом не нужно. 

Sample Input 1:

8 11
Sample Output 1:

expected 8, got 11
Sample Input 2:

11 11
Sample Output 2:

Sample Input 3:

11 15
Sample Output 3:

expected 11, got 15
'''


def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert   expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

test_input_text(8,11)
test_input_text(11,11)
test_input_text(11,15)
