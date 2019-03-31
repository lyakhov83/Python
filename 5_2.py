"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict

nums = defaultdict(list)

for i in range(2):
    varNums = input("Введите {} - ое число в шестнадцатеричном формате(0-9 и A-F): ". format(i + 1)).upper()
    nums[i + 1] = list(varNums)
    print(nums[1], nums[2])

numLst = [int("".join(v), 16) for v in nums.values()]
print(numLst[0], numLst[1])

print("Суума чисел: ", list(hex(sum(numLst)).upper())[2:])
print("Произведение чисел: ", list(hex(numLst[0] * numLst[1]).upper())[2:])
