
__author__ = 'AKV'

"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random
array = [[random.randint(0, 100) for i in range(6)] for j in range(5)]

j = 0
while j < len(array[0]):
    min_in_column = array[0][j]

    i = 1
    while i < len(array):
        if array[i][j] < min_in_column:
            min_in_column = array[i][j]
        i += 1

    if j == 0:
        max_in_min = min_in_column
    else:
        if max_in_min < min_in_column:
            max_in_min = min_in_column
    j += 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()
print(f"Максимальный элемент среди минимальных элементов столбцов таблицы равен {max_in_min}")