"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


for sym in range(32, 128):
    print(sym, "-->", chr(sym), end=" ")
    if sym < 100:
        print(" ", end="")
    if (sym - 1) % 10 == 0:
        print()

