"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile

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

print(timeit.timeit("NumCount(num, evenNum, oddNum)", setup = "from __main__ import NumCount, num, evenNum, oddNum"))
cProfile.run("NumCount(num, evenNum, oddNum)")

"""
Входные данные: 285147936123546987

Выходные данные: Количество четных и нечетных цифр в числе равно:  (8, 10)
Время поиска при стандартном количестве проходов: 4.798279499999999

22 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     19/1    0.000    0.000    0.000    0.000 1.py:14(NumCount)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

