from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


available_cars_names = ["спорткар", "внедорожник", "минивэн"]
available_cars_equipment = ["минимальная", "стандартная", "максимальная"]


class OrderCar(StatesGroup):
    waiting_for_car_name = State()
    waiting_for_car_equipment = State()


async def car_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_cars_names:
        keyboard.add(name)
    await message.answer("Выберите тип автомобиля:", reply_markup=keyboard)
    await OrderCar.waiting_for_car_name.set()


# Обратите внимание: есть второй аргумент
async def car_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_cars_names:
        await message.answer("Выберите тип автомобиля, используя кнопки ниже.")
        return
    await state.update_data(chosen_car=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for equipment in available_cars_equipment:
        keyboard.add(equipment)
    # Для простых шагов можно не указывать название состояния, обходясь next()
    await OrderCar.next()
    await message.answer("Выберите комплектацию:", reply_markup=keyboard)


async def car_eqp__chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_cars_equipment:
        await message.answer("Выберите комплектацию, используя кнопки ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы заказали {user_data['chosen_car']}. Комплектация - {message.text.lower()}\n"
                         f"Заполните форму получения заказа - /delivery", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_car(dp: Dispatcher):
    dp.register_message_handler(car_start, commands="car", state="*")
    dp.register_message_handler(car_chosen, state=OrderCar.waiting_for_car_name)
    dp.register_message_handler(car_eqp__chosen, state=OrderCar.waiting_for_car_equipment)
