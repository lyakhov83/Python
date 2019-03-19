#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import randint

quanNum = int(input("Введите количество элементов массива: "))
lst = [randint(0, 100) for i in range(0, quanNum)]
print("Список случайных чисел:", lst)

inMinEl = lst.index(min(lst))
inMaxEl = lst.index(max(lst))
lst[inMinEl], lst[inMaxEl] = lst[inMaxEl], lst[inMinEl]

print("{} - индекс минимального значения списка\n{} - индекс максимального значения списка". format(inMinEl, inMaxEl))
print("Новый список, в котором поменяли местами индексы Min и Max значения:", lst)


