from aiogram import types, Dispatcher
import markup
from create_bot import bot  # где создается бот и диспетчер


"""_________________________________________________раздел 'Главное меню'____________________________________________"""


# пользователь хочет вернуться назад в главное меню
async def back(callback: types.callback_query):
    print("назад в Главное меню - (back)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text=f'Выберите, что вас интересует', reply_markup=markup.creating_menu())


"""______________________________________раздел 'Ликвидность банковского сектора'____________________________________"""


# пользователь хочет вернуться в меню "Ликвидность банковского сектора"
async def back_dynamics_liquidity(callback: types.callback_query):
    print("назад в Динамика банковской ликвидности - (back_dynamics_liquidity)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Ликвидные средства банков", reply_markup=markup.dynamics_liquidity_markup())


# пользователь хочет вернуться в "Ликвидные средства банков (остатки)"
async def back_del_remains(callback: types.callback_query):
    print("назад в Ликвидные средства банков (остатки) - (back_row_remaining)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Ликвидные средства банков"
                                     "\nОстатки средств на корсчетах и депозитах",
                                reply_markup=markup.liquidity_balances_markup())


# пользователь хочет вернуться в "Длинный ряд - Остатки средств" (для графиков - с удалением предыдущих сообщений)
async def back_long_row_remains(callback: types.callback_query):
    print("назад в Длинный ряд (Остатки) - (back_long_row_remain)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Остатки средств на корсчетах и депозитах"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.long_row_balances())


# пользователь хочет вернуться в "Короткий ряд - Остатки средств" (для графиков - с удалением предыдущих сообщений)
async def back_short_row_remains(callback: types.callback_query):
    print("назад в Короткий ряд (Остатки) - (back_short_row_remaining)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Остатки средств на корсчетах и депозитах"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.short_row_balances())


# пользователь хочет венуться в "Ликвидные средства банков (приросты)"
async def back_del_gains(callback: types.callback_query):
    print("назад в Ликвидные средства банков (приросты) - (back_growth_menu)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Ликвидные средства банков"
                                     "\nПриросты остатков средств на корсчетах и депозитах",
                                reply_markup=markup.growth_markup())


# пользователь хочет венуться в Длинный ряд - приросты средств
async def back_long_row_gains(callback: types.callback_query):
    print("назад в длинный ряд (приросты) - (back_long_row_gains)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Приросты остатков средств\n\nС 2017 года по настоящий момент",
                                reply_markup=markup.long_row_growth())


# пользователь хочет вернуть в Короткий ряд - приросты средств
async def back_short_row_gains(callback: types.callback_query):
    print("назад в короткий ряд (приросты) - (back_short_row_gains)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Приросты остатков средств\n\nС 2022 года по настоящий момент",
                                reply_markup=markup.short_row_growth())


"""_________________________________________раздел 'Факторы ликвидности банков'______________________________________"""


# пользователь хочет вернуть в Факторы банковской ликвидности
async def back_liquidity_factors(callback: types.callback_query):
    print("Факторы банковской ликвидности (back_factors_liquidity)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Факторы формирования ликвидности банков",
                                reply_markup=markup.liquidity_factors_markup())


# пользователь хочет вернуть в Операции Казначейства и ЦБ
async def back_treasury_operations(callback: types.callback_query):
    print("Операции Казначейства и ЦБ")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Операции Казначейства и ЦБ Российской Федерации",
                                reply_markup=markup.treasury_operations_markup())


# пользователь хочет вернуть в Операции Казначейства и ЦБ (длинный ряд)
async def back_long_row_treasury(callback: types.callback_query):
    print("Операции Казначейства и ЦБ (длинный ряд)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Операции Казначейства и ЦБ Российской Федерации"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.treasury_operations_long_row())


# пользователь хочет вернуть в Операции Казначейства и ЦБ (короткий ряд)
async def back_short_row_treasury(callback: types.callback_query):
    print("Операции Казначейства и ЦБ (короткий ряд)")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Операции Казначейства и ЦБ Российской Федерации"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.treasury_operations_short_row())


# пользователь хочет вернуть в Валютные и налично-денежные операции
async def back_currency_cash_transactions_markup(callback: types.callback_query):
    print("Валютные и налично денежные операции")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Валютные и налично-денежные операции",
                                reply_markup=markup.currency_cash_transactions_markup())


# пользователь хочет вернуться в Валютные и наличные - Длинный ряд
async def back_long_row_currency_cash(callback: types.callback_query):
    print("Валютные и наличные - Длинный ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Валютные и налично-денежные операции"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.currency_cash_transactions_long_row()
                                )


# пользователь хочет вернуться в Валютные и наличные - Короткий ряд
async def back_short_row_currency_cash(callback: types.callback_query):
    print("Валютные и наличные - Короткий ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Валютные и налично-денежные операции"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.currency_cash_transactions_short_row())


