from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    '''
    Интерфейс для выполняемых комманд
    '''

    @abstractmethod
    def execute(self) -> None:
        pass


class Mechanic:
    def install_body(self) -> None:
        print("Installing car body")

    def install_engine_and_transmission(self) -> None:
        print("Installing engine and transmission")

    def install_interior(self) -> None:
        print("Installing interior")


class MechanicAssistant:
    def assemble_engine(self) -> None:
        print("Assembling engine")

    def assemble_tires(self) -> None:
        print("Assembling tires")


class Tools:
    def prepare_tools(self) -> None:
        print("Preparing all the tools")

    def remove_tools(self) -> None:
        print("Removing the tools")


class InstallBodyCommand(ICommand):
    def __init__(self, executor: Mechanic):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.install_body()


class InstallEngineTransmissionCommand(ICommand):
    def __init__(self, executor: Mechanic):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.install_engine_and_transmission()


class InstallInteriorCommand(ICommand):
    def __init__(self, executor: Mechanic):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.install_interior()


class AssembleEngineCommand(ICommand):
    def __init__(self, executor: MechanicAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.assemble_engine()


class AssembleTiresCommand(ICommand):
    def __init__(self, executor: MechanicAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.assemble_tires()


class PrepareToolsCommand(ICommand):
    def __init__(self, executor: Tools):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_tools()


class RemoveToolsCommand(ICommand):
    def __init__(self, executor: Tools):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.remove_tools()


class AutoRepairShop:
    def __init__(self):
        self.history: List[ICommand] = []

    def add_command(self, command: ICommand) -> None:
        self.history.append(command)

    def build(self) -> None:
        if not self.history:
            print("No commands in order")

        else:
            for executor in self.history:
                executor.execute()
            self.history.clear()
