
__author__ = 'AKV'

"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых 
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

count = int(input("Сколько чисел будет введено? "))
find_cipfer = int(input("Количество каких необходимо поределить? "))
count_cipher = 0

for i in range(count):
    number = int(input(f"Введите {i + 1} число: "))

    while number > 0:
        if find_cipfer == number % 10:
            count_cipher += 1
        number = number // 10

print(f"В введеной последовательности чисел цифра {find_cipfer} встретилась {count_cipher} раз(а).")
