"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import randint
"""
num = randint(0, 100)
quanAttempt = 1

while quanAttempt < 10:
    print("Ваша {}-ая попытка!". format(quanAttempt))
    userInp = int(input("Введите число от 0 до 100:"))
    if userInp != num:
        if num < userInp:
            print("Число {} больше искомого.\n". format(userInp))
        if num > userInp:
            print("Число {} меньше искомого.\n". format(userInp))
    else:
        print("Вы угадали!")
        break
    quanAttempt += 1
print("Искомое число:", num)
"""

def FindNum(quanAttempt, num):
    print("\nВаша {}-ая попытка!". format(quanAttempt))
    userInp = int(input("Введите число от 0 до 100:"))

    if quanAttempt == 10 or userInp == num:
        if userInp == num:
            print("Вы угадали!")
        print("Искомое число: {}.". format(num))
    else:
        if userInp > num:
            print("Искомое число меньше, чем {}.". format(userInp))
            FindNum(quanAttempt + 1, num)
        else:
            print("Искомое число больше, чем {}.". format(userInp))
            FindNum(quanAttempt + 1, num)

FindNum(1, randint(0, 100))
