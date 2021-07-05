"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
"""
num = int(input("Введите целое число: "))
revNum = (0)

while num > 0:
    var = num % 10
    num = num // 10
    revNum *= 10
    revNum += var
print("Число перевёртыш {}". format(revNum))

"""
num = int(input("Введите целое число: "))
revNum = 0

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