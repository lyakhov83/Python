"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


num = int(input("Введите число: "))
leftSide = 0
for i in range(1, num + 1):
    leftSide += i
    rightSide = num * (num + 1) // 2
print("Левая часть:", leftSide)
print("Правая часть:", rightSide)
print("Равенство:", leftSide == rightSide)

