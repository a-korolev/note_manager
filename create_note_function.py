"""create_note_function.py
Grade 1. Этап 3. Задание 1.
Функция создания заметки.

Функциональность:
Создание заметки на основе введенных пользователем данных в виде словаря
Автоматически добавляет текущую дату в поле created_date
Проверка правильности ввода даты заданному формату реализована отдельной функцией
Проверка на заполнение обязательных полей недопускающих пустой ввод
При пустом вводе даты дедлайна добавляет заданное количество дней от текущей даты
Выбор статуса из фиксированного списка по номеру в меню или по названию
"""

from datetime import datetime
from datetime import timedelta

# Константы
# TODO: move constants to a separate file
C_DATE_FORMAT: str = '%d-%m-%Y'
C_DATE_NOTE_PRINT_FORMAT: str = '%d-%m'
C_INPUT_TITLES = 'Ввод заголовков заметки:'
C_INPUT_TITLE = f'Введите заголовок (введите \'стоп\'' \
                'или оставьте пустым для завершения: '
C_ALREADY_EXIST_TITLE = 'Внимание! Такой заголовок уже существует. Повторите ввод.'
C_EMPTY_STRING = ''
C_STOP_WORD = 'стоп'

# Кортеж содержащий возможные статусы заметки
statuses = ('Новая', 'В процессе', 'Отложена', 'Выполнена')


def get_user_input(label: str = 'Введите данные: ') -> str:
    """
    Ввод имени пользователя.

    Проверка на пустой ввод
    :param label: str - заголовок для ввода
    :return: result: str - Возвращает введенное имя пользователя
    """
    result = ''
    while not result:
        result = input(label).strip()
        if not result:
            print('Это поле не может быть пустым')
    return result


def get_user_input_titles() -> list:
    """
    Функция ввода заголовков и возврат их в списке.
    Производит контроль на "дубли".

    :return: titles: list - список введенных заголовков
    """
    # Инициализация переменных
    titles = []

    # Ввод заголовков в цикле
    print(f'{C_INPUT_TITLES}')

    while True:
        title = input(f'{C_INPUT_TITLE}').strip()

        # Проверка на ввод завершающий цикл
        if title.lower() in (C_EMPTY_STRING, C_STOP_WORD):
            if len(titles) == 0:
                print('Введите минимум один заголовок.')
                continue
            else:
                break

        # Проверка на уникальность введенного заголовка
        if title in titles:
            print(f'{C_ALREADY_EXIST_TITLE}')
            continue

        # Добавление введенного заголовка в список
        titles.append(title)

    return titles


def get_user_input_status(statuses_tuple) -> int:
    """
    Функция вывода меню для выбора статуса и ввод выбранного значения.

    :param statuses_tuple: tuple - кортеж с возможными значениями статусов
    :return: status: int - индекс статуса
    """
    display_status_menu(statuses_tuple)
    return get_user_select_note_status(statuses_tuple)


def display_status_menu(statuses_tuple: tuple) -> None:
    """
    Вывод меню выбора нового статуса заметки

    :param statuses_tuple: tuple - кортеж с возможными значениями статусов
    :return: None
    """
    print(f'Выберите статус заметки. Для ввода статуса по умолчанию \'{statuses[0]}\' нажмите Enter:')
    for key, status in enumerate(statuses_tuple):
        print(f'{key + 1}. {status}')


def get_user_select_note_status(statuses_tuple: tuple) -> int:
    """
    Функция ввода и выбранного для обработки статуса заметки.

    :param statuses_tuple: tuple - кортеж с возможными значениями статусов
    :return: selected_status: int - индекс выбранного статуса
    """

    while True:
        selected_status = input('Ваш выбор: ').strip()

        if selected_status.isdigit():
            if 1 <= int(selected_status) <= len(statuses_tuple):
                selected_status = int(selected_status) - 1
                break
        elif selected_status.replace(' ', '').isalnum():
            if selected_status in statuses_tuple:
                selected_status = statuses.index(selected_status)
                break

        print('Некорректный ввод статуса. Выберите номер статуса или введите его название.')
        display_status_menu(statuses_tuple)

    return selected_status


def get_user_input_date(subtitle: str = '', is_default_input_allowed: bool = False,
                        offset_days_value: int = 0) -> datetime:
    """
    Ввод и обработка пользовательского ввода даты.

    :param subtitle: str - подзаголовок даты
    :param is_default_input_allowed: bool - делать проверку при пустом вводе. Нет по умолчанию
    :param offset_days_value: int - смещение от текущей даты в днях
    :return: datetime: дата введенная пользователем
    """
    is_valid_date = False
    input_date = ''
    while not is_valid_date:
        input_date = input(
            f'Введите дату {subtitle} (в формате {replace_format_string_to_word(C_DATE_FORMAT)}): ').strip()

        if is_default_input_allowed:
            input_date = (get_current_date() + timedelta(offset_days_value)).strftime(C_DATE_FORMAT)
            is_valid_date = True
        else:
            is_valid_date = validate_date_format(input_date, C_DATE_FORMAT)

        if not is_valid_date:
            print(
                f'Убедитесь, что вводите дату в формате {replace_format_string_to_word(C_DATE_FORMAT)}, '
                f'например: {get_current_date().strftime(C_DATE_FORMAT)}')

    return datetime.strptime(input_date, C_DATE_FORMAT)


def get_current_date() -> datetime:
    """
    Получение текущей даты с отсечением значения времени до 00:00:00

    :return: datetime - значения текущей даты
    """
    today_date = datetime.today().replace(minute=0, hour=0, second=0, microsecond=0)
    return today_date


def validate_date_format(date_text: str, date_format: str) -> bool:
    """
    Проверка соответствия даты заданному формату.

    Функция возвращает True, если строка соответствует переданному формату, иначе False

    :param date_text: str - дата в строковом представлении
    :param date_format: str - строка с форматом
    :return: bool
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


def create_note() -> dict:
    """
    Функция ввода данных и создания словаря заметки

    :return: dict - словарь содержащий данные созданной заметки
    """
    print('Ввод новой заметки\n')

    # Ввод данных заметки пользователем
    username = get_user_input('Введите имя пользователя: ')
    titles = get_user_input_titles()
    content = get_user_input('Введите описание заметки: ')
    status = statuses[get_user_input_status(statuses)]
    created_date = get_current_date()
    issue_date = get_user_input_date('дедлайна', True, 7)

    # Создание и инициализация словаря для хранения данных заметки
    note = {
        'username': username,
        'titles': titles,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date,
    }
    return note


if __name__ == '__main__':
    # Создание новой заметки
    new_note = create_note()

    # Вывод данных словаря новой заметки
    print(new_note)
