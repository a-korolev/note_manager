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


def print_notes(notes_list: list) -> None:
    """
    Функция выводит данные списка заметок.

    :param notes_list:  list - список заметок
    :return: None
    """
    print('\nТекущий список заметок:')
    print('-' * 80)

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
    print('Имя пользователя:', note['username'])
    print('Заголовок:', note['title'])
    print('Описание заметки:', note['content'])

    print('-' * 80)


def delete_note(notes_) -> dict:
    """
    Удаление заметок.

    :return: None
    """

    message = ''  # сообщение пользователю
    while True:
        # Вывод списка заметок
        print_notes(notes_)

        if message:
            print(f'\n{message}')

        # Ввод критерия для удаления заметок
        criteria = input(
            'Введите имя пользователя или заголовок для удаления заметки. Enter - выход в главное меню: ').strip().lower()

        # Если пустой ввод тогда выход
        if not criteria:
            break

        # Получение списка ID заметок попадающий под критерий поиска
        find_note_ids = find_note(criteria, notes_)

        if find_note_ids:
            while True:
                answer = input(
                    f'Критерий поиска "{criteria}": В списке найдено {len(find_note_ids)} {declension(len(find_note_ids))}. Вы уверены, что хотите их удалить? (да/нет): ').strip()
                if answer.lower() == 'да':
                    # Удаление заметок из списка в соответствии списка ID и сохранение обновленного списка
                    notes_ = delete_notes(find_note_ids, notes_)
                    message = f'Удалено {len(find_note_ids)} {declension(len(find_note_ids))}'
                    break
                elif answer.lower() == 'нет':
                    message = 'Список заказов не изменен.'
                    break

        else:
            message = f'Критерий поиска "{criteria}": Заметок с таким именем пользователя или заголовком не найдено.'

    return notes_


def delete_notes(find_note_ids: list, notes: list) -> list:
    """
    Удаляет заметки из списка по переданному списку ID

    :param find_note_ids: list - список ID
    :param notes: list - список заметок
    :return: новый список без удаленных заметок
    """
    new_notes = []

    for index, note in enumerate(notes):
        if index not in find_note_ids:
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
        if note['username'].lower() == criteria or note['title'].lower() == criteria:
            result.append(key)

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


if __name__ == '__main__':
    def print_welcome() -> None:
        """
        Вывод приветствия для пользователя.

        :return: None
        """
        print('\nДобро пожаловать в "Менеджер заметок"!')


    def print_goodbye() -> None:
        """
        Выводит финальное сообщение

        :return: None
        """
        print('До встречи!')


    # Список текущих заметок
    test_notes = [
        {
            'username': 'Иван',
            'title': 'Практика',
            'content': 'Обучение',
            'status': 'Активна',
            'created_date': '10-01-2025',
            'issue_date': '15-01-2025',
        },
        {
            'username': 'Петр',
            'title': 'Учеба',
            'content': 'Обучение',
            'status': 'Активна',
            'created_date': '26-12-2024',
            'issue_date': '26-10-2025',
        },
        {
            'username': 'Иван',
            'title': 'Путешествие',
            'content': 'Отдых',
            'status': 'Активна',
            'created_date': '01-01-2025',
            'issue_date': '08-01-2025',
        },
        {
            'username': 'Зинаида',
            'title': 'Учеба',
            'content': 'Школа',
            'status': 'Активна',
            'created_date': '01-09-2024',
            'issue_date': '25-12-2024',
        },
        {
            'username': 'Петр',
            'title': 'Спорт',
            'content': 'Отдых',
            'status': 'Активна',
            'created_date': '01-06-2025',
            'issue_date': '24-06-2025',
        },
    ]

    # Вывод приветствия
    print_welcome()
    # Основной цикл программы
    delete_note(test_notes)
    # Финальное сообщение
    print_goodbye()
