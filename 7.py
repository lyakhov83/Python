"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

quanNum = int(input("Введите количество элементов массива: "))
lst = [randint(0, 100) for i in range(0, quanNum)]
print("{} - Список случайных чисел.". format(lst))

"""
var = sorted(lst)
print("{} - Список по возрастанию.". format(var))
print("{} - Два минимальных элемента списка.". format(var[0:2]))
"""

if lst[0] > lst[1]:
    firMinEl = 0
    secMinEl = 1
else:
    firMinEl = 1
    secMinEl = 0

for i in range(2,quanNum):
    if lst[i] < lst[firMinEl]:
        var = firMinEl
        firMinEl = i
        if lst[var] < lst[secMinEl]:
            secMinEl = var
    elif lst[i] < lst[secMinEl]:
        secMinEl = i

print("{} - Первый Min элемент списка.\n{} - Второй Min элемент списка.". format(lst[firMinEl], lst[secMinEl]))



