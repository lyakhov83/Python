# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint

quanNum = int(input("Введите количество элементов массива: "))
lst = [randint(0, 10) for i in range(0, quanNum)]
print("Список случайных чисел:", lst)

num = lst[0]
frqRep = 1
for i in range(quanNum - 1):
    numRep = 1
    for j in range(i + 1, quanNum):
        if lst[i] == lst[j]:
            numRep += 1
    if numRep > frqRep:
        frqRep = numRep
        num = lst[i]
if frqRep > 1:
    print("{} раз(а) встреается число {}". format(frqRep, num))
else:
    pass


