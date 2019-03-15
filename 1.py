"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
"""
print("{:*^50}".format("Добро пожаловать в программу-калькулятор!"))

while True:
    action = input("0 - отдыхаем;\n1 - работаем;")
    if action == "0":
        print("Программа-калькулятор завершена!")
        break
    elif action == "1":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Ваши числа {} и {}".format(num1, num2))
        mathOperSym = input("Выбирите тип операции: + - * /")
        if mathOperSym in ("+", "-", "*", "/"):
            if mathOperSym == "+":
                print("Сумма чисел: {} + {} = {}". format(num1, num2, num1 + num2))
            elif mathOperSym == "-":
                print("Разность чисел: {} - {} = {}". format(num1, num2, num1 - num2))
            elif mathOperSym == "*":
                print("Произведение чисел: {} * {} = {}". format(num1, num2, num1 * num2))
            elif mathOperSym == "/":
                if num2 != 0:
                    print("Частное чисел: {:.3f} / {:.3f} = {:.3f}". format(num1, num2, num1 / num2))
                else:
                    print("Деление на ноль запрещено!")
    else:
        print("Неверный знак операции.")
"""
print("{:*^50}".format("Добро пожаловать в программу-калькулятор!"))

def RecCalc():
    action = input("0 - отдыхаем\n1 - работаем")

    if action == "0":
       return "Выход"

    elif action == "1":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Ваши числа {} и {}".format(num1, num2))
        mathOperSym = input("Выбирите тип операции: + - * /")

        if mathOperSym in ("+", "-", "*", "/"):
            if mathOperSym == "+":
                print("Сумма чисел: {} + {} = {}". format(num1, num2, num1 + num2))
                return RecCalc()
            elif mathOperSym == "-":
                print("Разность чисел: {} - {} = {}". format(num1, num2, num1 - num2))
                return RecCalc()
            elif mathOperSym == "*":
                print("Произведение чисел: {} * {} = {}". format(num1, num2, num1 * num2))
                return RecCalc()
            elif mathOperSym == "/":
                if num2 != 0:
                    print("Частное чисел: {:.3f} / {:.3f} = {:.3f}". format(num1, num2, num1 / num2))
                else:
                    print("Деление на ноль запрещено!")
                return RecCalc()
        else:
            print("Неверный знак операции.")
            return RecCalc()

print(RecCalc())






