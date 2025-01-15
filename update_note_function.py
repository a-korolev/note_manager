"""update_note_function.py
Grade 1. Этап 3. Задание 2.
Функция обновления заметки.

Функциональность:
Функция корректно принимает заметку в качестве аргумента.
Пользователь может выбрать поле для обновления.
Поле обновляется с учётом корректности введённого значения (например, проверка формата для даты).
Возвращается обновлённый словарь заметки.
"""
from datetime import datetime

# Константы
C_DATE_FORMAT: str = '%d-%m-%Y'

# Словарь с данными заметки
note = {
    'username': 'Иван',
    'title': 'Отдых',
    'content': 'Путешествие, рыбалка, экскурсии',
    'status': 'Активна',
    'created_date': '01-01-2025',
    'issue_date': '08-01-2025',
}

note_fields_updated = {}

# Кортеж содержащий возможные статусы заметки
statuses = ('Отменить ввод', 'Активна', 'В процессе', 'Отложено', 'Выполнено')


def get_user_input_end():
    global note
    if note_fields_updated:
        while True:
            user_answer = get_user_confirm_update()
            if user_answer == 'нет':
                print('\nЗаметка не обновлена.')
                break
            elif user_answer == 'да':
                print('\nЗаметка обновлена')
                note |= note_fields_updated
                break

    else:
        print('\nНет полей для обновления. Заметка не обновлена.')


def get_user_confirm_update():
    user_answer = input('Вы уверены, что хотите обновить поля заметки? (да/нет): ').strip().lower()
    return user_answer

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


def get_user_input_username():
    return get_user_input('Введите имя пользователя: ')


def get_user_input_title():
    return get_user_input('Введите заголовок: ')


def get_user_input_content():
    return get_user_input('Введите содержание: ')


def get_user_input_satus():
    result = ''
    # Вывод меню для выбора нового статуса
    print_status_menu()

    # Выбор статуса из меню
    status_id = select_note_status()

    if status_id == 0:
        return ''
    else:
        return statuses[status_id]


def get_user_input_issue_date() -> str:
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

    return input_date


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


def get_current_date() -> datetime:
    """
    Получение текущей даты с отсечением значения времени до 00:00:00

    :return: datetime - значения текущей даты
    """
    today_date = datetime.today().replace(minute=0, hour=0, second=0, microsecond=0)
    return today_date


def print_status_menu() -> None:
    """
    Вывод меню выбора нового статуса заметки

    :return: None
    """
    print('Выберите новый статус заметки. Для отмены изменения статуса выберите \'0\' или нажмите Enter:')
    for key in range(1, len(statuses)):
        print(f'{key}. {statuses[key]}')
    print('0. Отменить ввод')


def select_note_status() -> int:
    """
    Обработка выбранного статуса заметки.

    Делает проверку на ввод только разрешенных статусов.
    Позволяет выбрать статус по номеру (1, 2, 3...) или по названию ('В процессе', 'Отложено', 'Выполнено')
    :return: selected_status: int - Возвращает номер выбранного статуса. 0 если ввод отменен.
    """
    while True:
        selected_status = input('Ваш выбор: ').strip()
        #if selected_status == '' or selected_status == '0':
        if selected_status == '0':
            selected_status = 0
            break
        if selected_status.isdigit():
            if int(selected_status) < len(statuses):
                selected_status = int(selected_status)
                break
        elif selected_status.replace(' ', '').isalnum():
            if selected_status in statuses:
                selected_status = statuses.index(selected_status)
                break

        print_status_menu()
        print(f'Выбран некорректный статус. Введите номер статус или его название из списка {str(statuses)}.')

    return selected_status


note_fields = [
    {'field_code': 'input_end', 'field_title': 'Сохранить изменения и выйти', 'field_input_fn': get_user_input_end},
    {'field_code': 'username', 'field_title': 'Имя пользователя', 'field_input_fn': get_user_input_username},
    {'field_code': 'title', 'field_title': 'Заголовок', 'field_input_fn': get_user_input_title},
    {'field_code': 'content', 'field_title': 'Содержание', 'field_input_fn': get_user_input_content},
    {'field_code': 'status', 'field_title': 'Статус', 'field_input_fn': get_user_input_satus},
    {'field_code': 'issue_date', 'field_title': 'Дата дедлайна', 'field_input_fn': get_user_input_issue_date}
]


def display_note(note: dict, date_format: str):
    """
    Выводит данные заметки.

    :param note: dict - словарь содержащий данные заметки
    :param date_format: str - формат даты
    :return: None
    """
    print('\nЗаметка')
    print('-' * len('Заметка'))
    print('Имя пользователя:', note['username'])
    print('Заголовок:', note['title'])
    print('Описание заметки:', note['content'])
    print('Статус заметки:', note['status'])
    # print('Дата создания заметки:', note['created_date'].strftime(date_format))  # Вывод даты создания
    # print('Дата истечения заметки:', note['issue_date'].strftime(date_format))  # Вывод даты истечения
    print('Дата создания заметки:', note['created_date'])  # Вывод даты создания
    print('Дата истечения заметки:', note['issue_date'])  # Вывод даты истечения

    print('-' * 60)
    print()


def display_update_fields_menu(note_fields):
    """
    Вывод меню выбора поле заметки для обновления

    :param statuses_tuple: tuple - кортеж с возможными значениями статусов
    :return: None
    """
    print(f'Список полей заметки для обновления')
    print('-' * len('Список поле заметки для обновления'))

    for index in range(1, len(note_fields)):  # enumerate(note_fields):
        field = note_fields[index]
        print(f'{index}. {field['field_code']} ({field['field_title']})')

    index = 0
    field = note_fields[index]
    print(f'{index}. {field['field_title']}')  # {field['field_code']}')

    # for key, value in note_fields.items():
    #     print(f'{key}. {value}')


# def test():
#     print('test_fn')
# test_fn = test
# test_fn_arr = [test_fn, test_fn]

def get_user_choice_field():
    # note_fields_selected = []
    result = 0

    while not result:
        user_choice = input('Для обновления данных, выберите поле (введите номер или название поле): ').strip()

        #if user_choice == '' or user_choice == '0':
        if user_choice == '0':
            break
        if user_choice.isdigit():
            if int(user_choice) < len(note_fields):
                result = int(user_choice)
                break
        elif user_choice.replace(' ', '').isalnum():
            for key, note_field in enumerate(note_fields):
                if note_field['field_code'].lower() == user_choice.lower():
                    result = key
                    break

    return result


def update_note(note):
    #note_fields_updated = {}

    while True:
        display_update_fields_menu(note_fields)
        user_choice_field = get_user_choice_field()
        # print(user_choice, type(user_choice))
        user_choice_data = note_fields[user_choice_field]['field_input_fn']()

        if user_choice_field == 0:
            break
        elif user_choice_data:
            note_fields_updated[note_fields[user_choice_field]['field_code']] = user_choice_data
            #print(note_fields_updated)
            #note |= note_fields_updated
        # else:
        #     break

    return note


if __name__ == '__main__':
    print('\nОбновление заметки')

    # Вывод данных заметки до обновления
    display_note(note, C_DATE_FORMAT)
    # Обновление заявки
    note = update_note(note)
    # Вывод данных заметки после обновления
    display_note(note, C_DATE_FORMAT)
