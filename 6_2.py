"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof

class MachineCNC:
    def __init__(self, title, typeMachine, typeCNC, weight):
        self.title = title
        self.typeMachine = typeMachine
        self.typeCNC = typeCNC
        self.weight = weight

class MachineCNCSlots:
    __slots__ = ["title", "typeMachine", "typeCNC", "weight"]
    def __init__(self, title, typeMachine, typeCNC, weight):
        self.title = title
        self.typeMachine = typeMachine
        self.typeCNC = typeCNC
        self.weight = weight

machine = MachineCNC("BRAY", "Mill", "Heidenhain", "15500" )
machine2 = MachineCNCSlots("HAAS", "Drill", "HaasCNC", "4100")

print(machine.__dict__)
print(asizeof.asizeof(machine))
print(asizeof.asizeof(machine2))

"""
Выходные данные:
{'title': 'BRAY', 'typeMachine': 'Mill', 'typeCNC': 'Heidenhain', 'weight': '19000'}
632 Bytes - выделено для "class MachineCNC" при использовании словаря атрибутов
296 Bytes - выделено для "class MachineCNCSlots", когда количество атрибутов класса есть константа
"""

