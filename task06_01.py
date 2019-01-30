
__author__ = 'AKV'

"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
import sys

# Вариант красивый
a = int(input("Введите трехзначное число: a = "))

num = []
summa = 0
multi = 1

for i in range(3):
    num.append((a // (10 ** i)) % 10)

for i in range(3):
    summa += num[i]
    multi *= num[i]

print(f"Сумма цифр числа а равно {summa}")
print(f"Произведение цифр числа а равно {multi}")

# Вариант быстрый


a = input("Введите трехзначное число: a = ")
summa = 0
multi = 1

for i in range(3):
    num = int(a[i])
    summa += num
    multi *= num

print(f"Сумма цифр числа а равно {summa}")
print(f"Произведение цифр числа а равно {multi}")


def get_size(x):

    size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += get_size(key)
                size += get_size(value)
        elif not isinstance(x, str):
            for item in x:
                size += get_size(item)

    return size


print(f'size = {get_size(locals())}')

'''
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
'''