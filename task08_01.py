
__author__ = 'AKV'

"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""

_str = input('Введите строку: ')

hash_list = []
for i in range(len(_str) - 1):

    for j in range(1, len(_str) - i):
        init_str = hash(_str[i:(i+j)])
        print(init_str)
        if init_str not in hash_list:
            hash_list.append(init_str)

print(f'Число подстрок равно {len(hash_list)}')

