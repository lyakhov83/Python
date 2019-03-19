"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

quanNum = int(input("Введите количество элементов массива: "))
lst = [randint(0, 100) for i in range(0, quanNum)]
print("{} - Список случайных чисел.". format(lst))

inMinEl, inMaxEl = lst.index(min(lst)), lst.index(max(lst))
addLst = sorted((inMinEl, inMaxEl))

print("{} - Индекс минимального элемента.\n{} - Индекс максимального элемента.". format(inMinEl, inMaxEl))
print("{} - Сортированный список индексов элементов.". format(addLst))
print("{} - Сумма элементов между индексами сортированного списка.". format(sum(lst[addLst[0] + 1:addLst[1]])))
