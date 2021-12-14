from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

available_delivery_names = ["доставка курьером", "самовывоз"]
available_delivery_payment = ["наличными", "картой"]


class OrderDelivery(StatesGroup):
    waiting_for_delivery_name = State()
    waiting_for_delivery_payment = State()


async def delivery_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_delivery_names:
        keyboard.add(name)
    await message.answer("Выберите способ получения заказанного автомобиля:", reply_markup=keyboard)
    await OrderDelivery.waiting_for_delivery_name.set()


async def delivery_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_delivery_names:
        await message.answer("Выберите способ доставки, используя кнопки ниже.")
        return
    await state.update_data(chosen_delivery=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for payment in available_delivery_payment:
        keyboard.add(payment)
    # для простых шагов можно не указывать название состояния, обходясь next()
    await OrderDelivery.next()
    await message.answer("Теперь выберите способ оплаты:", reply_markup=keyboard)


async def delivery_size_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_delivery_payment:
        await message.answer("Выберите способ оплаты, используя кнопки ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Ваш способ доставки - {user_data['chosen_delivery']}. Оплата {message.text.lower()}.\n"
                         f"Оформите заказ: /car", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_delivery(dp: Dispatcher):
    dp.register_message_handler(delivery_start, commands="delivery", state="*")
    dp.register_message_handler(delivery_chosen, state=OrderDelivery.waiting_for_delivery_name)
    dp.register_message_handler(delivery_size_chosen, state=OrderDelivery.waiting_for_delivery_payment)
