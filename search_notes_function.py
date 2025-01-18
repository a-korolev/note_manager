"""display_note_function.py
Grade 1. Этап 3. Задание 4.
Функция поиска заметок

Функциональность:
Функция корректно обрабатывает пустой список заметок.
Успешно выполняется поиск по ключевым словам.
Успешно выполняется поиск по статусу.
Успешно выполняется комбинированный поиск (по ключевому слову и статусу).
Возможность поиска с нечувствительностью к регистру.
"""

import re

# Алиас типа для списка заметок
type Notes = list[dict[str | str] | dict[str, str]]


def search_notes(notes: Notes, keyword: str = None, status: str = None):
    result = []

    # Если передан пустой список возвращаем пустой список поиска. Искать негде.
    if not notes:
        return result

    # Если не переданы критерии поиска возвращаем переданный список. Искать нечего.
    if not keyword and not status:
        return notes

    """ Поиск заметок с заданным статусом без учета регистра при помощи filter и lambda функции.
    Если статусом поиска задан, присваиваем список найденных заметок в результат для дальнейшего поиска.
    Иначе в результат присваиваем исходный список для поиска.   
    """
    if status:
        result = list(filter(lambda note: note['status'].lower() == status.lower(), notes))
    else:
        result = notes

    """ Поиск вхождения строкового значения keyword при помощи filter и lambda функции в списке словарей заметок по ключевым словам
    в полях переданных списком search_fields с нечувствительностью регистра.
    """
    if keyword and result:
        # Кортеж с ключами полей поиска
        search_fields = ('username', 'title', 'content')

        result = list(
            filter(lambda note: [x for x in [x.lower() for x in [note.get(key) for key in search_fields]]
                                 if re.search(keyword.lower(), x)
                                 ], result
                   )
        )

    return result


if __name__ == '__main__':
    from display_notes_function import display_notes

    notes_list: Notes = [
        {
            'username': 'Иван',
            'title': 'Учеба',
            'content': 'Обучение',
            'status': 'Активна',
            'created_date': '10-01-2025',
            'issue_date': '15-01-2025',
        },
        {
            'username': 'Петр',
            'title': 'Практика',
            'content': 'Обучение',
            'status': 'Новая',
            'created_date': '26-12-2024',
            'issue_date': '26-10-2025',
        },
        {
            'username': 'Иван',
            'title': 'Рыбалка',
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

    result_notes = search_notes(notes_list, keyword='пеТр', status='активНа')

    display_notes(result_notes, full_mode=True, notes_per_page=0)
