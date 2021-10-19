from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple

FullEngine = namedtuple('FullEngine', ['Type', 'Volume', 'Horsepower'])

''' 
Классы составных частей 
'''


class CarEngine(Enum):
    SUV_ENGINE = '2UZ-FE'
    SPORT_ENGINE = '2JZ-GTE'
    VAN_ENGINE = 'l5'


class CarBody(Enum):
    SUV_BODY = auto()
    SPORT_BODY = auto()
    VAN_BODY = auto()


class CarTires(Enum):
    SUV_TIRES = '245/70 R16'
    SPORT_TIRES = '275/35 R19'
    VAN_TIRES = '215/60 R15'


class CarDrive(Enum):
    FRONT_DRIVE = auto()
    REAR_DRIVE = auto()
    FULL_DRIVE = auto()


class CarInterior(Enum):
    BASIC_INTERIOR = auto()
    EXTENDED_INTERIOR = auto()
    PREMIUM_INTERIOR = auto()


''' 
Класс компонуемого объекта
'''


class Car:
    def __init__(self, name):
        self.name = name
        self.engine = None
        self.body = None
        self.tires = None
        self.drive = None
        self.interior = None

    def __str__(self):
        info: str = f"Car name: {self.name} \n" \
                    f"Body type: {self.body} \n" \
                    f"Engine specifications: {self.engine.Type} " \
                    f"{self.engine.Volume}" \
                    f" {self.engine.Horsepower} \n" \
                    f"Tires: {self.tires} \n" \
                    f"Type of drive: {self.drive} \n" \
                    f"Selected interior: {self.interior} \n"

        return info


''' 
Абстрактный класс для задания интерфейса строителя
'''


class Builder(ABC):
    @abstractmethod
    def select_body(self) -> None: pass

    @abstractmethod
    def select_engine(self) -> None: pass

    @abstractmethod
    def select_tires(self) -> None: pass

    @abstractmethod
    def select_drive(self) -> None: pass

    @abstractmethod
    def select_interior(self) -> None: pass

    @abstractmethod
    def get_car(self) -> Car: pass


''' 
Реализация конкретных строителей для трех типов машин
'''


class SuvCarBuilder(Builder):
    def __init__(self):
        self.car = Car("Toyota Tundra")

    def select_body(self) -> None:
        self.car.body = CarBody.SUV_BODY.name

    def select_engine(self) -> None:
        self.car.engine = FullEngine(CarEngine.SUV_ENGINE.value, '4.7 L', '381 HP')

    def select_drive(self) -> None:
        self.car.drive = CarDrive.FULL_DRIVE.name

    def select_tires(self) -> None:
        self.car.tires = CarTires.SUV_TIRES.value

    def select_interior(self) -> None:
        self.car.interior = CarInterior.BASIC_INTERIOR.name

    def get_car(self) -> Car:
        return self.car


class SportCarBuilder(Builder):
    def __init__(self):
        self.car = Car("Toyota Supra")

    def select_body(self) -> None:
        self.car.body = CarBody.SPORT_BODY.name

    def select_engine(self) -> None:
        self.car.engine = FullEngine(CarEngine.SPORT_ENGINE.value, '3 L', '280 HP')

    def select_drive(self) -> None:
        self.car.drive = CarDrive.REAR_DRIVE.name

    def select_tires(self) -> None:
        self.car.tires = CarTires.SPORT_TIRES.value

    def select_interior(self) -> None:
        self.car.interior = CarInterior.PREMIUM_INTERIOR.name

    def get_car(self) -> Car:
        return self.car


class VanCarBuilder(Builder):
    def __init__(self):
        self.car = Car("Volkswagen Transporter")

    def select_body(self) -> None:
        self.car.body = CarBody.VAN_BODY.name

    def select_engine(self) -> None:
        self.car.engine = FullEngine(CarEngine.VAN_ENGINE.value, '2.5 L', '150 HP')

    def select_drive(self) -> None:
        self.car.drive = CarDrive.FRONT_DRIVE.name

    def select_tires(self) -> None:
        self.car.tires = CarTires.VAN_TIRES.value

    def select_interior(self) -> None:
        self.car.interior = CarInterior.EXTENDED_INTERIOR.name

    def get_car(self) -> Car:
        return self.car


"""
Класс Director, отвечающий за процесс поэтапной сборки машины
"""


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def build_car(self):
        if not self.builder:
            raise ValueError("Сборщик не установлен")
        self.builder.select_body()
        self.builder.select_engine()
        self.builder.select_drive()
        self.builder.select_tires()
        self.builder.select_interior()


if __name__ == '__main__':
    director = Director()
    for selected_car in (SuvCarBuilder, SportCarBuilder, VanCarBuilder):
        builder = selected_car()
        director.set_builder(builder)
        director.build_car()
        car = builder.get_car()
        print(car)
