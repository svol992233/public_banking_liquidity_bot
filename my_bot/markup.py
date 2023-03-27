from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def creating_menu():
    """Таблица стартового меню"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Динамика банковской ликвидности", callback_data="dynamics_liquidity"),
        InlineKeyboardButton(text="Факторы ликвидности банков", callback_data="liquidity_factors"),
    )
    return markup


def dynamics_liquidity_markup():
    """Таблица динамики банковской ликвидности"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Остатки средств", callback_data="remaining_menu"),
        InlineKeyboardButton(text="Приросты средств", callback_data="growth_menu"),
        InlineKeyboardButton(text="Назад", callback_data="back")
    )
    return markup


def liquidity_balances_markup():
    """Остатки средств на корсчетах и депозитах коммерческих банков (Кнопка "Ликвидные средства банков (остатки)")"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Длинный ряд", callback_data="balances_long"),
        InlineKeyboardButton(text="Короткий ряд", callback_data="balances_short"),
        InlineKeyboardButton(text="Назад", callback_data="back_dynamics_liquidity")
    )
    return markup


def long_row_balances():
    """Остатки средств на корсчетах и депозитах коммерческих банков (Кнопка "Длинный ряд")"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Среднее значение - месяц", callback_data="cd_long_res_month"),
        InlineKeyboardButton(text="Среднее значение - квартал", callback_data="cd_long_res_quarter"),
        InlineKeyboardButton(text="Среднее значение - год", callback_data="cd_long_res_year"),
        InlineKeyboardButton(text="Скользящая средняя - 22 дня", callback_data="cd_long_rol_month"),
        InlineKeyboardButton(text="Скользящая средняя - 67 дней", callback_data="cd_long_rol_quarter"),
        InlineKeyboardButton(text="Скользящая средняя - 247 дней", callback_data="cd_long_rol_year"),
        InlineKeyboardButton(text="Назад", callback_data="back_row_remaining")
    )
    return markup


def short_row_balances():
    """Остатки средств на корсчетах и депозитах коммерческих банков (Кнопка "Короткий ряд")"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Среднее значение - неделя", callback_data="cd_short_res_week"),
        InlineKeyboardButton(text="Среднее значение - месяц", callback_data="cd_short_res_month"),
        InlineKeyboardButton(text="Скользящая средняя - 5 дней", callback_data="cd_short_rol_week"),
        InlineKeyboardButton(text="Скользящая средняя - 22 дня", callback_data="cd_short_rol_month"),
        InlineKeyboardButton(text="Назад", callback_data="back_row_remaining")
    )
    return markup


def growth_markup():
    """Ежедневные приросты остатков средств на корсчетах и депозитах (кнопка "Ликвидные средства банков (приросты)")"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Длинный ряд", callback_data="growth_long"),
        InlineKeyboardButton(text="Короткий ряд", callback_data="growth_short"),
        InlineKeyboardButton(text="Назад", callback_data="back_dynamics_liquidity")
    )
    return markup


def long_row_growth():
    """Приросты средств банков - Длинный ряд"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Среднее значение - месяц", callback_data="growth_long_month_res"),
        InlineKeyboardButton(text="Среднее значение - квартал", callback_data="growth_long_quarter_res"),
        InlineKeyboardButton(text="Среднее значение - год", callback_data="growth_long_year_res"),
        InlineKeyboardButton(text="Скользящая средняя - 22 дня", callback_data="growth_long_month_rol"),
        InlineKeyboardButton(text="Скользящая средняя - 67 дней", callback_data="growth_long_quarter_rol"),
        InlineKeyboardButton(text="Скользящая средняя - 247 дней", callback_data="growth_long_year_rol"),
        InlineKeyboardButton(text="Назад", callback_data="back_growth_menu")
    )
    return markup


def short_row_growth():
    """Приросты средства банков - Короткий ряд"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Среднее значение - неделя", callback_data="growth_short_week_res"),
        InlineKeyboardButton(text="Среднее значение - месяц", callback_data="growth_short_month_res"),
        InlineKeyboardButton(text="Среднее значение - 5 дней", callback_data="growth_short_week_rol"),
        InlineKeyboardButton(text="Среднее значение - 22 дня", callback_data="growth_short_month_rol"),
        InlineKeyboardButton(text="Назад", callback_data="back_growth_menu")
    )
    return markup


def liquidity_factors_markup():
    """Таблица факторов банковской ликвидности"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Операции Казначейства и ЦБ", callback_data="treasury_operations"),
        InlineKeyboardButton(text="Валюта и наличные", callback_data="currency_cash"),
        InlineKeyboardButton(text="Все факторы", callback_data="all_factors"),
        InlineKeyboardButton(text="Назад", callback_data="back")
    )
    return markup


def treasury_operations_markup():
    """Операции Казначейства и ЦБ"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Длинный ряд", callback_data="treasury_operations_long_row"),
        InlineKeyboardButton(text="Короткий ряд", callback_data="treasury_operations_short_row"),
        InlineKeyboardButton(text="Назад", callback_data="back_factors_liquidity")
    )
    return markup


