"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input("Введите натуральное число: ")
evenNum = 0
oddNum = 0

for i in num:
    if int(i) % 2 == 0:
        evenNum += 1
    else:
        oddNum += 1

print("Число {} содержит: {} - четных и {} - нечетных цифр.". format(num, evenNum, oddNum))

"""
num = int(input("Введите число: "))
evenNum = 0
oddNum = 0

def NumCount(num, evenNum, oddNum):
    if num == 0:
        return evenNum, oddNum
    else:
        N = num % 10
        num = num // 10
        if N % 2 == 0:
            evenNum += 1
            return NumCount(num, evenNum, oddNum)
        else:
            oddNum += 1
            return NumCount(num, evenNum, oddNum)
#print("Число {} содержит: {} - четных и {} - нечетных цифр.". format(num, quantity, nextNum))
print("Количество четных и нечетных цифр в числе равно: ", NumCount(num, evenNum, oddNum))
"""

