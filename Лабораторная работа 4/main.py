from builder import Director, SuvCarBuilder, SportCarBuilder, VanCarBuilder
from composite import ComplexPart, Part, Car
from command import Mechanic, MechanicAssistant, Tools, AutoRepairShop, PrepareToolsCommand, RemoveToolsCommand, \
    AssembleTiresCommand, AssembleEngineCommand, InstallEngineTransmissionCommand, InstallInteriorCommand, \
    InstallBodyCommand

if __name__ == '__main__':
    print('FIRST PATTERN: BUILDER \n')
    director = Director()
    for selected_car in (SuvCarBuilder, SportCarBuilder, VanCarBuilder):
        builder = selected_car()
        director.set_builder(builder)
        director.build_car()
        car = builder.get_car()
        print(car)
    print('SECOND PATTERN: COMPOSITE \n')
    engine = ComplexPart('Engine')
    engine.add_product(Part('Cylinders', 100))
    engine.add_product(Part('Pistons', 120))
    body = Part('SUV Body', 2300)
    tires = Part('SUV tires', 200)
    SUV = Car('Toyota Tundra')
    SUV.add_product(engine)
    SUV.add_product(body)
    SUV.add_product(tires)
    print(SUV.cost())
    print('THIRD PATTERN: COMMAND \n')
    mechanic = Mechanic()
    mechanic_assistant = MechanicAssistant()
    tools = Tools()
    auto_repair_shop = AutoRepairShop()
    auto_repair_shop.add_command(PrepareToolsCommand(tools))
    auto_repair_shop.add_command(AssembleTiresCommand(mechanic_assistant))
    auto_repair_shop.add_command(AssembleEngineCommand(mechanic_assistant))
    auto_repair_shop.add_command(InstallBodyCommand(mechanic))
    auto_repair_shop.add_command(InstallEngineTransmissionCommand(mechanic))
    auto_repair_shop.add_command(InstallInteriorCommand(mechanic))
    auto_repair_shop.add_command(RemoveToolsCommand(tools))
    auto_repair_shop.build()
