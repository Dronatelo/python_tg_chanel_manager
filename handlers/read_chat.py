from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.main_kb import main_menu,read_ch_gp
from settings.write_read_list import read_data_

async def get_chennels(message: types.Message):
    await message.answer(read_data_(), reply_markup=main_menu)
    return

def register_handlers_read_chat(dp: Dispatcher):
    dp.register_message_handler(get_chennels, Text(equals=f"{read_ch_gp}"),state=None)
