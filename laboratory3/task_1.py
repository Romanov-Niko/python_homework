import sys
print("=============================================")
print("ЛАБОРАТОРНА РОБОТА №3")
print("РЯДКИ")
print("АВТОР: РОМАНОВ МИКОЛА, КМ-91 (18 ВАРІАНТ)")
print("=============================================")
print("Перевірити у математичному вираженні, заданому рядком, відповідність")
print("відкриваючих і закриваючих дужок.")
print("=============================================")

def get_row(promt):
    text = input(promt)
    if text == "":
        print("В виразі відсутні дужки")
        sys.exit()
    return text

def count():
    start_bracket = 0
    end_bracket = 0
    read = get_row("Введіть вираз: ")
    for letter in read:
        if letter == '(':
            start_bracket = start_bracket + 1
    for letter in read:
        if letter == ')':
            end_bracket = end_bracket + 1
    return start_bracket, end_bracket

def compare():
    start, end = count()
    if start == 0 & end == 0:
        result = "В виразі відсутні дужки"
    elif start > end:
        result = "В виразі не вистачає закриваючих дужок"
    elif start < end:
        result = "В виразі зайві закриваючі дужки"
    elif start == end:
        result = "В виразі однакова кількість дужок"
    return result

print(compare())


