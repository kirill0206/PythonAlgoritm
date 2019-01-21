
__author__ = "AKV"

"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала 
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль 
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего 
и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import defaultdict
SIZE = 4    # количество учитываемых кварталов
registration = defaultdict(list)   # тип коллекции для ввода данных о предприятиях


def input_company(n):
    for i in range(n):
        reg_name = input(f'Введите название {i + 1} предприятия: ')
        for j in range(SIZE):
            registration[reg_name].append(int(input(f'Введите прибыль {reg_name} в {j + 1} квартале: ')))


def average_rescue(reg):
    rescue = 0
    for k, v in reg.items():
        for i in range(SIZE):
            rescue += v[i]
    return rescue / value


def print_max():
    print("=" * 80)
    print("Предприятия с прибылью ваше средней:")
    print("=" * 80)

    average = average_rescue(registration)

    for k, v in registration.items():
        rescue = 0
        for i in range(SIZE):
            rescue += v[i]
        if average < rescue:
            print(k)

    print("=" * 80)


def print_min():
    print("=" * 80)
    print("Предприятия с прибылью ниже средней:")
    print("=" * 80)

    average = average_rescue(registration)

    for k, v in registration.items():
        rescue = 0
        for i in range(SIZE):
            rescue += v[i]
        if average > rescue:
            print(k)

    print("=" * 80)


value = int(input("Введите количество предприятий: "))
input_company(value)
print_max()
print_min()

