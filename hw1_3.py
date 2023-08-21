from aiogram import Bot,Dispatcher,types,executor
from random import randint
from config import token
bot = Bot(token)

dp = Dispatcher(bot)

try:
    @dp.message_handler(commands="start")
    async def start(message:types.Message):
        await message.answer(f'Привет,{message.from_user.full_name}')
        await message.answer(f'Нажмите /gamestart для начало игры ')

    @dp.message_handler(commands= "gamestart")
    async def choice(message:types.Message):
        await message.answer("Выберите от 1 до 3")

    @dp.message_handler(regexp="^[1-3]")
    async def random_1(message:types.Message):
        poh = randint(1,3)
        poh2= int(message.text)
        if poh == poh2:
            with open("1.jpg", "rb") as a:
                await message.answer_photo(a,"Вы выиграли ")
        
        else:
            with open("3.jpg", "rb") as b:
                await message.answer_photo(b,f"Чычавардин ука\nбот выбрал: {poh}")
except:
    TypeError(TypeError)

executor.start_polling(dp)