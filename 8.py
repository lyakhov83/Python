"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from random import randint

numInCol = 5
numInStr = 4

lst = [0] * 5
for i in range(numInStr):
    lst2 = [0] * 4
    for j in range(numInCol - 1):
        lst2= ([randint(0, 1000) for j in range(0, numInCol)])
        print("{:4d}". format(lst2[j]), end=" ")
    lst.append(lst2)
    print(" = ", sum(lst2))


