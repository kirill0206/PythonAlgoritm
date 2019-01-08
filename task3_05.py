
__author__ = 'AKV'

"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random
# Generate random array
rand_array = [random.randint(-50, 51) for i in range(100)]

position_min = -1
i = 0
# search first negative number
while i < len(rand_array):
    if rand_array[i] < 0:
        position_min = i
        break
    i += 1
if position_min == -1:
    print(f"В массиве нет отрицателных элементов")
    exit(0)

# search maximum from negative numbers in array
while i < len(rand_array):
    if rand_array[i] < 0:
        if rand_array[i] > rand_array[position_min]:
            position_min = i
    i += 1

print(f"В массиве найдено максимальное отрицательное число {rand_array[position_min]} под индексом {position_min}")
