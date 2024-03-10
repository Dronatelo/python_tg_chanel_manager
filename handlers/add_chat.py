from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.main_kb import main_menu,add_ch_gp,menu
from settings.write_read_list import write_data_

class add_chennel_id(StatesGroup):
    get_name_chat=State()
    get_id_chat=State()

async def get_chennel(message: types.Message):
    await message.answer("Вставьте название чата или группы.", reply_markup=menu)
    await add_chennel_id.get_name_chat.set()


async def get_chat_name(message: types.Message, state: FSMContext):
    chat_name = message.text
    
    if chat_name == "Меню" or chat_name == "/start":
        await message.answer('Вы возвращены в меню.', reply_markup=main_menu)
        await state.finish()
        return
    
    else:
        async with state.proxy() as data:
            data['chat name'] = chat_name
        await message.answer("Вставьте ID чата или группы.", reply_markup=menu)
        await add_chennel_id.get_id_chat.set()


async def get_chat_id(message: types.Message, state: FSMContext):
    chat_id = message.text
    
    if chat_id == "Меню" or chat_id == "/start":
        await message.answer('Вы возвращены в меню.', reply_markup=main_menu)
        await state.finish()
        return
    
    else:
        async with state.proxy() as data:
            chat_name = data['chat name']
        try:
            converted_number = int(chat_id)
            await message.answer(write_data_(chat_name, converted_number), reply_markup=main_menu)
            await state.finish()
            return
        except ValueError:
            await message.answer(f"Cтрока {converted_number} не является числом.", reply_markup=main_menu)
            await state.finish()
            return

def register_handlers_add_chat(dp: Dispatcher):
    dp.register_message_handler(get_chennel, Text(equals=f"{add_ch_gp}"),state=None)
    dp.register_message_handler(get_chat_name, state=add_chennel_id.get_name_chat)
    dp.register_message_handler(get_chat_id, state=add_chennel_id.get_id_chat)