def treasury_operations_long_row():
    """Операции Казначейства и ЦБ - Длинный ряд"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Cумма операций за месяц", callback_data="sum_trans_month_long_res_chart"),
        InlineKeyboardButton(text="Cумма операций за квартал", callback_data="sum_trans_quarter_long_res_chart"),
        InlineKeyboardButton(text="Cумма операций за год", callback_data="sum_trans_year_long_res_chart"),

        InlineKeyboardButton(text="Скользящая средняя - 22 дня", callback_data="treasury_oper_long_rol_month_chart"),
        InlineKeyboardButton(text="Скользящая средняя - 67 дней", callback_data="treasury_oper_long_rol_quarter_chart"),
        InlineKeyboardButton(text="Скользящая средняя - 247 дней", callback_data="treasury_oper_long_rol_year_chart"),

        InlineKeyboardButton(text="Назад", callback_data="back_treasury_operations")
    )
    return markup


def treasury_operations_short_row():
    """Операции Казначейства и ЦБ - Короткий ряд"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Cумма операций за неделю", callback_data="sum_trans_week_short_res_chart"),
        InlineKeyboardButton(text="Cумма операций за месяц", callback_data="sum_trans_month_short_res_chart"),

        InlineKeyboardButton(text="Скользящая средняя - 5 дней", callback_data="treasury_oper_short_rol_week_chart"),
        InlineKeyboardButton(text="Скользящая средняя - 22 дня", callback_data="treasury_oper_short_rol_month_chart"),

        InlineKeyboardButton(text="Назад", callback_data="back_treasury_operations")
    )
    return markup


def currency_cash_transactions_markup():
    """Валютные и налично-денежные операции"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Длинный ряд", callback_data="currency_cash_transactions_long_row"),
        InlineKeyboardButton(text="Короткий ряд", callback_data="currency_cash_transactions_short_row"),
        InlineKeyboardButton(text="Назад", callback_data="back_factors_liquidity")
    )
    return markup


def currency_cash_transactions_long_row():
    """Валютные и налично-денежные операции (Длинный ряд)"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Cумма операций за месяц", callback_data="currency_cash_res_month_long_row"),
        InlineKeyboardButton(text="Cумма операций за квартал", callback_data="currency_cash_res_quarter_long_row"),
        InlineKeyboardButton(text="Cумма операций за год", callback_data="currency_cash_res_year_long_row"),
        InlineKeyboardButton(text="Cкользящая средняя - 22 дня", callback_data="currency_cash_rol_month_long_row"),
        InlineKeyboardButton(text="Cкользящая средняя - 67 дней", callback_data="currency_cash_rol_quarter_long_row"),
        InlineKeyboardButton(text="Cкользящая средняя - 247 дней", callback_data="currency_cash_rol_year_long_row"),
        InlineKeyboardButton(text="Назад", callback_data="back_currency_cash_transactions_markup")
    )
    return markup


def currency_cash_transactions_short_row():
    """Валютные и налично-денежные операции (Короткий ряд)"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Cумма операций за неделю", callback_data="currency_cash_res_week_short_row"),
        InlineKeyboardButton(text="Cумма операций за месяц", callback_data="currency_cash_res_month_short_row"),
        InlineKeyboardButton(text="Cумма операций за квартал", callback_data="currency_cash_res_quarter_short_row"),

        InlineKeyboardButton(text="Cкользящая средняя - 5 дней", callback_data="currency_cash_rol_week_short_row"),
        InlineKeyboardButton(text="Cкользящая средняя - 22 дня", callback_data="currency_cash_rol_month_short_row"),
        InlineKeyboardButton(text="Cкользящая средняя - 67 дней", callback_data="currency_cash_rol_quarter_short_row"),

        InlineKeyboardButton(text="Назад", callback_data="back_currency_cash_transactions_markup")
    )
    return markup


def all_factors_markup():
    """Все факторы"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Длинный ряд", callback_data="all_factors_long_row"),
        InlineKeyboardButton(text="Короткий ряд", callback_data="all_factors_short_row"),
        InlineKeyboardButton(text="Назад", callback_data="back_factors_liquidity")
    )
    return markup


def all_factors_long_row():
    """Все факторы - Длинный ряд"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Сумма операций за год", callback_data="all_factors_year_res_long"),
        InlineKeyboardButton(text="Скользящая средняя - 247 дней", callback_data="all_factors_year_rol_long"),
        InlineKeyboardButton(text="Назад", callback_data="back_all_factors_markup")
    )
    return markup


def all_factors_short_row():
    """Все факторы - Короткий ряд"""

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="Сумма операций за месяц", callback_data="all_factors_month_res_short"),
        InlineKeyboardButton(text="Скользящая средняя - 67 дней", callback_data="all_factors_quarter_rol_short"),
        InlineKeyboardButton(text="Назад", callback_data="back_all_factors_markup")
    )
    return markup