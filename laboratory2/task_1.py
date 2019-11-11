import sys
import re
print("=============================================")
print("Лабораторна робота №2")
print("Програмування циклічних алгоритмів")
print("Автор: Романов Микола, КМ-91 (18 варіант)")
print("=============================================")
print("Обчислити добуток множників (x/(2^i)) від 0 до N")
print("=============================================")

def check_variable(text):
    return bool(re.match('^[-+]{0,1}\d*\.{0,1}\d*$', text))

def get_number(prompt):

    number = input(prompt)
    while not check_variable(number):
        number = input(prompt)
    return float(number)

def check_amount(text):
    return bool(re.match('^\d*$', text))

def get_amount(prompt):

    number = input(prompt)
    while not check_amount(number):
        number = input(prompt)
    return int(number)

def diviser():
    x = get_number("Введіть (x) - ")
    n = get_amount("Введіть (n) - ")
    if n <= 0:
        print("Введіть додатній N")
        n = get_number("Введіть (n) - ")
    P = 1
    for i in range(0, n + 1):
        R = (x / pow(2, i))
        P = P * R
    return round(P, 3)

print("Добуток множників дорівнює  - ", diviser())
print("=============================================")

