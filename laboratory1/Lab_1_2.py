import re
print("=============================================")
print("Лабораторна робота №1")
print("Програмування лінійних алгоритмів")
print("Автор: Романов Микола, КМ-91 (18 варіант)")
print("=============================================")
print("Визначити, введений символ є буквою чи цифрою")
print("=============================================")

def check_alone(text):
    return bool(re.match('^\[0-9]|\w$', text))

def get_alone(prompt):
    number = input(prompt)
    while not check_alone(number):
        number = input(prompt)
    return number

def diviser():
    user_input = get_alone('Введіть один символ - ')
    if user_input.isdigit():
        print("Введений символ є цифрою")
    else:
        print("Введений символ є літерою")
    return user_input

print(diviser())
print("=============================================")

