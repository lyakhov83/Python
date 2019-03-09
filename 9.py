# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

firNum = int(input("Введите первое число: "))
secNum = int(input("Введите второе число: "))
thNum = int(input("Введите третье число: "))

if firNum == secNum == thNum:
    print("Введенные числа - равны между собой!")
elif firNum == secNum or firNum == thNum or secNum == thNum:
    print("Два из трех чисел - равны между собой!")

else:
    if firNum < secNum < thNum:
        print("%d - средние число, введенное пользователем." % secNum)
    elif secNum < firNum < thNum:
        print("%d - средние число, введенное пользователем." % firNum)
    else:
        print("%d - средние число, введенное пользователем." % thNum)



