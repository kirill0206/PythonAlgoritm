
__author__ = 'AKV'

"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму 
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

ROWS = 4
COLUMNS = 5
num_array = [[[0] * COLUMNS] * ROWS]

for i in range(ROWS):
    sum_row = 0
    for j in range(COLUMNS - 1):
        number = int(input("введите элемент матрицы: "))
        num_array[i][j] = number
        sum_row += number
    num_array[i][4] = sum_row

for rows in num_array:
    for number in rows:
        print(f"{number:4}", sep='')
    print()
