import re
print("=============================================")
print("Лабораторна робота №1")
print("Програмування лінійних алгоритмів")
print("Автор: Романов Микола, КМ-91 (18 варіант)")
print("=============================================")
print("Знайти суму членів арифметичної прогресії, якщо відомі її перший член,")
print("знаменник і число членів прогресії.")
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
    a1 = get_number('Введіть перший член арифметичної прогресії - ')
    d = get_number('Введіть значення знаменника - ')
    n = get_amount('Введіть кількість членів прогресії - ')
    if n == 0:
        print("Введіть додатню кількість членів прогресії")
        n = get_amount('Введіть кількість членів прогресії - ')
    an = a1 + d * (n - 1)
    S = ((a1 + an) / 2) * n
    return S

print("Сума членів арифметичної прогресії дорівнює - ", diviser())
print("=============================================")

