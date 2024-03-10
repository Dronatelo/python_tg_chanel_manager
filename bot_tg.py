from aiogram import executor
from create_bot import dp
from handlers import start_connect, add_chat,del_chat,read_chat,parse_service

async def on_startup(_):
    print("Bot Online!")
    
start_connect.register_handlers_start_connect(dp)
add_chat.register_handlers_add_chat(dp)
read_chat.register_handlers_read_chat(dp)
del_chat.register_handlers_del_chat(dp)
parse_service.register_handlers_menu(dp)
    
def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == '__main__':
    main()