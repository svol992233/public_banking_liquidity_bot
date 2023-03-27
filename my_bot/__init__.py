from dynamic_bank_liquidity_gains import register_handlers_bk_gains
from dynamic_bank_liquidity_remains import register_handlers_bk_remains
from treasury_operations_factor_liq import register_treasury_operations
from currency_cash_transactions import register_currency_cash_transactions
from all_factors import register_all_factors
import back_buttons
import markup
from aiogram import types
from aiogram.utils import executor
import time
from create_bot import bot, dp


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    print("Комманда start")
    await message.answer(text="Выберите, что вас интересует", reply_markup=markup.creating_menu())


@dp.message_handler(commands=["help"])
async def help_bot(message: types.Message):
    print("help")
    with open("bot_description.txt", encoding="utf-8") as description:
        await message.answer(text=description.read(), parse_mode="html")


@dp.callback_query_handler(lambda callback: callback.data == "dynamics_liquidity")
async def dynamics_liquidity(callback: types.CallbackQuery):
    print("Динамика банковской ликвидности")
    await bot.edit_message_text(text="Ликвидные средства банков", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                reply_markup=markup.dynamics_liquidity_markup())


@dp.callback_query_handler(lambda callback: callback.data == "liquidity_factors")
async def dynamics_liquidity(callback: types.CallbackQuery):
    print("Факторы банковской ликвидности")
    await bot.edit_message_text(text="Факторы формирования ликвидности банков", chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                reply_markup=markup.liquidity_factors_markup())


# ликвидность банковского сектора (остатки)
register_handlers_bk_remains(dp=dp)
# ликвидность банковского сектора (приросты)
register_handlers_bk_gains(dp=dp)
# Операции Казначейства и ЦБ
register_treasury_operations(dp=dp)
# Валютные и налично-денежные операции
register_currency_cash_transactions(dp=dp)
# Все факторы
register_all_factors(dp=dp)
# кнопки возвращения назад
back_buttons.register_back_buttons(dp=dp)


if __name__ == "__main__":
    try:
        executor.start_polling(dispatcher=dp, skip_updates=True)  # skip_updates=True - не отвечает, на сообщения,
                                                                           # которые он получил, пока был выключен
    except Exception as e:
        print(e)
        time.sleep(5)
