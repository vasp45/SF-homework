#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_input(text, min=None, max=None):
    while True:
        tmp_in = input(text).split()
        if not all(n.lstrip('-').isnumeric() for n in tmp_in):
            print('Введенные значения должны быть числами.\n')
            continue
        if min and len(tmp_in) < min:
            print(f'Минимальное количество чисел, которое необходимо ввести: {min}.\n')
            continue
        if max and len(tmp_in) > max:
            print(f'Максимальное количество чисел, которое можно ввести: {max}.\n')
            continue
        return list(map(int, tmp_in))


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def binary_search(array, element, left, right):
    
    def not_unique_element(elem):
        # двигаемся влево если найденное число повторяется в последовательности
        if elem != -1 and array[elem] == array[elem + 1]:
            return not_unique_element(elem - 1)
        else:
            return elem
    
    if left > right:
        return left - 1
    middle = (right + left) // 2
    if len(array) == middle:
        return right
    if array[middle] == element:
        return not_unique_element(middle - 1)
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


array = my_input('Введите последовательность чисел через пробел: ', min=1)
number = my_input('Введите отдельное число: ', max=1)[0]

bubble_sort(array)
inx = binary_search(array, number, 0, len(array))

print(f'\nСортированная последовательность:\n{str(array)[1:-1]}\n')

if inx == -1:
    print('Условия не выполнены:\n' +
          'Введенное число меньше минимального числа в последовательности,\n' +
          'либо является минимальным.')
elif inx == len(array):
    print('Условия не выполнены:\n' +
          'Введенное число больше самого большого числа в последовательности.')
else:
    print(f'Индекс искомого элемента  : {inx}\n' +
          f'Значение искомого элемента: {array[inx]}')
