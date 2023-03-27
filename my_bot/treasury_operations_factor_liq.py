from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import markup
from create_bot import bot
from data_processing import func_charts

long_row = func_charts.long_row
short_row = func_charts.short_row


markup_back_long = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                              callback_data="back_long_row_treasury"))
markup_back_short = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                               callback_data="back_short_row_treasury"))


# Пользователь зашел в 'Операции Казначейства и ЦБ'
async def treasury_operations_menu(callback: types.callback_query):
    print("Операции Казначейства и ЦБ")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Операции Казначейства и ЦБ Российской Федерации",
                                reply_markup=markup.treasury_operations_markup())


"""__________________________________________________длинный ряд_____________________________________________________"""


# Пользователь зашел в Операции Казначейства и ЦБ (Длинный ряд)
async def treasury_long(callback: types.callback_query):
    print("Операции Казначейства и ЦБ (Длинный ряд)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Операции Казначейства и ЦБ Российской Федерации"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.treasury_operations_long_row())


# Скользящая средняя - 22 дня
async def treasury_oper_long_rol_month(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Скользящая средняя - 22 банковских дня (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.treasury_rol_chart(long_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСкользящая средняя - 22 банковских дня",
                           reply_markup=markup_back_long)


# Скользящая средняя - 67 дней
async def treasury_oper_long_rol_quarter(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Скользящая средняя - 67 банковских дней (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.treasury_rol_chart(long_row, 67), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСкользящая средняя - 67 банковских дней",
                           reply_markup=markup_back_long)


# Скользящая средняя - 247 дней
async def treasury_oper_long_rol_year(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Скользящая средняя - 247 банковских дней (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.treasury_rol_chart(long_row, 247), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСкользящая средняя - 247 банковских дней",
                           reply_markup=markup_back_long)


# Cумма операций за месяц
async def sum_trans_month_long_res(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Сумма опреаций за месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.sum_trans_res_chart(long_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСумма операций за месяц",
                           reply_markup=markup_back_long)


# Cумма операций за квартал
async def sum_trans_quarter_long_res(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Сумма опреаций за месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.sum_trans_res_chart(long_row, "Q"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСумма операций за квартал",
                           reply_markup=markup_back_long)


# Cумма операций за год
async def sum_trans_year_long_res(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Сумма опреаций за месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.sum_trans_res_chart(long_row, "Y"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСумма операций за год",
                           reply_markup=markup_back_long)


"""__________________________________________________короткий ряд____________________________________________________"""


# Пользователь зашел в Операции Казначейства и ЦБ (Длинный ряд)
async def treasury_short(callback: types.callback_query):
    print("Операции Казначейства и ЦБ (Короткий ряд)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Операции Казначейства и ЦБ Российской Федерации"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.treasury_operations_short_row())


# Скользящая средняя - 5 дней
async def treasury_oper_short_rol_week(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Скользящая средняя - 5 банковских дней (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.treasury_rol_chart(short_row, 5), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСкользящая средняя - 5 банковских дней",
                           reply_markup=markup_back_short)


# Скользящая средняя - 22 дня
async def treasury_oper_short_rol_month(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Скользящая средняя - 22 банковских дня (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.treasury_rol_chart(short_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСкользящая средняя - 22 банковских дня",
                           reply_markup=markup_back_short)


# Cумма операций за неделю
async def sum_trans_week_short_res(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Сумма опреаций за неделю (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.sum_trans_res_chart(short_row, "W"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСумма операций за неделю",
                           reply_markup=markup_back_short)


# Cумма операций за месяц
async def sum_trans_month_short_res(callback: types.callback_query):
    print("Операции Казначейства и ЦБ РФ, Сумма опреаций за месяц (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.sum_trans_res_chart(short_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Операции Казначейства и ЦБ РФ"
                                "\nВ миллиардах\nСумма операций за месяц",
                           reply_markup=markup_back_short)


def register_treasury_operations(dp: Dispatcher):
    dp.register_callback_query_handler(treasury_operations_menu, lambda call: call.data == "treasury_operations")
    dp.register_callback_query_handler(treasury_long, lambda call: call.data == "treasury_operations_long_row")

    dp.register_callback_query_handler(treasury_oper_long_rol_month,
                                       lambda call: call.data == "treasury_oper_long_rol_month_chart")
    dp.register_callback_query_handler(treasury_oper_long_rol_quarter,
                                       lambda call: call.data == "treasury_oper_long_rol_quarter_chart")
    dp.register_callback_query_handler(treasury_oper_long_rol_year,
                                       lambda call: call.data == "treasury_oper_long_rol_year_chart")
    dp.register_callback_query_handler(sum_trans_month_long_res,
                                       lambda call: call.data == "sum_trans_month_long_res_chart")
    dp.register_callback_query_handler(sum_trans_quarter_long_res,
                                       lambda call: call.data == "sum_trans_quarter_long_res_chart")
    dp.register_callback_query_handler(sum_trans_year_long_res,
                                       lambda call: call.data == "sum_trans_year_long_res_chart")

    dp.register_callback_query_handler(treasury_short, lambda call: call.data == "treasury_operations_short_row")

    dp.register_callback_query_handler(treasury_oper_short_rol_week,
                                       lambda call: call.data == "treasury_oper_short_rol_week_chart")
    dp.register_callback_query_handler(treasury_oper_short_rol_month,
                                       lambda call: call.data == "treasury_oper_short_rol_month_chart")
    dp.register_callback_query_handler(sum_trans_week_short_res,
                                       lambda call: call.data == "sum_trans_week_short_res_chart")
    dp.register_callback_query_handler(sum_trans_month_short_res,
                                       lambda call: call.data == "sum_trans_month_short_res_chart")
