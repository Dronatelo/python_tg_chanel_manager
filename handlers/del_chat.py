from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.main_kb import main_menu,del_ch_gp,menu
from settings.write_read_list import read_data_,del_data_

class del_chennels(StatesGroup):
    get_number=State()

async def get_chennels(message: types.Message):
    await message.answer(read_data_(), reply_markup=menu)
    await message.answer("Выберите номер для удаления", reply_markup=menu)
    await del_chennels.get_number.set()


async def del_chennel(message: types.Message, state: FSMContext):
    number_in_list = message.text
    
    if number_in_list == "Меню" or number_in_list == "/start":
        await message.answer('Вы возвращены в меню.', reply_markup=main_menu)
        await state.finish()
        return
    
    else:
        try:
            converted_number = int(number_in_list)
            print(del_data_(converted_number))
            await message.answer(read_data_(), reply_markup=menu)
            await message.answer(f"Запись №{converted_number} удалена!", reply_markup=main_menu)
            await state.finish()
            return
        except ValueError:
            await message.answer("Введенная строка не является числом.", reply_markup=main_menu)
            await state.finish()
            return


def register_handlers_del_chat(dp: Dispatcher):
    dp.register_message_handler(get_chennels, Text(equals=f"{del_ch_gp}"),state=None)
    dp.register_message_handler(del_chennel, state=del_chennels.get_number)

