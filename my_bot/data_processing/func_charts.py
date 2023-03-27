import pandas
import datetime
import requests
from bs4 import BeautifulSoup
from datetime import date
import matplotlib.pyplot as plt


def get_data_raw(url, param=None):
    """парсим данные цб и возвращаем объект BeautifulSoup"""

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/"
                  "signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru, en-GB,en-US;q=0.9, en;q=0.8",
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/83.0.4103.97 Safari/537.36",
        }

    site = requests.get(url, params=param, headers=headers)
    return BeautifulSoup(site.text, 'lxml')


# получаем таблицу данных
def get_data_table(days):
    data = []
    for day in days:
        vals = day.findAll('td')
        if vals:
            d = []
            for val in vals:
                x = val.text if val.text != ' — ' else 0
                d = d + [x]
            data = data + [d]
    return data


# создаем объект datetime из строки даты
def as_date(c):
    return c.apply(func=lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"))


# приводим число к типу float64
def as_float(c):
    return c.apply(lambda x: x.replace(',', '.').replace(' ', '')).astype('float64')


start_date = date(2023, 1, 1).strftime('%d.%m.%Y')  # начало 2023 года
today_date = date.today().strftime('%d.%m.%Y')  # сегодняшняя дата
params = {'UniDbQuery.Posted': 'True', 'UniDbQuery.From': start_date, 'UniDbQuery.To': today_date}


# Депозиты DA
def deposits():
    url = r'https://cbr.ru/hd_base/ostat_depo_new/'
    soup = get_data_raw(url, params)
    data = reversed([list(map(lambda elem: elem.replace(",", ".") if isinstance(elem, str) else elem, line))
                     for line in get_data_table(soup.find(name='div', class_='table').findAll('tr'))])

    columns = ['Date', 'DA', 'Depo7', 'Depo30', 'DepoUT']
    deposits_pd = pandas.DataFrame(data=data, columns=columns, dtype='string')  # создание экзмеляра класса т-цы пандас
    deposits_pd["Date"] = as_date(deposits_pd["Date"])  # создаем объект datetime который становится datetime64[ns]
    deposits_pd["DA"] = as_float(deposits_pd["DA"]) / 1000  # меняем тип данных на float64 и делим на 1000
    deposits_pd = deposits_pd.iloc[:, 0:2]  # вырезаем из таблицы два первых столбца
    deposits_pd.index = deposits_pd.Date  # делаем дату индексом
    deposits_pd.drop(columns='Date', inplace=True)  # удаляем столбец даты
    return deposits_pd.sort_index()  # сортируем индексы


# # Корреспондентские счета CA
def corr_accounts():
    url = r'https://cbr.ru/hd_base/ostat_base/'
    soup = get_data_raw(url, params)
    data = get_data_table(soup.find('div', class_='table').findAll('tr'))
    corr = pandas.DataFrame(data=data, columns=['Date', 'CA', 'CA_Moscow'], dtype='string')  # создаем таблицу
    corr["Date"] = as_date(corr["Date"])  # меняем тип данных даты на datetime64[ns]
    corr["CA"] = as_float(corr["CA"])  # меняем тип данных на float64
    corr = corr.iloc[:, 0:2]  # вырезаем из таблицы два первых столбца
    corr.index = corr["Date"]  # делаем дату индексом
    corr.drop(columns='Date', inplace=True)  # удаляем столбец даты
    return corr.sort_index()  # сортируем индексы


# Ликвидность банковского сектора Cash
def liquidity_factors():
    url = r'https://www.cbr.ru/statistics/flikvid/'
    soup = get_data_raw(url, params)
    data = get_data_table(soup.find('div', class_='table').find('tbody').findAll('tr'))
    columns = ['Date', 'Cash', 'Tresor', 'SDebt', 'SDepo', 'SRepo', 'SCurrency', 'BCurrency', 'BSaldo']
    liquidity = pandas.DataFrame(data=data, columns=columns, dtype='string')  # создаем таблицу
    liquidity["Date"] = as_date(liquidity["Date"])  # меняем тип данных даты на datetime64[ns]

    for word in columns[1:]:
        liquidity[word] = as_float(liquidity[word])  # меняем тип данных на float64

    liquidity.index = liquidity["Date"]
    liquidity.drop(columns=["Date"], inplace=True)
    return liquidity.sort_index()  # сортируем индексы


# объединение таблиц корреспондентских счетов и депозитов
def correspondent_and_deposits():
    corr_dep = pandas.concat(objs=[corr_accounts(), deposits()], axis="columns", join='inner').sort_index()
    corr_dep["DA-Delta"] = -corr_dep['DA'].diff(periods=-1)  # Первое дискретное различие элемента.
                                                # Вычисляет разницу элемента по сравнению с другим элементом в столбце
                                                # (по умолчанию используется элемент в предыдущей строке).
    corr_dep["DA-Delta"] = corr_dep["DA-Delta"].fillna(value=0)  # Заполниние значения NA/NaN указанным методом.
    corr_dep["CA-Delta"] = -corr_dep["CA"].diff(periods=-1)
    corr_dep["CA-Delta"] = corr_dep["CA-Delta"].fillna(0)
    return corr_dep


# объединение таблиц "ликвидность банковского сектора" и "кор.счета-депозиты" в новую таблицу
def new_table():
    new = pandas.concat(objs=[liquidity_factors(), correspondent_and_deposits()], axis="columns", join='inner')
    new["Debt"] = new["SDebt"] + new["SDepo"] + new["SRepo"]
    new["Budjet"] = new["Tresor"] - new["Debt"] - new["SCurrency"]
    new["Currency"] = new["SCurrency"] + new["BCurrency"]
    new["CB"] = new["BSaldo"] + new["DA-Delta"]
    new["FL-All"] = new["Cash"] + new["Tresor"] + new["BCurrency"] + new["CB"]
    return new


# получаем старую таблицу данных
def old_table():
    old = pandas.read_excel("my_bot/data_processing/data_2017-CD.xlsx",
                            sheet_name="Data")  # читаем эксель файл
    old = old[old["Date"] < start_date]  # выбираем те даты, которые меньше стартовой (начало 2023 года)
    old.index = old["Date"]
    old.drop(["Date"], axis="columns", inplace=True)
    return old


long_row = pandas.concat([old_table(), new_table()]).sort_index()  # объединяем старую и новую спаршенную таблицы
# создаем объект записи для записи данных в excel. Указываем "overlay" в if_sheet_exists= для добавления данных к сущ-им
with pandas.ExcelWriter(path="my_bot/data_processing/data_2017-CD.xlsx",
                        mode="a", if_sheet_exists="overlay") as writer_object:
    long_row.to_excel(excel_writer=writer_object, sheet_name="Data")

short_row = long_row[long_row.index > '2021-12-31']  # получаем таблицу начиная с 2022 года (короткая таблица)


"""__________________________________________Динамика банковской ликвидности_________________________________________"""

"""__________________________________________Ликвидные средства банков (остатки)_____________________________________"""


# для вывода графига - plt.show()
# resample() - выборка по фиксированным отрезкам, mean() - среднее значение, plot - создает график, area - его заполняет
def remains_res_chart(row, period):
    box_period = {"W": "неделя", "M": "месяц", "Q": "квартал", "Y": "год"}
    """Среднее значение по календарному периоду (неделя - W, месяц - M, квартал - Q, год - Y)
    на длинном или коротком ряду"""
    object_axes = row.loc[:, ["CA", "DA"]].resample(period).mean().plot.area()
    object_axes.set_title("Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                          f"\nСреднее значение - {box_period[period]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


# Скользящее среднее значение по месяцам (22), кварталам (67), годам (247) (банковским)
# rolling() - вывод интервала с захватом предыдущих значений, указанных в скобках.
def remains_rol_chart(row, days):
    """Скользящее среднее значение по дням, на длинном или коротком ряду"""
    box_days = {5: "дней", 22: "дня", 67: "дней", 247: "дней"}
    object_axes = row.loc[:, ["CA", "DA"]].rolling(days).mean().plot.area()
    object_axes.set_title("Остатки средств на корсчетах и депозитах коммерческих банков в ЦБ"
                          f"\nСкользящая средняя - {days} {box_days[days]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


"""__________________________________________Ликвидные средства банков (приросты)____________________________________"""


# С начала 2017 года по настоящее время.
# Приросты остатков средств за месяц, квартал, год (календарный)
# plot - рисует график, area - заполняет, stacked=True\False - зап-ие графика по одну\по обе стороны коор-ой. прямой
def growth_res_chart(row, period):
    """Приросты остатков средств за календарный период (неделя - W, месяц -M, квартал - Q, год - Y)
    на длинном или коротком ряду"""
    box_period = {"W": "неделя", "M": "месяц", "Q": "квартал", "Y": "год"}
    object_axes = row.loc[:, ["CA-Delta", "DA-Delta"]].resample(period).sum().plot.area(stacked=False)
    object_axes.set_title("Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                          f"\nСреднее значение - {box_period[period]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


# Приросты остатков средств за период до текущей даты – месяц (22), квартал, год
# скользящая средняя
def growth_rol_chart(row, days):
    """Скользящая средняя приростов остатков средств по дням, на длинном или коротком ряду"""
    box_days = {5: "дней", 22: "дня", 67: "дней", 247: "дней"}
    object_axes = row.loc[:, ["CA-Delta", "DA-Delta"]].rolling(days).sum().plot.area(stacked=False)
    object_axes.set_title("Приросты остатков средств на корсчетах и депозитах коммерческих банков в ЦБ"
                          f"\nСкользящая средняя - {days} {box_days[days]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


"""______________________________________Факторы ликвидности банковского сектора_____________________________________"""

"""_____________________________________________Операции Казначейства и ЦБ___________________________________________"""


def treasury_rol_chart(row, days):
    """Скользящая средняя - по дням, на длинном или коротком ряду"""
    box_days = {5: "дней", 22: "дня", 67: "дней", 247: "дней"}
    object_axes = row.loc[:, ["Budjet", "Debt", "CB"]].rolling(days).mean().plot.area(stacked=False)
    object_axes.set_title("Операции Казначейства и ЦБ Российской Федерации"
                          f"\nСкользящая средняя - {days} {box_days[days]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


def sum_trans_res_chart(row, period):
    """Cумма операций за календарный период (неделя - W, месяц -M, квартал - Q, год - Y)
    на длинном или коротком ряду"""
    box_period = {"W": "неделю", "M": "месяц", "Q": "квартал", "Y": "год"}
    object_axes = row.loc[:, ['Budjet', 'Debt', 'CB']].resample(period).sum().plot.area(stacked=False)
    object_axes.set_title("Операции Казначейства и ЦБ Российской Федерации"
                          f"\nСумма операций за {box_period[period]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


"""_______________________________________________Валюта и наличные__________________________________________________"""


def currency_cash_res_chart(row, period):
    """Cумма операций за календарный период (неделя - W, месяц -M, квартал - Q, год - Y)
    на длинном или коротком ряду"""

    box_period = {"W": "неделю", "M": "месяц", "Q": "квартал", "Y": "год"}
    object_axes = row.loc[:, ['Cash', 'Currency']].resample(period).sum().plot(linewidth=3.0)
    object_axes.set_title("Валютные и налично денежные операции"
                          f"\nСумма операций за {box_period[period]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


def currency_cash_rol_chart(row, days):
    """Скользящая средняя валютных и налично денежных операций - по дням
    на длинном или коротком ряду"""

    box_days = {5: "дней", 22: "дня", 67: "дней", 247: "дней"}
    object_axes = row.loc[:, ['Cash', 'Currency']].rolling(days).mean().plot(linewidth=3.0)
    object_axes.set_title("Валютные и налично денежные операции"
                          f"\nСкользящая средняя - {days} {box_days[days]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


"""__________________________________________________Все факторы_____________________________________________________"""


def all_factors_res_area_chart(row, period):
    """Сумма операций за календарный период (неделя - W, месяц -M, квартал - Q, год - Y)
    на длинном или коротком ряду c заливкой"""

    box_period = {"W": "неделю", "M": "месяц", "Q": "квартал", "Y": "год"}
    obj_axes = row.loc[:, ['Budjet', 'Debt', 'CB', 'Cash', 'Currency']].resample(period).sum().plot.area(stacked=False)
    obj_axes.set_title("Все факторы"
                       f"\nСумма операций за {box_period[period]}", fontsize=20)
    figure = obj_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


def all_factors_res_bar_chart(row, period):
    """Сумма операций за календарный период (неделя - W, месяц -M, квартал - Q, год - Y)
    на длинном или коротком ряду bar()"""

    box_period = {"W": "неделю", "M": "месяц", "Q": "квартал", "Y": "год"}
    obj_axes = row.loc[:, ['Budjet', 'Debt', 'CB', 'Cash', 'Currency']].resample(period).sum().plot.bar()
    obj_axes.set_title("Все факторы"
                       f"\nСумма операций за {box_period[period]}", fontsize=20)
    figure = obj_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"


def all_factors_rol_chart(row, days):
    """Скользящая средняя - по дням на длинном или коротком ряду"""

    box_days = {5: "дней", 22: "дня", 67: "дней", 247: "дней"}
    object_axes = row.loc[:, ['Budjet', 'Debt', 'CB', 'Cash', 'Currency']].rolling(days).mean().plot(linewidth=3.0)
    object_axes.set_title("Все факторы"
                          f"\nСкользящая средняя - {days} {box_days[days]}", fontsize=20)
    figure = object_axes.get_figure()
    figure.set_size_inches(12.5, 7.5)
    plt.savefig("graf.png")
    plt.close()
    return "graf.png"
