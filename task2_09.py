
__author__ = 'AKV'

"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
"""
max_num = 0
max_num_sum = 0

while True:
    number = int(input("Введите натуральное число или '0' для окончания работы программы:"))

    if number != 0:
        number_sum = 0
        tmp = number

        while tmp > 0:
            number_sum += tmp % 10
            tmp = tmp // 10
        if max_num_sum < number_sum:
            max_num_sum = number_sum
            max_num = number

    else:
        if max_num_sum != 0:
            print(f"Число {max_num} имеет наибольшую сумму цифр {max_num_sum}")
        else:
            print("Выход из программы")
        break
