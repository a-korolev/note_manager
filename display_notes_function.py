"""display_note_function.py
Grade 1. Этап 3. Задание 3.
Функция отображения заметок.

Функциональность:
Функция корректно обрабатывает пустой список заметок.
Заметки выводятся в указанном формате, с номерами и разделителями.
Вывод удобен для чтения.
"""

import math
from colorama import init, Fore
from datetime import datetime

type Notes = list[dict[str | str] | dict[str, str]]

C_DATE_FORMAT: str = '%d-%m-%Y'


def display_notes(notes: Notes, full_mode: bool = True, sort_field_name: str = '', sort_reverse: bool = False,
                  notes_per_page: int = 0) -> None:
    """
    Функция вывода текущего списка заметок

    Функциональность:
    Функция корректно обрабатывает пустой список заметок.
    Реализована поддержка цветного вывода.
    Заметки выводятся в указанном формате только заголовки или полные данные, с номерами и разделителями.
    Позволяет сортировать список с указанием направления и поля сортировки.
    Поддерживает вывод заметок в формате таблицы.
    Возможность постраничного вывода.

    :param notes: Список заметок для вывода
    :param full_mode: Формат вывода. True (по умолчанию) - полные данные. False - только заголовки.
    :param sort_field_name: Имя поля для сортировки (по умолчанию без сортировки).
    :param sort_reverse: Направление сортировки (по умолчанию по возрастанию).
    :param notes_per_page: Количество страниц на странице. 0 - постраничный вывод отключен.
    :return: None
    """
    init(autoreset=True)

    print(f'\n{Fore.BLUE}Текущий список заметок:')
    print('-' * 80)

    # Сортировка списка если указано поле
    if sort_field_name:
        if sort_field_name == 'created_date' or sort_field_name == 'issue_date':
            notes_list.sort(key=lambda field: datetime.strptime(field[sort_field_name], C_DATE_FORMAT),
                            reverse=sort_reverse)
        else:
            notes_list.sort(key=lambda field: field[sort_field_name], reverse=sort_reverse)

    # Значения и переменные для постраничного ввода
    notes_per_page = abs(notes_per_page)
    current_note_per_page_counter = notes_per_page
    current_page_counter = 1
    if notes_per_page != 0:
        page_count = math.ceil(len(notes) / notes_per_page)
    else:
        page_count = 0

    if len(notes) > 0:
        for key, note in enumerate(notes, start=1):

            print(f'{Fore.YELLOW}Заметка №{key}:')

            if full_mode:
                print(f'{'Имя пользователя:':18}{Fore.CYAN}{note.get('username', f'{Fore.RED}<не определено>')}')
                print(f'{'Заголовок:':18}{Fore.CYAN}{note.get('title', f'{Fore.RED}<не определено>')}')
                print(f'{'Описание:':18}{Fore.CYAN}{note.get('content', f'{Fore.RED}<не определено>')}')
                print(f'{'Статус:':18}{Fore.CYAN}{note.get('status', f'{Fore.RED}<не определено>')}')
                print(f'{'Дата создания:':18}{Fore.CYAN}{note.get('created_date', f'{Fore.RED}<не определено>')}')
                print(f'{'Дедлайн:':18}{Fore.CYAN}{note.get('issue_date', f'{Fore.RED}<не определено>')}')
            else:
                print(f'{'Заголовок:':11}{Fore.CYAN}{note.get('title', f'{Fore.RED}<не определено>')}')

            print('-' * 80)

            current_note_per_page_counter -= 1

            if key < len(notes) and current_note_per_page_counter == 0:
                input(f'Страница [{current_page_counter}/{page_count}] Нажмите Enter для продолжения...')
                current_note_per_page_counter = notes_per_page
                current_page_counter += 1

        if notes_per_page != 0:
            print(f'Страница [{current_page_counter}/{page_count}]')

    else:
        print('У вас нет сохранённых заметок.')


if __name__ == '__main__':
    # Список текущих заметок
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
            'status': 'Активна',
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

    # Вызов функции отображения заметок
    display_notes(notes_list, full_mode=True, sort_field_name='created_date', sort_reverse=False, notes_per_page=2)
