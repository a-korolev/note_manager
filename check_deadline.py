"""check_deadline.py
Grade 1. Этап 2. Задание 3.
Проверка истечения срока выполнения задачи.

Запрашивает дату дедлайна и сравнивает её с текущей датой.
Сообщает, истёк ли дедлайн или сколько дней осталось.
Проверяет корректность формата ввода.

Формат даты задается константой C_DATE_FORMAT
"""
from datetime import date
from datetime import datetime

C_DATE_FORMAT: str = '%d-%m-%Y'


def get_current_date() -> datetime:
    """
    Получение текущей даты с отсечением значения времени до 00:00:00

    :return: datetime - значения текущей даты
    """
    today_date = datetime.today().replace(minute=0, hour=0, second=0, microsecond=0)
    return today_date


def print_current_date() -> None:
    """
    Вывод текущей даты в заданном формате константой C_DATE_FORMAT

    :return: None
    """
    print(f'Текущая дата: {current_date.strftime(C_DATE_FORMAT)}')


def input_date() -> datetime:
    """
    Ввод и обработка пользовательского ввода даты дедлайна.

    :return: datetime: дата введенная пользователем
    """
    is_valid_date = False
    input_date = ''
    while not is_valid_date:
        input_date = input(
            f'Введите дату дедлайна (в формате {replace_format_string_to_word(C_DATE_FORMAT)}): ').strip()
        is_valid_date = validate_date_format(input_date, C_DATE_FORMAT)
        if not is_valid_date:
            print(
                f'Убедитесь, что вводите дату в формате {replace_format_string_to_word(C_DATE_FORMAT)}, например: {get_current_date().strftime(C_DATE_FORMAT)}')

    return datetime.strptime(input_date, C_DATE_FORMAT)


def validate_date_format(date_text: str, date_format: str) -> bool:
    """
    Проверка соответствия даты заданному формату.

    Функция возвращает True, если строка соответствует переданному формату, иначе False

    :param date_text: str - дата в строковом представлении
    :param date_format: str - строка с форматом
    :return: bool - True если текст даты соответствует формату, иначе False
    """
    try:
        if date_text != datetime.strptime(date_text, date_format).strftime(date_format):
            raise ValueError
        return True
    except ValueError:
        return False


def replace_format_string_to_word(format_string: str) -> str:
    """
    Замена в строке подстрок подстроками заданными в словаре.

    :param format_string: str - строка в которой необходимо сделать замену
    :return: str - строка с произведенными заменами
    """
    replace_values = {'%d': 'день', '%m': 'месяц', '%Y': 'год', '%y': 'год'}
    for i, j in replace_values.items():
        format_string = format_string.replace(i, j)
    return format_string


def calc_days_between_dates(date1: date, date2: date) -> int:
    """
    Расчет разницы между текущей датой и датой дедлайна и вывод соответствующего сообщения.

    :param date1: date - Дата1
    :param date2: date - Дата2
    :return: int - Количество дней между датами
    """
    return (date2 - date1).days


def declension(number: int, one: str = 'день', four: str = 'дня', five: str = 'дней') -> str:
    """
    Возврат окончания слова при склонении

    Функция возвращает окончание слова, в зависимости от примененного к ней числа
    Например: 5 товаров, 1 товар, 3 товара

    :param number: int - число, к которому необходимо применить склонение
    :param one: str - слово в именительном падеже
    :param four: str - слово в родительном падеже
    :param five: str - слово в родительном падеже множ. числа
    :return: str - слово в соответствующем падеже number
    """
    result = five
    number = abs(number) % 100
    if number < 11 or number > 19:
        number = number % 10
        if number == 1:
            result = one
        if 2 <= number <= 4:
            result = four
    return result


def print_result(days_between) -> None:
    """
    Выводит сообщение с результатом проверки.

    :param days_between:
    :return: None
    """
    if days_between < 0:
        print(f'Внимание! Дедлайн истёк {abs(days_between)} {declension(abs(days_between))} назад.')
    elif days_between > 0:
        print(f'До дедлайна осталось {days_between} {declension(days_between)}.')
    else:
        print(f'Дедлайн сегодня!')


# Получение текущей даты
current_date = get_current_date()

# Вывод текущей даты в формате
print_current_date()

# Ввод даты окончания заметки пользователем
issue_date = input_date()

# Расчет разницы между текущей датой и датой дедлайна и вывод соответствующего сообщения.
days_between = calc_days_between_dates(current_date, issue_date)

# Выводит сообщение с результатом проверки.
print_result(days_between)
