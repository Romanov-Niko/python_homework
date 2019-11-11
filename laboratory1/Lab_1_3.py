from math import sin
import re
print("=============================================")
print("Лабораторна робота №1")
print("Програмування лінійних алгоритмів")
print("Автор: Романов Микола, КМ-91 (18 варіант)")
print("=============================================")
print("Обчислити функцію")
print("=============================================")

def check_variable(text):
    return bool(re.match('^[-+]{0,1}\d*\.{0,1}\d*$', text))

def get_number(prompt):

    number = input(prompt)
    while not check_variable(number):
        number = input(prompt)
    return float(number)

def diviser():
    x = get_number("Введіть значення X - ")
    if x <= 3:
        y = float(pow(x, 2)+3*x+9)
    else:
        y = float((sin(x))/(pow(x, 2)-9))
    return round(y,3)

print("Значення функції дорівнює - ", diviser())
print("=============================================")
