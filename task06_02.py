
__author__ = 'AKV'

"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 
3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
import sys

a = int(input("Введите натуральное число: "))

sum_even = 0
sum_odd = 0
tmp_a = a

while tmp_a != 0:
    if tmp_a % 10 % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1

    tmp_a = tmp_a // 10

print(f'В натуральном числе {a}:  {sum_even} четные(х) цифры и {sum_odd} нечетные(х)')



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