
__author__ = 'AKV'

"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


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
