import re

def check_variable(number):
    return bool(re.match('^[-+]{0,1}\d*\.{0,1}\d*$', number))

def get_number(prompt):
    number = input(prompt)
    while not check_variable(number):
        number = input(prompt)
    return float(number)


def check_amount(number):
    return bool(re.match('^\d*$', number))

def get_amount(prompt):
    number = input(prompt)
    while not check_amount(number):
        number = input(prompt)
    return int(number)