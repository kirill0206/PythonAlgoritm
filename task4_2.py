
__author__ = 'AKV'

'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
'''

def simple(n):
    _list = [2, 3, 5]
    i = _list[len(_list) - 1]

    while n > len(_list):
        i += 1

        if i % 2 == 0 or i % 10 == 5:
            continue

        for num in _list:
            if num * num > i:
                _list.append(i)
                break
            if i % num == 0:
                break

    return _list.pop()


'''
100 loops, best of 5: 13.8 usec per loop - 5
100 loops, best of 5: 43.1 usec per loop - 10
100 loops, best of 5: 457 usec per loop - 50
100 loops, best of 5: 1.21 msec per loop - 100
'''


def simple_eratosfen(n):

    sieve = [i for i in range(n**2)]
    sieve[1] = 0

    for i in range(2, n**2):
        if sieve[i] != 0:
            j = i + i
            while j < n**2:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]

    return result[n-1]

'''
100 loops, best of 5: 97.9 usec per loop - 5
100 loops, best of 5: 456 usec per loop - 10
100 loops, best of 5: 15.1 msec per loop - 50
100 loops, best of 5: 65.7 msec per loop - 100
'''
