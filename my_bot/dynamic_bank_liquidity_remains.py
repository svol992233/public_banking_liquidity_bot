from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import markup
from create_bot import bot  # где создается бот и диспетчер
from data_processing import func_charts

long_row = func_charts.long_row
short_row = func_charts.short_row

markup_back_long = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                              callback_data="back_long_row_remain"))
markup_back_short = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Назад",
                                                                               callback_data="back_short_row_remaining"))


# Пользователь зашел в раздел "Ликвидные средства банков (остатки)"
async def remaining(callback: types.callback_query):
    print("Ликвидные средства банков (остатки)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Ликвидные средства банков"
                                     "\nОстатки средств на корсчетах и депозитах",
                                reply_markup=markup.liquidity_balances_markup())

"""__________________________________________________длинный ряд_____________________________________________________"""


# Пользователь зашел в раздел "Длинный ряд"
async def balances_long(callback: types.callback_query):
    print("Длинный ряд (остатки)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Остатки средств на корсчетах и депозитах"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.long_row_balances())


# Пользователь зашел в раздел "Среднее значение по месяцам"
async def monthly_average_remaining(callback: types.callback_query):
    print("Остатки - среднее значение по месяцам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_res_chart(long_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за месяц",
                           reply_markup=markup_back_long)


# Пользователь зашел в раздел "Среднее значение по кварталам"
async def average_quarter_remaining(callback: types.callback_query):
    print("Остатки - среднее значение по кварталам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_res_chart(long_row, "Q"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за квартал",
                           reply_markup=markup_back_long)


# Пользователь зашел в раздел "Среднее значение по годам"
async def average_year_remaining(callback: types.callback_query):
    print("Остатки - среднее значение по годам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_res_chart(long_row, "Y"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за год",
                           reply_markup=markup_back_long)


# Пользователь зашел в раздел "Скользящая средняя по банк. месяцам"
async def moving_average_month_remaining(callback: types.callback_query):
    print("Остатки - скользящая средняя по банк. месяцам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=open(func_charts.remains_rol_chart(long_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 22 дня",
                           reply_markup=markup_back_long)


# Пользователь зашел в раздел "Скользящая средняя по банк. кварталам"
async def moving_average_quarter_remaining(callback: types.callback_query):
    print("Остатки - скользящая средняя по банк. кварталам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_rol_chart(long_row, 67), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 67 дней",
                           reply_markup=markup_back_long)


# Пользователь зашел в раздел "Скользящая средняя по банк. годам"
async def moving_average_year_remaining(callback : types.callback_query):
    print("Остатки - скользящая средняя по банк. годам (Длинный ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_rol_chart(long_row, 247), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 247 дней",
                           reply_markup=markup_back_long)


"""__________________________________________________короткий ряд____________________________________________________"""


# Пользователь зашел в раздел "Короткий ряд"
async def balances_short(callback : types.callback_query):
    print("Короткий ряд (остатки)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Остатки средств на корсчетах и депозитах"
                                     "\n\nС 2022 года по настоящий момент",
                                reply_markup=markup.short_row_balances())


# Пользователь зашел в раздел "Среднее значение по неделям"
async def short_average_week(callback: types.callback_query):
    print("Остатки - среднее значение по неделям (Короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_res_chart(short_row, "W"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за неделю",
                           reply_markup=markup_back_short)


# Пользователь зашел в раздел "Среднее значение по месяцам"
async def short_average_month(callback: types.callback_query):
    print("Остатки - среднее значение по неделям (Короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_res_chart(short_row, "M"), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСреднее значение за месяца",
                           reply_markup=markup_back_short)


# Скользящая средняя по банк. неделям
async def short_moving_average_week(callback: types.callback_query):
    print("Остатки - скользящая средняя по банк. неделям (Короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_rol_chart(short_row, 5), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 5 дней",
                           reply_markup=markup_back_short)


# Скользящая средняя по банк. месяцам
async def short_moving_average_month(callback: types.callback_query):
    print("Остатки - скользящая средняя по банк. неделям (Короткий ряд)")
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)  # удаляем с-ие с меню
    await bot.send_photo(chat_id=callback.message.chat.id, photo=open(func_charts.remains_rol_chart(short_row, 22), "rb"))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text="Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                                "\nВ миллиардах\nСкользящая средняя - 22 дня",
                           reply_markup=markup_back_short)


def register_handlers_bk_remains(dp: Dispatcher):
    # меню ликвидные средства банков (остатки)
    dp.register_callback_query_handler(remaining, lambda callback: callback.data == "remaining_menu")

    # меню длинного ряда
    dp.register_callback_query_handler(balances_long, lambda callback: callback.data == "balances_long")

    # длинный ряд (графики)
    dp.register_callback_query_handler(monthly_average_remaining, lambda callback: callback.data == "cd_long_res_month")
    dp.register_callback_query_handler(average_quarter_remaining,
                                       lambda callback: callback.data == "cd_long_res_quarter")
    dp.register_callback_query_handler(average_year_remaining, lambda callback: callback.data == "cd_long_res_year")
    dp.register_callback_query_handler(moving_average_month_remaining,
                                       lambda callback: callback.data == "cd_long_rol_month")
    dp.register_callback_query_handler(moving_average_quarter_remaining,
                                       lambda callback: callback.data == "cd_long_rol_quarter")
    dp.register_callback_query_handler(moving_average_year_remaining,
                                       lambda callback: callback.data == "cd_long_rol_year")

    # меню короткого ряда
    dp.register_callback_query_handler(balances_short, lambda callback: callback.data == "balances_short")

    # короткий ряд (графики)
    dp.register_callback_query_handler(short_average_week, lambda callback: callback.data == "cd_short_res_week")
    dp.register_callback_query_handler(short_average_month, lambda callback: callback.data == "cd_short_res_month")
    dp.register_callback_query_handler(short_moving_average_week, lambda callback: callback.data == "cd_short_rol_week")
    dp.register_callback_query_handler(short_moving_average_month,
                                       lambda callback: callback.data == "cd_short_rol_month")
