"""constants.py
Константы
"""

C_DATE_FORMAT: str = '%d-%m-%Y'
C_DATE_NOTE_PRINT_FORMAT: str = '%d-%m'
C_INPUT_TITLES = 'Ввод заголовков заметки:'
C_INPUT_TITLE = f'Введите заголовок (введите \'стоп\'' \
                'или оставьте пустым для завершения: '
C_ALREADY_EXIST_TITLE = 'Внимание! Такой заголовок уже существует. Повторите ввод.'
C_EMPTY_STRING = ''
C_STOP_WORD = 'стоп'

# Кортеж содержащий возможные статусы заметки
C_NOTE_STATUSES = ('Новая', 'В процессе', 'Отложена', 'Выполнена')