# пользователь хочет вернуть в "Все факторы"
async def back_all_factors_markup(callback: types.callback_query):
    print("back Все факторы")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Все факторы",
                                reply_markup=markup.all_factors_markup())


# пользователь хочет вернуть в "Все факторы - Длинный ряд"
async def back_all_factors_long(callback: types.callback_query):
    print("back Все факторы Длинный ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Все факторы"
                                     "\n\nC 2017 года по настоящий момент",
                                reply_markup=markup.all_factors_long_row())


# пользователь хочет вернуть в "Все факторы - Короткий ряд"
async def back_all_factors_short(callback: types.callback_query):
    print("back Все факторы Короткий ряд")
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text="Все факторы"
                                     "\n\nC 2022 года по настоящий момент",
                                reply_markup=markup.all_factors_short_row())


def register_back_buttons(dp: Dispatcher):
    # пользователь хочет вернуться назад в главное меню
    dp.register_callback_query_handler(back, lambda callback: callback.data == "back")

    # пользователь хочет вернуться в меню "Ликвидность банковского сектора"
    dp.register_callback_query_handler(back_dynamics_liquidity,
                                       lambda callback: callback.data == "back_dynamics_liquidity")

    # пользователь хочет вернуться в "Ликвидные средства банков (остатки)"
    dp.register_callback_query_handler(back_del_remains, lambda callback: callback.data == "back_row_remaining")

    # пользователь хочет вернуться в "Длинный ряд - Остатки средств" (для графиков - с удалением предыдущих сообщений)
    dp.register_callback_query_handler(back_long_row_remains,
                                       lambda callback: callback.data == "back_long_row_remain")
    # пользователь хочет вернуться в "Короткий ряд - Остатки средств" (для графиков - с удалением предыдущих сообщений)
    dp.register_callback_query_handler(back_short_row_remains,
                                       lambda callback: callback.data == "back_short_row_remaining")

    # пользователь хочет вернуться в "Ликвидные средства банков (приросты)"
    dp.register_callback_query_handler(back_del_gains, lambda callback: callback.data == "back_growth_menu")

    # пользователь хочет вернуться в "Длинный ряд - Приросты средств" (для графиков - с удалением предыдущих сообщений)
    dp.register_callback_query_handler(back_long_row_gains, lambda callback: callback.data == "back_long_row_gains")
    # пользователь хочет вернуться в "Короткий ряд - Приросты средств" (для графиков - с удалением предыдущих сообщений)
    dp.register_callback_query_handler(back_short_row_gains, lambda callback: callback.data == "back_short_row_gains")

    # пользователь хочет вернуть в Факторы банковской ликвидности
    dp.register_callback_query_handler(back_liquidity_factors,
                                       lambda callback: callback.data == "back_factors_liquidity")

    # пользователь хочет вернуть в Операции Казначейства и ЦБ
    dp.register_callback_query_handler(back_treasury_operations,
                                       lambda callback: callback.data == "back_treasury_operations")

    # пользователь хочет вернуть в Операции Казначейства и ЦБ (длинный ряд)
    dp.register_callback_query_handler(back_long_row_treasury,
                                       lambda callback: callback.data == "back_long_row_treasury")
    # пользователь хочет вернуть в Операции Казначейства и ЦБ (длинный ряд)
    dp.register_callback_query_handler(back_short_row_treasury,
                                       lambda callback: callback.data == "back_short_row_treasury")

    # пользователь хочет вернуть в Валютные и налично денежные операции
    dp.register_callback_query_handler(back_currency_cash_transactions_markup,
                                       lambda callback: callback.data == "back_currency_cash_transactions_markup")

    # пользователь хочет вернуться в Валютные и наличные - Длинный ряд
    dp.register_callback_query_handler(back_long_row_currency_cash,
                                       lambda callback: callback.data == "back_long_row_currency_cash")
    # пользователь хочет вернуться в Валютные и наличные - Короткий ряд
    dp.register_callback_query_handler(back_short_row_currency_cash,
                                       lambda callback: callback.data == "back_short_row_currency_cash")

    # пользователь хочет вернуть в "Все факторы"
    dp.register_callback_query_handler(back_all_factors_markup,
                                       lambda callback: callback.data == "back_all_factors_markup")
    # пользователь хочет вернуть в "Все факторы - Длинный ряд"
    dp.register_callback_query_handler(back_all_factors_long,
                                       lambda callback: callback.data == "back_all_factors_long")
    # пользователь хочет вернуть в "Все факторы - Короткий ряд"
    dp.register_callback_query_handler(back_all_factors_short,
                                       lambda callback: callback.data == "back_all_factors_short")