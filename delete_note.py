"""delete_note.py
Grade 1. Этап 2. Задание 5.
Удаление заметок.

Функциональность:
Удаляет заметки по имени пользователя или заголовку.
Удаление нескольких заметок по совпадающему критерию поиска.
Поиск нечувствителен к регистру.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.
"""

# Список текущих заметок
notes = [
    {
        'ID': 1,
        'username': 'Иван',
        'titles': ['Учеба', 'Практика', 'Тестирование'],
        'content': 'Обучение',
        'status': 'Активна',
        'created_date': '10-01-2025',
        'issue_date': '15-01-2025',
    },
    {
        'ID': 2,
        'username': 'Петр',
        'titles': ['Учеба', 'Практика', 'Тестирование'],
        'content': 'Обучение',
        'status': 'Активна',
        'created_date': '26-12-2024',
        'issue_date': '26-10-2025',
    },
    {
        'ID': 3,
        'username': 'Иван',
        'titles': ['Путешествие', 'Рыбалка', 'Экскурсии'],
        'content': 'Отдых',
        'status': 'Активна',
        'created_date': '01-01-2025',
        'issue_date': '08-01-2025',
    },
    {
        'ID': 4,
        'username': 'Зинаида',
        'titles': ['Учеба', 'Уроки'],
        'content': 'Школа',
        'status': 'Активна',
        'created_date': '01-09-2024',
        'issue_date': '25-12-2024',
    },
    {
        'ID': 5,
        'username': 'Петр',
        'titles': ['Спорт', 'Пляж'],
        'content': 'Отдых',
        'status': 'Активна',
        'created_date': '01-06-2025',
        'issue_date': '24-06-2025',
    },
]


def print_welcome() -> None:
    """
    Вывод приветствия для пользователя.

    :return: None
    """
    print('\nДобро пожаловать в "Менеджер заметок"!')


def print_notes_title() -> None:
    """
    Функция выводит заголовок списка заметок

    :return: None
    """
    print('\nТекущий список заметок:')
    print('-' * 60)


def print_notes(notes_list: list) -> None:
    """
    Функция выводит данные списка заметок.

    :param notes_list:  list - список заметок
    :return: None
    """
    print_notes_title()

    if len(notes_list) > 0:
        for note in notes_list:
            print_note(note)
    else:
        print('-- список не содержит заметок --')


def print_note(note: dict) -> None:
    """
    Выводит данные заметки.

    :param note: dict - словарь содержащий данные заметки
    :return: None
    """
    print('ID:', note['ID'])
    print('Имя пользователя:', note['username'])
    print('Заголовки заметки:')

    # Вывод списка заголовков в цикле
    for index, title in enumerate(note['titles']):
        print(f'\tЗаголовок {index + 1}: {title}')
    print('Описание заметки:', note['content'])

    print('-' * 60)


def get_delete_criteria() -> str:
    """
    Ввод критерия поиска

    :return: Result: str - возврат введенного критерия
    """
    result = input('Введите имя пользователя или заголовок для удаления заметки. Enter - выход из программы: ')
    return result


def main_loop(notes) -> None:
    """
    Основной цикл программы

    :return: None
    """

    message = ''  # сообщение пользователю
    while True:
        # Вывод списка заметок
        print_notes(notes)

        if message:
            print(f'\n{message}')

        # Ввод критерия для удаления заметок
        criteria = get_delete_criteria().strip().lower()

        # Если пустой ввод тогда выход
        if not criteria:
            break

        # Получение списка ID заметок попадающий под критерий поиска
        find_note_ids = find_note(criteria, notes)

        if find_note_ids:
            while True:
                answer = input(
                    f'Критерий поиска "{criteria}": В списке найдено {len(find_note_ids)} {declension(len(find_note_ids))}. Вы уверены, что хотите их удалить? (да/нет): ').strip()
                if answer.lower() == 'да':
                    # Удаление заметок из списка в соответствии списка ID и сохранение обновленного списка
                    notes = delete_notes(find_note_ids, notes)
                    message = f'Удалено {len(find_note_ids)} {declension(len(find_note_ids))}'
                    break
                elif answer.lower() == 'нет':
                    message = 'Список заказов не изменен.'
                    break

        else:
            message = f'Критерий поиска "{criteria}": Заметок с таким именем пользователя или заголовком не найдено.'


def delete_notes(find_note_ids: list, notes: list) -> list:
    """
    Удаляет заметки из списка по переданному списку ID

    :param find_note_ids: list - список ID
    :param notes: list - список заметок
    :return: новый список без удаленных заметок
    """
    new_notes = []

    for index, note in enumerate(notes):
        if note['ID'] not in find_note_ids:
            new_notes.append(note)

    return new_notes


def find_note(criteria: str, notes: str) -> list:
    """
    Производит поиск заметок в списке по заданному критерию.
    Поиск по имени пользователя и заголовкам.

    Не чувствительна к регистру
    :param criteria: str - критерий поиска
    :param notes: str - список заметок
    :return: list: Возвращает список ID найденных заметок
    """
    result = []
    for key, note in enumerate(notes):
        if note['username'].lower() == criteria or criteria in list(map(str.lower, note['titles'])):
            result.append(note['ID'])

    return result


def declension(number: int, one: str = 'заметка', four: str = 'заметки', five: str = 'заметок') -> str:
    """
    Возврат слова при склонении

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


def print_goodbye() -> None:
    """
    Выводит финальное сообщение

    :return: None
    """
    print('До встречи!')


if __name__ == '__main__':
    # Вывод приветствия
    print_welcome()
    # Основной цикл программы
    main_loop(notes)
    # Финальное сообщение
    print_goodbye()
