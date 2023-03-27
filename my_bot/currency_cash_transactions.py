from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import markup
from create_bot import bot
from data_processing import func_charts

long_row = func_charts.long_row
short_row = func_charts.short_row

markup_back_long = \
    InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                               callback_data="back_long_row_currency_cash"))

markup_back_short = \
    InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                               callback_data="back_short_row_currency_cash"))


# Пользователь зашел в 'Валюта и наличные'
async def currency_cash_transactions_menu(callback: types.callback_query):
    print("Валютные и налично-денежные операции")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Валютные и налично-денежные операции",
                                reply_markup=markup.currency_cash_transactions_markup())


"""__________________________________________________длинный ряд_____________________________________________________"""


# Пользователь зашел в 'Валюта и наличные' - Длинный ряд
async def currency_cash_transactions_long_menu(callback: types.callback_query):
    print("Валютные и налично-денежные операции - Длинный ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Валютные и налично-денежные операции"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.currency_cash_transactions_long_row())


# Сумма операций за месяц
async def currency_cash_res_month_long(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Сумма операций за месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_res_chart(long_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСумма операций по месяцам",
                           reply_markup=markup_back_long)


# Сумма операций за квартал
async def currency_cash_res_quarter_long(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Сумма операций за квартал (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_res_chart(long_row, "Q"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСумма операций по кварталам",
                           reply_markup=markup_back_long)


# Сумма операций за год
async def currency_cash_res_year_long(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Сумма операций за год (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_res_chart(long_row, "Y"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСумма операций по годам",
                           reply_markup=markup_back_long)


# Скользящая средняя - 22 дня
async def currency_cash_rol_month_long(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Скользящая средняя - 22 банковских дня (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_rol_chart(long_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСкользящая средняя - 22 банковских дня",
                           reply_markup=markup_back_long)


# Скользящая средняя - 67 дней
async def currency_cash_rol_quarter_long(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Скользящая средняя - 67 банковских дней (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_rol_chart(long_row, 67), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСкользящая средняя - 67 банковских дней",
                           reply_markup=markup_back_long)


# Скользящая средняя - 247 дней
async def currency_cash_rol_year_long(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Скользящая средняя - 247 банковских дней (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_rol_chart(long_row, 247), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСкользящая средняя - 247 банковских дней",
                           reply_markup=markup_back_long)


"""__________________________________________________короткий ряд____________________________________________________"""


# Пользователь зашел в 'Валюта и наличные' - Короткий ряд
async def currency_cash_transactions_short_menu(callback: types.callback_query):
    print("Валютные и налично-денежные операции - Короткий ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Валютные и налично-денежные операции"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.currency_cash_transactions_short_row())


# Сумма операция за неделю
async def currency_cash_res_week_short(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Сумма операций за неделю (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_res_chart(short_row, "W"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСумма операций по неделям",
                           reply_markup=markup_back_short)


# Сумма операций за месяц
async def currency_cash_res_month_short(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Сумма операций за месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_res_chart(short_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСумма операций по месяцам",
                           reply_markup=markup_back_short)


# Сумма операций за квартал
async def currency_cash_res_quarter_short(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Сумма операций за квартал (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_res_chart(short_row, "Q"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСумма операций по кварталам",
                           reply_markup=markup_back_short)


# Скользящая средняя - 5 дней
async def currency_cash_rol_week_short(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Скользящая средняя - 5 банковских дней (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_rol_chart(short_row, 5), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСкользящая средняя - 5 банковских дней",
                           reply_markup=markup_back_short)


# Скользящая средняя - 22 дня
async def currency_cash_rol_month_short(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Скользящая средняя - 22 банковских дня (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_rol_chart(short_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСкользящая средняя - 22 банковских дня",
                           reply_markup=markup_back_short)


# Скользящая средняя - 67 дней
async def currency_cash_rol_quarter_short(callback: types.callback_query):
    print("Валютные и налично-денежные операции, Скользящая средняя - 67 банковских дней (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.currency_cash_rol_chart(short_row, 67), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Валютные и налично-денежные операции"
                                "\nВ миллиардах\nСкользящая средняя - 67 банковских дней",
                           reply_markup=markup_back_short)


def register_currency_cash_transactions(dp: Dispatcher):
    dp.register_callback_query_handler(currency_cash_transactions_menu,
                                       lambda callback: callback.data == "currency_cash")
    dp.register_callback_query_handler(currency_cash_transactions_long_menu,
                                       lambda callback: callback.data == "currency_cash_transactions_long_row")

    dp.register_callback_query_handler(currency_cash_res_month_long,
                                       lambda callback: callback.data == "currency_cash_res_month_long_row")
    dp.register_callback_query_handler(currency_cash_res_quarter_long,
                                       lambda callback: callback.data == "currency_cash_res_quarter_long_row")
    dp.register_callback_query_handler(currency_cash_res_year_long,
                                       lambda callback: callback.data == "currency_cash_res_year_long_row")
    dp.register_callback_query_handler(currency_cash_rol_month_long,
                                       lambda callback: callback.data == "currency_cash_rol_month_long_row")
    dp.register_callback_query_handler(currency_cash_rol_quarter_long,
                                       lambda callback: callback.data == "currency_cash_rol_quarter_long_row")
    dp.register_callback_query_handler(currency_cash_rol_year_long,
                                       lambda callback: callback.data == "currency_cash_rol_year_long_row")

    dp.register_callback_query_handler(currency_cash_transactions_short_menu,
                                       lambda callback: callback.data == "currency_cash_transactions_short_row")

    dp.register_callback_query_handler(currency_cash_res_week_short,
                                       lambda callback: callback.data == "currency_cash_res_week_short_row")
    dp.register_callback_query_handler(currency_cash_res_month_short,
                                       lambda callback: callback.data == "currency_cash_res_month_short_row")
    dp.register_callback_query_handler(currency_cash_res_quarter_short,
                                       lambda callback: callback.data == "currency_cash_res_quarter_short_row")
    dp.register_callback_query_handler(currency_cash_rol_week_short,
                                       lambda callback: callback.data == "currency_cash_rol_week_short_row")
    dp.register_callback_query_handler(currency_cash_rol_month_short,
                                       lambda callback: callback.data == "currency_cash_rol_month_short_row")
    dp.register_callback_query_handler(currency_cash_rol_quarter_short,
                                       lambda callback: callback.data == "currency_cash_rol_quarter_short_row")

