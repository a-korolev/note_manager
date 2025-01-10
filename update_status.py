"""update_status.py
Grade 1. Этап 2. Задание 2.
Проверка и обновление статуса заметки.

Функциональность:
Показывает текущий статус заметки.
Предлагает изменить статус на один из предложенных.
Обрабатывает некорректный ввод.
"""

# Кортеж содержащий возможные статусы заметки
statuses = ('В процессе', 'Отложено', 'Выполнено')

# Создание и инициализация словаря для хранения данных заметки
note = {
    'username': 'Королев Андрей',
    'titles': ['Подготовка', 'Решение', 'Сдача'],
    'content': 'Выполнение и сдача задания "Базовые переменные для заметок".',
    'status': statuses[0],
    'created_date': '26-12-2024',
    'issue_date': '09-01-2025',
}


def print_current_note_status(note: dict) -> None:
    """
    Вывод текущего статуса заметки

    :param: note: dict - Словарь содержащий данные заметки
    :return: None
    """
    print(f'Текущий статус заметки: {note['status']}')


def print_status_menu() -> None:
    """
    Вывод меню выбора нового статуса заметки

    :return: None
    """
    print('Выберите новый статус заметки. Для отмены изменения статуса выберите \'0\' или нажмите Enter:')
    for key, status in enumerate(statuses):
        print(f'{key + 1}. {status}')
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
        if selected_status == '':
            selected_status = 0
            break
        if selected_status.isdigit():
            if int(selected_status) <= len(statuses):
                selected_status = int(selected_status)
                break
        elif selected_status.replace(' ', '').isalnum():
            if selected_status in statuses:
                selected_status = statuses.index(selected_status) + 1
                break

        print_status_menu()
        print(f'Выбран некорректный статус. Введите номер статус или его название из списка {str(statuses)}.')

    return selected_status


def set_note_status(status: int) -> None:
    """
    Устанавливает новый статус в заметке

    :param status: int - Порядковый номер статуса в кортеже
    :return: None
    """
    note['status'] = statuses[status - 1]


def print_update_status_result(status: int) -> None:
    """
    Вывод нового статуса заметки.

    :param status: int - Номер статуса. 0 - если ввод статуса был отменен
    :return:
    """
    if status > 0:
        print(f'Статус заметки изменен на: {note['status']}')
    else:
        print('Статус заметки не изменен')


# Вывод текущего статуса заметки
print_current_note_status(note)

# Вывод меню для выбора нового статуса
print_status_menu()

# Выбор статуса из меню
new_status = select_note_status()

# Изменение статуса заметки
set_note_status(new_status)

# Вывод результата выбора изменения статуса
print_update_status_result(new_status)
