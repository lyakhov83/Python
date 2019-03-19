# 9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

numInStr = 5
numInCol = 4


matrix = []

for i in range(numInStr):
    str_ = []
    for j in range(numInCol):
        str_.append(randint(0, 100))
        print("{:5d}". format(str_[j]), end='')
    matrix.append(str_)
    print("")

minLst2 = []
for i in range(numInCol):
    minLst = []
    for j in range(numInStr):
        minLst.append(matrix[j][i])
    minLst2.append(min(minLst))

print("{} - Минимальные значения по столбцам". format(minLst2))
print("{} - Максимальное значение среди минимальных". format(max(minLst2)))

