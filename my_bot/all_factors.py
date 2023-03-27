from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import markup
from create_bot import bot
from data_processing import func_charts

long_row = func_charts.long_row
short_row = func_charts.short_row

markup_back_long = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                              callback_data="back_all_factors_long"))

markup_back_short = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                               callback_data="back_all_factors_short"))


# пользователь зашел в "Все факторы"
async def all_factors_menu(callback: types.callback_query):
    print("Все факторы")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Все факторы", reply_markup=markup.all_factors_markup())


# пользователь зашел в "Все факторы" - Длинный ряд
async def all_factors_long_row(callback: types.callback_query):
    print("Все факторы - Длинный ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Все факторы"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.all_factors_long_row())


# Сумма операций за год (длинный ряд)
async def all_factors_year_res_long(callback: types.callback_query):
    print("Все факторы, Сумма операций по месяцам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.all_factors_res_bar_chart(long_row, "Y"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Все факторы\nВ миллиардах\nСумма операций по годам",
                           reply_markup=markup_back_long)


# Скользящая средняя - 247 дней (длинный ряд)
async def all_factors_year_rol_long(callback: types.callback_query):
    print("Все факторы, Скользящая средняя - 247 дней (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.all_factors_rol_chart(long_row, 247), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Все факторы\nВ миллиардах\nСкользящая средняя - 247 банковских дней",
                           reply_markup=markup_back_long)


# пользователь зашел в "Все факторы" - Короткий ряд
async def all_factors_short_row(callback: types.callback_query):
    print("Все факторы - Короткий ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Все факторы"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.all_factors_short_row())


# Сумма операций за месяц (короткий ряд)
async def all_factors_month_res_short(callback: types.callback_query):
    print("Все факторы, Сумма операций по месяцам (Короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.all_factors_res_area_chart(short_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Все факторы\nВ миллиардах\nСумма операций по месяцам",
                           reply_markup=markup_back_short)


# Скользящая средняя - 67 дней (короткий ряд)
async def all_factors_quarter_rol_short(callback: types.callback_query):
    print("Все факторы, Скользящая средняя - 67 дней (Короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.all_factors_rol_chart(short_row, 67), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Все факторы\nВ миллиардах\nСкользящая средняя - 67 банковских дней",
                           reply_markup=markup_back_short)


def register_all_factors(dp: Dispatcher):
    dp.register_callback_query_handler(all_factors_menu, lambda callback: callback.data == "all_factors")

    dp.register_callback_query_handler(all_factors_long_row, lambda callback: callback.data == "all_factors_long_row")
    dp.register_callback_query_handler(all_factors_year_res_long,
                                       lambda callback: callback.data == "all_factors_year_res_long")
    dp.register_callback_query_handler(all_factors_year_rol_long,
                                       lambda callback: callback.data == "all_factors_year_rol_long")

    dp.register_callback_query_handler(all_factors_short_row, lambda callback: callback.data == "all_factors_short_row")
    dp.register_callback_query_handler(all_factors_month_res_short,
                                       lambda callback: callback.data == "all_factors_month_res_short")
    dp.register_callback_query_handler(all_factors_quarter_rol_short,
                                       lambda callback: callback.data == "all_factors_quarter_rol_short")