"""multiple_notes.py
Grade 1. Этап 2. Задание 4.
Работа с несколькими заметками.

Функциональность:
Создаёт несколько заметок через ввод данных (имя, заголовок, описание, статус, дату создания, дедлайн).
Присваивает уникальный ID для новой заметки в списке.
Хранит заметки в списке словарей.
Выводит список всех заметок.
"""

from datetime import datetime

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

# Список для сохранения заметок
notes = []
# Кортеж содержащий возможные статусы заметки
statuses = ('Активна', 'В процессе', 'Отложена', 'Выполнена')


def print_welcome() -> None:
    """
    Вывод приветствия для пользователя.

    :return: None
    """
    print('\nДобро пожаловать в "Менеджер заметок"!')


def input_notes() -> list:
    """
    Функция для ввода и сохранения заметок в списке.

    :return: notes: list - список созданных заметок
    """
    is_input_another_note = 'да'

    while is_input_another_note == 'да':
        print('\nВы можете добавить новую заметку.')
        note = create_note()
        notes.append(note)

        while True:
            is_input_another_note = input('Хотите добавить ещё одну заметку? (да/нет): ').strip().lower()
            if is_input_another_note in ('нет', 'да'):
                break
            else:
                continue
    return notes


def input_username() -> str:
    """
    Ввод имени пользователя.

    Проверка на пустой ввод
    :return: result: str - Возвращает введенное имя пользователя
    """
    result = ''
    while not result:
        result = input('Введите имя пользователя: ').strip()
        if not result:
            print('Имя пользователя не может быть пустым')
    return result


def input_titles() -> list:
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


def input_content() -> str:
    """
    Ввод описания заметки

    Проверка на пустой ввод
    :return: result: str - Возвращает введенное описание заметки
    """
    result = ''
    while not result:
        result = input('Введите описание заметки: ').strip()
        if not result:
            print('Описание заметки не может быть пустым')
    return result


def print_status_menu(statuses_tuple) -> None:
    """
    Вывод меню выбора нового статуса заметки

    :param statuses_tuple: tuple - кортеж с возможными значениями статусов
    :return: None
    """
    print('Выберите статус заметки. Для статуса по умолчанию \'Активна\' нажмите Enter:')
    for key, status in enumerate(statuses_tuple):
        print(f'{key + 1}. {status}')


def select_note_status(statuses_tuple: tuple) -> int:
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
        print_status_menu(statuses_tuple)

    return selected_status


def input_status(statuses_tuple) -> int:
    """
    Функция вывода меню для выбора статуса и ввод выбранного значения.

    :param statuses_tuple: tuple - кортеж с возможными значениями статусов
    :return: status: int - индекс статуса
    """
    print_status_menu(statuses_tuple)
    return select_note_status(statuses_tuple)


def input_date(subtitle: str = '') -> datetime:
    """
    Ввод и обработка пользовательского ввода даты.

    :param subtitle: str - подзаголовок даты
    :return: datetime: дата введенная пользователем
    """
    is_valid_date = False
    input_date = ''
    while not is_valid_date:
        input_date = input(
            f'Введите дату {subtitle} (в формате {replace_format_string_to_word(C_DATE_FORMAT)}): ').strip()
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


def get_unique_note_id(notes: list) -> int:
    """
    Находит в списке заметок заметку с максимальным ID и возвращает значение с инкрементом 1

    :param notes: Список заметок
    :return: result: int - уникальный ID в списке заметок
    """
    result = 0

    for value in notes:
        if value['ID'] > result:
            result = value['ID']
    return result + 1


def create_note() -> dict:
    """
    Функция ввода данных и создания словаря заметки

    :return: dict - словарь содержащий данные созданной заметки
    """
    id = get_unique_note_id(notes)
    username = input_username()
    titles = input_titles()
    content = input_content()
    status = statuses[input_status(statuses)]
    created_date = input_date('создания заметки')
    issue_date = input_date('истечения заметки')

    # Создание и инициализация списка для хранения данных заметки
    note = {
        'ID': id,
        'username': username,
        'titles': titles,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date,
    }
    return note


def print_notes(notes_list: list):
    """
    Функция выводит данные списка заметок.

    :param notes_list:  list - список заметок
    :return: None
    """
    print_notes_title()
    for note in notes_list:
        print_note(note, C_DATE_NOTE_PRINT_FORMAT)


def print_note(note: dict, date_format: str):
    """
    Выводит данные заметки.

    :param note: dict - словарь содержащий данные заметки
    :param date_format: str - формат даты
    :return: None
    """
    print('ID:', note['ID'])
    print('Имя пользователя:', note['username'])
    print('Заголовки заметки:')

    # Вывод списка заголовков в цикле
    for index, title in enumerate(note['titles']):
        print(f'\tЗаголовок {index + 1}: {title}')

    print('Описание заметки:', note['content'])
    print('Статус заметки:', note['status'])
    print('Дата создания заметки:', note['created_date'].strftime(date_format))  # Вывод даты создания
    print('Дата истечения заметки:', note['issue_date'].strftime(date_format))  # Вывод даты истечения
    print('-' * 60)


def print_notes_title() -> None:
    """
    Функция выводит заголовок списка заметок

    :return: None
    """
    print('\nСписок заметок:')
    print('-' * 60)


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


if __name__ == '__main__':
    # Вывод приветствия для пользователя.
    print_welcome()

    # Ввод и сохранения заметок в списке.
    notes = input_notes()

    # Вывод данных заметок в списке.
    print_notes(notes)
