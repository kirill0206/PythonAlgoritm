
__author__ = "AKV"

"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число 
представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque, defaultdict

hex_int = defaultdict(int)
for i, k in enumerate('0123456789ABCDEF'):
    hex_int[k] = i


def hex_to_int(hex_num):
    _int = 0
    _len = len(hex_num)

    for i, k in enumerate(hex_num):
        _int += 16 ** (_len - i - 1) * hex_int[k]

    return _int


def int_to_hex(int_num):
    _hex = deque()
    while int_num > 0:
        letter = int_num % 16
        for i, k in enumerate(hex_int):
            if letter == i:
                _hex.appendleft(k)
                break

        int_num = int_num // 16

    return _hex


num_1_hex = deque(input('Введите первое шестнадцетиричное число: ').upper())
num_2_hex = deque(input('Введите второе шестнадцетиричное число: ').upper())

num_1 = hex_to_int(num_1_hex)
num_2 = hex_to_int(num_2_hex)

print(num_1, num_2)
print(f'Сумма двух чисел равна {int_to_hex(num_1 + num_2)}')
print(f'Произведение двух чисел равно {int_to_hex(num_1 * num_2)}')
