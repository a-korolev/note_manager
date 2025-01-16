"""display_note_function.py
Grade 1. Этап 3. Задание 3.
Функция отображения заметок.

Функциональность:
Функция корректно обрабатывает пустой список заметок.
Заметки выводятся в указанном формате, с номерами и разделителями.
Вывод удобен для чтения.
"""


def display_notes(notes: list = None):
    if notes is None:
        notes = []

    if notes:
        for note in notes:
            display_note(note)
    else:
        print('У вас нет сохранённых заметок.')


def display_note(note: dict) -> None:
    """
    Выводит данные заметки.

    :param note: dict - словарь содержащий данные заметки
    :return: None
    """
    print(f'Заметка №{note['ID']}:')
    print('Имя пользователя:', note.get('username', '<не определено>'))
    print('Заголовок:', note.get('title', '<не определено>'))
    print('Описание:', note.get('content', '<не определено>'))
    print('Статус:', note.get('status', '<не определено>'))
    print('Дата создания:', note.get('created_date', '<не определено>'))
    print('Дедлайн:', note.get('issue_date', '<не определено>'))
    print('-' * 80)


if __name__ == '__main__':
    # Список текущих заметок
    notes = [
        {
            'ID': 1,
            'username': 'Иван',
            'title': 'Учеба',
            'content': 'Обучение',
            'status': 'Активна',
            'created_date': '10-01-2025',
            'issue_date': '15-01-2025',
        },
        {
            'ID': 2,
            'username': 'Петр',
            'title': 'Практика',
            'content': 'Обучение',
            'status': 'Активна',
            'created_date': '26-12-2024',
            'issue_date': '26-10-2025',
        },
        {
            'ID': 3,
            'username': 'Иван',
            'title': 'Рыбалка',
            'content': 'Отдых',
            'status': 'Активна',
            'created_date': '01-01-2025',
            'issue_date': '08-01-2025',
        },
        {
            'ID': 4,
            'username': 'Зинаида',
            'title': 'Учеба',
            'content': 'Школа',
            'status': 'Активна',
            'created_date': '01-09-2024',
            'issue_date': '25-12-2024',
        },
        {
            'ID': 5,
            'username': 'Петр',
            'title': 'Спорт',
            'content': 'Отдых',
            'status': 'Активна',
            'created_date': '01-06-2025',
            'issue_date': '24-06-2025',
        },
    ]


    def print_notes_title() -> None:
        """
        Функция выводит заголовок списка заметок

        :return: None
        """
        print('\nТекущий список заметок:')
        print('-' * 80)

    print_notes_title()
    display_notes(notes)
