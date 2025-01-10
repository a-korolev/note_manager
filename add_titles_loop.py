"""add_titles_loop.py
Grade 1. Этап 2. Задание 1.
Работа с циклами и условиями.

Функциональность:
Запрашивает у пользователя заголовки.
Позволяет завершить ввод специальной командой или пустым вводом.
Выводит итоговый список добавленных заголовков.
"""

# Константы ESC-последовательностей стилей консольного вывода
# TODO: move constants to a separate file
C_RED_STYLE = '\033[31m'
C_RED2_STYLE = '\033[91m'
C_GREEN_STYLE = '\033[32m'
C_GREEN2_STYLE = '\033[92m'
C_YELLOW_STYLE = '\033[33m'
C_YELLOW2_STYLE = '\033[93m'
C_BLUE_STYLE = '\033[34m'
C_BLUE2_STYLE = '\033[94m'
C_VIOLET_STYLE = '\033[35m'
C_VIOLET2_STYLE = '\033[95m'
C_BEIGE_STYLE = '\033[36m'
C_BEIGE2_STYLE = '\033[96m'
C_WHITE_STYLE = '\33[37m'
C_WHITE2_STYLE = '\33[97m'
C_END_STYLE = '\033[0m'
C_BOLD_STYLE = '\033[1m'
C_ITALIC_STYLE = '\33[3m'
C_UNDERLINE_STYLE = '\033[4m'
C_BLINK_STYLE = '\33[5m'
C_BLINK2_STYLE = '\33[6m'

# Константы сообщений
# TODO: move constants to a separate file
C_INPUT_TITLES = 'Ввод заголовков заметки:'
C_INPUT_TITLE = f'Введите заголовок (введите \'{C_WHITE2_STYLE}стоп{C_END_STYLE}\'' \
                'или оставьте пустым для завершения: '
C_ALREADY_EXIST_TITLE = 'Внимание! Такой заголовок уже существует. Повторите ввод.'
C_INPUT_END = 'Ввод завершен.'
C_OUTPUT_TITLES = 'Введенные заголовки заметки:'

# Константы
# TODO: move constants to a separate file
C_EMPTY_STRING = ''
C_STOP_WORD = 'стоп'

# Инициализация переменных
titles = []
title = ''

# Ввод заголовков в цикле
print(f'{C_VIOLET_STYLE}{C_INPUT_TITLES}{C_END_STYLE}')

while True:
    title = input(f'{C_INPUT_TITLE}').strip()

    # Проверка на ввод завершающий цикл
    if title.lower() in (C_EMPTY_STRING, C_STOP_WORD):
        break

    # Проверка на уникальность введенного заголовка
    if title in titles:
        print(f'{C_YELLOW2_STYLE}{C_ALREADY_EXIST_TITLE}{C_END_STYLE}')
        continue

    # Добавление введенного заголовка в список
    titles.append(title)

print(f'{C_BLUE_STYLE}{C_INPUT_END}{C_END_STYLE}')

# Вывод списка введенных заголовков
print(f'\n{C_VIOLET_STYLE}{C_OUTPUT_TITLES}{C_END_STYLE}')

for title in titles:
    print(f'- {title}')
