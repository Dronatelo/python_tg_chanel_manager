from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

add_ch_gp = "🗂"
del_ch_gp ="✂️"
read_ch_gp ="📖"

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(add_ch_gp,read_ch_gp,del_ch_gp)

start_button = KeyboardButton("/start")
start_bt = ReplyKeyboardMarkup(resize_keyboard=True)
start_bt.add(start_button)

menu_bt = KeyboardButton("Меню")
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(menu_bt)

