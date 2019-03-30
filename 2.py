"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit

nums = int(input("Введите количество чисел"))
indexNum = int(input("Укажите индекс искомого i - го простого числа: "))

def SieveErat(nums, indexNum):
    lstNums = []
    for i in range(nums + 1):
        lstNums.append(i)

    lstSimpleNums = []
    i = 2
    while i <= nums:
        if lstNums[i] != 0:
            lstSimpleNums.append(lstNums[i])
            for j in range(i, nums + 1, i):
                lstNums[j] = 0
        i += 1
    return lstSimpleNums[indexNum - 1]

    #if indexNum > len(lstSimpleNums):
    #    return "Индекс искомого i - го простого числа задан не верно"
    #else:
    #    return lstSimpleNums[indexNum - 1]

print(SieveErat(nums, indexNum))
print("Время поиска i - ого по счету простого числа: Решето Эратосфена - ",
    timeit.timeit("SieveErat(nums, indexNum)", setup = 'from __main__ import SieveErat, nums, indexNum', number = 10))

# Сложность - О(n)
# Решето Эратосфена - число 11(lstSimleNums[5] in lstSimleNums=[0...100]), время поиска           0.0008319999999990557
# Решето Эратосфена - число 229(lstSimleNums[50] in lstSimleNums=[0...1000]), время поиска        0.0033247999999996836
# Решето Эратосфена - число 3571(lstSimleNums[500] in lstSimleNums=[0...10000]), время поиска     0.03324190000000016
# Решето Эратосфена - число 48611(lstSimleNums[5000] in lstSimleNums=[0...100000]), время поиска  0.3188165000000005


def WithSieveErat(nums, indexNum):
    lstSimpleNums=[]
    for i in range(2, nums + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lstSimpleNums.append(i)

    return lstSimpleNums[indexNum - 1]

print(WithSieveErat(nums, indexNum))
print("Время поиска i - ого по счету простого числа: без использования решета Эратосфена - ",
    timeit.timeit("WithSieveErat(nums, indexNum)", setup = 'from __main__ import WithSieveErat, nums, indexNum', number = 10))

# Сложность - О(n^2)
# Без использования решета Эратосфена - число 11(lstSimleNums[5] in lstSimleNums=[0...100]), время поиска           0.0008847999999996858
# Без использования решета Эратосфена - число 229(lstSimleNums[50] in lstSimleNums=[0...1000]), время поиска        0.04149300000000089
# Без использования решета Эратосфена - число 3571(lstSimleNums[500] in lstSimleNums=[0...10000]), время поиска     3.3281860000000005
# Без использования решета Эратосфена - число 48611(lstSimleNums[5000] in lstSimleNums=[0...100000]), время поиска  265.1359817

