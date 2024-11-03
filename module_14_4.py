#Задача "Продуктовая база":

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *


api = '8009539523:AAFMFgoO-Rvww6Zt-da5q_bZynwBo7E_YFk'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton( text='Рассчитать')
button2 = KeyboardButton( text='Информация')
#В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
button3 = KeyboardButton( text='Купить')
kb.add(button1)
kb.add(button2)
kb.add(button3)

kb2 = InlineKeyboardMarkup()
inline_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.row(inline_button1)
kb2.row(inline_button2)
#Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"
kb3 = InlineKeyboardMarkup()
inline_button3_1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
inline_button3_2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
inline_button3_3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
inline_button3_4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3.row(inline_button3_1, inline_button3_2, inline_button3_3, inline_button3_4)

products = get_all_products()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

#Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
@dp.message_handler(text=['Купить'])
#Функция get_buying_list должна выводить надписи
async def get_buying_list(message):
# 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
# После каждой надписи выводите картинки к продуктам.
    number = 0
    for product in products:
        number += 1
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(f'images/{number}.jpg', 'rb') as img:
            await message.answer_photo(img)
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)

#Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
@dp.callback_query_handler(text='product_buying')
#Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async  def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def  set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def  set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def  send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    calorii = 10 * int(data['third']) + 6.25 * int(data['second']) - 5 * int(data['first']) + 5
    await message.answer(f'Ваша норма калорий: {calorii}')
    await state.finish()


@dp.message_handler(commands='start')
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler()
async  def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)