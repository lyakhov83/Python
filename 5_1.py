"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import defaultdict


numCompany = int(input("Введите количество компаний: "))
company = defaultdict(list)

for i in range(numCompany):
    name = input("Введите название {} - й компании". format(i + 1))
    profit = [(int(input("Введите прибыль компании {} за {} - й квартал: ". format(name, j + 1)))) for j in range(4)]
    company[name] = sum(profit)

# для обхода значений словаря используем values
averProfit = sum(company.values()) / numCompany
print("Средняя прибыль {}.". format(averProfit))

for i in company:
    if company[i] < averProfit:
        print("{} компания имеет прибыль ниже средней: {}.". format(i, company[i]))
    elif company[i] > averProfit:
        print("{} компания имеет прибыль выше средней: {}.". format(i, company[i]))
