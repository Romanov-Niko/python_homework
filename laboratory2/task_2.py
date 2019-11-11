import sys
import math
import re
print("=============================================")
print("Лабораторна робота №2")
print("Програмування циклічних алгоритмів")
print("Автор: Романов Микола, КМ-91 (18 варіант)")
print("=============================================")
print("Дано ціле число N(>1). Знайти найменше ціле число K, при якому")
print("виконується нерівність 3K>N")
print("=============================================")

def check_number(text):
    return bool(re.match('^\d*$', text))

def get_number(prompt):

    number = input(prompt)
    while not check_number(number):
        number = input(prompt)
    return int(number)

def diviser():
    n = get_number("Введіть ціле число (N), яке більше одиниці - ")
    while n <= 1:
        n = get_number("Введіть ціле число (N), яке більше одиниці - ")
    if n % 3 != 0:
        K = math.ceil(n/3)
    else:
        K = n/3+1
    return K

print("Найменше ціле число К, при якому виконується нерівність - ", diviser())
print("=============================================")