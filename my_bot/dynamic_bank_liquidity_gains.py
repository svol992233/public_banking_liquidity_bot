from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import markup
from create_bot import bot, dp  # где создается бот и диспетчер
from data_processing import func_charts

long_row = func_charts.long_row
short_row = func_charts.short_row

markup_back_long = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                              callback_data="back_long_row_gains"))
markup_back_short = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                               callback_data="back_short_row_gains"))


# пользователь зашел в меню "Ликвидные средства банков (приросты)"
async def growth_menu(callback: types.callback_query):
    print("Ликвидные средства банков (приросты)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Ликвидные средства банков"
                                     "\nПриросты остатков средств на корсчетах и депозитах",
                                reply_markup=markup.growth_markup())


"""__________________________________________________длинный ряд_____________________________________________________"""


# пользователь выбрал "Длинный ряд"
async def growth_long(callback: types.callback_query):
    print("Длинный ряд (приросты)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Приросты остатков средств на корсчетах и депозитах"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.long_row_growth())


# Приросты остатков средств за месяц (длинный ряд)
async def growth_long_month_res(callback: types.callback_query):
    print("Приросты - среднее значение остатков средств за месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_res_chart(long_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за месяц",
                           reply_markup=markup_back_long)


# Приросты остатков средств за квартал
async def growth_long_quarter_res(callback: types.callback_query):
    print("Приросты - среднее значение остатков средств за квартал (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_res_chart(long_row, "Q"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за квартал",
                           reply_markup=markup_back_long)


# Приросты остатков средств за год
async def growth_long_year_res(callback: types.callback_query):
    print("Приросты - среднее значение остатков средств за год (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_res_chart(long_row, "Y"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за год",
                           reply_markup=markup_back_long)


# Приросты остатков средств за банк. месяц
async def growth_long_month_rol(callback: types.callback_query):
    print("Приросты - скользящая средняя остатков средств за банк. месяц (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_rol_chart(long_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 22 банковских дня",
                           reply_markup=markup_back_long)


# Приросты остатков средств за банк. квартал
async def growth_long_quarter_rol(callback: types.callback_query):
    print("Приросты - скользящая средняя остатков средств за банк. квартал (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_rol_chart(long_row, 67), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 67 банковских дней",
                           reply_markup=markup_back_long)


# Приросты остатков средств за банк. год
async def growth_long_year_rol(callback: types.callback_query):
    print("Приросты - скользящая средняя остатков средств за банк. год (длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_rol_chart(long_row, 247), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 247 банковсих дней",
                           reply_markup=markup_back_long)


"""__________________________________________________короткий ряд____________________________________________________"""


# пользователь выбрал "Короткий ряд"
async def growth_short(callback: types.callback_query):
    print("Короткий ряд (приросты)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Приросты остатков средств на корсчетах и депозитах"
                                     f"\n\nС 2022 года по настоящий момент\n",
                                reply_markup=markup.short_row_growth())


# Приросты остатков средств за неделю
async def growth_short_week_res(callback: types.callback_query):
    print("Приросты - среднее значение за неделю (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_res_chart(short_row, "W"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за неделю",
                           reply_markup=markup_back_short)


# Приросты остатков средств за месяц
async def growth_short_month_res(callback: types.callback_query):
    print("Приросты - среднее значение за месяц (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_res_chart(short_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за месяц",
                           reply_markup=markup_back_short)


# Приросты остатков средств за банк. неделю
async def growth_short_week_rol(callback: types.callback_query):
    print("Приросты - скользящая средняя значений за неделю (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_rol_chart(short_row, 5), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 5 банковских дней",
                           reply_markup=markup_back_short)


# Приросты остатков средств за банк. месяц
async def growth_short_month_rol(callback: types.callback_query):
    print("Приросты - скользящая средняя значений за месяц (короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.growth_rol_chart(short_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 22 банковсих дня",
                           reply_markup=markup_back_short)


def register_handlers_bk_gains(dp: Dispatcher):
    # меню "Ликвидные средства банков (приросты)"
    dp.register_callback_query_handler(growth_menu, lambda callback: callback.data == "growth_menu")

    # меню "Длинный ряд"
    dp.register_callback_query_handler(growth_long, lambda callback: callback.data == "growth_long")

    # приросты остатков средств за месяц (длинный ряд)
    dp.register_callback_query_handler(growth_long_month_res, lambda callback: callback.data == "growth_long_month_res")
    # Приросты остатков средств за квартал (длинный ряд)
    dp.register_callback_query_handler(growth_long_quarter_res,
                                       lambda callback: callback.data == "growth_long_quarter_res")
    # Приросты остатков средств за год (длинный ряд)
    dp.register_callback_query_handler(growth_long_year_res,
                                       lambda callback: callback.data == "growth_long_year_res")
    # приросты остатков средств за банк. месяц (длинный ряд)
    dp.register_callback_query_handler(growth_long_month_rol, lambda callback: callback.data == "growth_long_month_rol")
    # приросты остатков средств за банк. квартал (длинный ряд)
    dp.register_callback_query_handler(growth_long_quarter_rol,
                                       lambda callback: callback.data == "growth_long_quarter_rol")
    # приросты остатков средств за банк. год (длинный ряд)
    dp.register_callback_query_handler(growth_long_year_rol, lambda callback: callback.data == "growth_long_year_rol")

    # меню "Короткий ряд"
    dp.register_callback_query_handler(growth_short, lambda callback: callback.data == "growth_short")

    # Приросты остатков средств за неделю
    dp.register_callback_query_handler(growth_short_week_res, lambda callback: callback.data == "growth_short_week_res")
    # Приросты остатков средств за месяц
    dp.register_callback_query_handler(growth_short_month_res,
                                       lambda callback: callback.data == "growth_short_month_res")
    # Приросты остатков средств за банк. неделю
    dp.register_callback_query_handler(growth_short_week_rol, lambda callback: callback.data == "growth_short_week_rol")
    # Приросты остатков средств за банк. месяц
    dp.register_callback_query_handler(growth_short_month_rol,
                                       lambda callback: callback.data == "growth_short_month_rol")