"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
"""
numEl = int(input("Укажите количество элементов: "))
firstEl = 1
countRow = 0
sumEl = 0

while countRow < numEl:
    sumEl += firstEl
    firstEl /= -2
    countRow += 1
print("Сумма элементов ряда:", sumEl)
"""
numEl = int(input("Укажите количество элементов: "))

def RecNum(numEl, firstEl, countRow, sumEl):
    if countRow == numEl:
        return sumEl
    elif countRow < numEl:
        return RecNum(numEl, firstEl/-2, countRow + 1, sumEl + firstEl)

print("Сумма элементов ряда:", RecNum(numEl, 1, 0, 0))
