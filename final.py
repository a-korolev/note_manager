# final.py

username = input('Ваше имя: ')
title1 = input('Введите заголовок 1 заметки: ')
title2 = input('Введите заголовок 2 заметки: ')
title3 = input('Введите заголовок 3 заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки (ДД.ММ.ГГГ): ')
issue_date = input('Ввндите дату истечения заметки (ДД.ММ.ГГГ): ')

title = [title1, title2, title3]

note = [
    username,
    title,
    content,
    status,
    created_date,
    issue_date
]

print(note)
