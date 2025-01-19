"""menu.py
Grade 1. Этап 3. Задание 5.
Функция меню действий

Функциональность:
Отображает список доступных действий.
Выполняет выбранное пользователем действие, вызывая соответствующую функцию.
Повторно показывать меню после завершения действия, пока пользователь не выберет выход.
"""
from colorama import init, Fore
from constants import C_DATE_FORMAT
from create_note_function import create_note
from update_note_function import update_note, display_note
from display_notes_function import display_notes
from search_notes_function import search_notes
from delete_note import delete_note

# Алиас типа для списка заметок
type Notes = list[dict[str | str] | dict[str, str]]


def menu(notes: Notes):
    init(autoreset=True)

    while True:
        print(f'\n\t{Fore.BLUE}Менеджер заметок.')
        print(f'\n\t{Fore.CYAN}Меню действий:')
        print(f'\t{Fore.YELLOW}1.{Fore.RESET} Создать новую заметку')
        print(f'\t{Fore.YELLOW}2.{Fore.RESET} Показать все заметки')
        print(f'\t{Fore.YELLOW}3.{Fore.RESET} Обновить заметку')
        print(f'\t{Fore.YELLOW}4.{Fore.RESET} Удалить заметку')
        print(f'\t{Fore.YELLOW}5.{Fore.RESET} Найти заметки')
        print(f'\t{Fore.YELLOW}6.{Fore.RESET} Выйти из программы')

        user_choice = input(f'\n{Fore.CYAN}Выберите действие (введите цифру от 1 до 6): ').strip()

        if user_choice == '6':
            break

        if user_choice.isdigit() and int(user_choice) in range(1, 6):

            match user_choice:
                case '1':
                    note = create_note()
                    if note:
                        print(f'{Fore.GREEN}Заметка создана.')
                        notes.append(note)
                    # display_notes(notes, full_mode=False)
                case '2':
                    display_notes(notes, full_mode=True)
                case '3':
                    note_count = len(notes)
                    while True:
                        user_choice = input(f'{Fore.CYAN}Введите номер заметки для обновления или Enter для выхода: ').strip()
                        if not user_choice:
                            break
                        if user_choice.isdigit() and 0 < int(user_choice) <= note_count:
                            note_for_update = notes[int(user_choice) - 1]
                            display_note(note_for_update, C_DATE_FORMAT)
                            update_note(note_for_update)
                            display_note(note_for_update, C_DATE_FORMAT)
                            break

                case '4':
                    notes = delete_note(notes)
                case '5':
                    keyword = input(f'{Fore.CYAN}Введите ключевое слово для поиска заметок или Enter для выхода: ').strip()
                    status = input(f'{Fore.CYAN}Введите статус для поиска заметок или Enter для выхода: ').strip()

                    result_notes = search_notes(notes, keyword, status)
                    display_notes(result_notes, full_mode=True)
                case _:
                    print(f'{Fore.RED}Что-то пошло не так...')

        else:
            print(f'{Fore.RED}Неверный выбор. Пожалуйста, выберите действие из списка.')

    print(f'{Fore.BLUE}Программа завершена. Спасибо за использование!')


if __name__ == '__main__':
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

    menu(notes_list)
