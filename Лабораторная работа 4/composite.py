from abc import ABC, abstractmethod


class IPart(ABC):
    '''
    Интерфейс частей автомобиля
    '''

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass


class Part(IPart):
    '''
    Класс части автомобиля
    '''

    def __init__(self, name: str, cost: float):
        try:
            self.__cost = float(cost)
        except:
            self.__cost = 0
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class ComplexPart(IPart):
    '''
    Класс составных частей автомобиля
    '''

    def __init__(self, name: str):
        self.__name = name
        self.parts = []

    def cost(self):
        cost = 0
        for i in self.parts:
            cost += i.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, part: IPart):
        self.parts.append(part)

    def remove_product(self, part: IPart):
        self.parts.remove(part)

    def clear(self):
        self.parts = []


class Car(ComplexPart):
    '''
    Класс машины, состоящей из частей
    '''

    def __init__(self, name: str):
        super(Car, self).__init__(name)

    def cost(self):
        cost = 0
        for i in self.parts:
            cost_i = i.cost()
            print(f"Price for '{i.name()}' is {cost_i} dollars")
            cost += cost_i

        print(f"Price for '{self.name()}' is {cost} dollars")
        return cost
