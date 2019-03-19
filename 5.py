#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

quanNum = int(input("Введите количество элементов массива: "))
lst = [randint(-100, 100) for i in range(0, quanNum)]
print("Список случайных чисел:", lst)

print("{} - индекс минимального элемента\n{} - значение минимального элемента".
      format(lst.index(max([i for i in lst if i < 0])), max([i for i in lst if i < 0])))