"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

#   2.3. Сформировать из введенного числа обратное по порядку входящих в него
#   цифр и вывести на экран. Например, если введено число 3486,
#   то надо вывести число 6843.

from memory_profiler import profile
import sys

nums = int(input("Введите количество чисел"))
indexNum = int(input("Укажите индекс искомого i - го простого числа: "))



"""
@profile
def RevFunc(num, revNum):
    if num == 0:
        return revNum
    else:
        var = num % 10
        num = num // 10
        revNum *= 10
        revNum += var
        return RevFunc(num, revNum)
print("Число перевёртыш:", RevFunc(num, revNum))
"""
"""
Входные данные: 987456231
                Python 3.7.2
                x64-based PC

Выходные данные: Число перевёртыш: 132654789
Память, выделенная для запуска программы - 19.6 MiB

    Line #    Mem usage    Increment   Line Contents
================================================
    20     19.6 MiB     19.6 MiB   @profile
    21                             def RevFunc(num, revNum):
    22     19.6 MiB      0.0 MiB       if num == 0:
    23     19.6 MiB      0.0 MiB           return revNum
    24                                 else:
    25     19.6 MiB      0.0 MiB           var = num % 10
    26     19.6 MiB      0.0 MiB           num = num // 10
    27     19.6 MiB      0.0 MiB           revNum *= 10
    28     19.6 MiB      0.0 MiB           revNum += var
    29     19.7 MiB      0.0 MiB           return RevFunc(num, revNum)





#   4.2 Написать два алгоритма нахождения i-го по счёту простого числа.
#   Без использования «Решета Эратосфена»;
#   Используя алгоритм «Решето Эратосфена»

@profile
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

    del lstNums
    return lstSimpleNums[indexNum - 1]

print(SieveErat(nums, indexNum))


Входные данные: nums = 10000
                indexNum = 500
                Python 3.7.2
                x64-based PC

Выходные данные: 3571

Память, выделенная для запуска программы            - 19.7 MiB
На заполнение списка listNums числами потребовалось - 0.5 MiB
После удаления списка listNums, освободилось        - 1.5 MiB
Line #    Mem usage    Increment   Line Contents
================================================
    58     19.6 MiB     19.6 MiB   @profile
    59                             def SieveErat(nums, indexNum):
    60     19.6 MiB      0.0 MiB       lstNums = []
    61     24.6 MiB      0.0 MiB       for i in range(nums + 1):
    62     24.6 MiB      0.5 MiB           lstNums.append(i)
    63
    64     24.6 MiB      0.0 MiB       lstSimpleNums = []
    65     24.6 MiB      0.0 MiB       i = 2
    66     24.6 MiB      0.0 MiB       while i <= nums:
    67     24.6 MiB      0.0 MiB           if lstNums[i] != 0:
    68     24.6 MiB      0.0 MiB               lstSimpleNums.append(lstNums[i])
    69     24.6 MiB      0.0 MiB               for j in range(i, nums + 1, i):
    70     24.6 MiB      0.0 MiB                   lstNums[j] = 0
    71     24.6 MiB      0.0 MiB           i += 1
    72
    73     23.1 MiB      0.0 MiB       del lstNums
    74     23.1 MiB      0.0 MiB       return lstSimpleNums[indexNum - 1]
"""

@profile
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

"""
Входные данные: nums = 10000
                indexNum = 500
                Python 3.7.2
                x64-based PC

Выходные данные: 3571

Память, выделенная для запуска программы - 19.5 MiB

Line #    Mem usage    Increment   Line Contents
================================================
   117     19.5 MiB     19.5 MiB   @profile
   118                             def WithSieveErat(nums, indexNum):
   119     19.5 MiB      0.0 MiB       lstSimpleNums=[]
   120     19.6 MiB      0.0 MiB       for i in range(2, nums + 1):
   121     19.6 MiB      0.0 MiB           for j in range(2, i):
   122     19.6 MiB      0.0 MiB               if i % j == 0:
   123     19.6 MiB      0.0 MiB                   break
   124                                     else:
   125     19.6 MiB      0.0 MiB               lstSimpleNums.append(i)
   126
   127     19.5 MiB      0.0 MiB       return lstSimpleNums[indexNum - 1]

"""