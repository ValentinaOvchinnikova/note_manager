
def vvod():
    notes = []
    while True:
        print('Добро пожаловать в "Менеджер заметок".\n',
              'Создание новой заметки\n')

        username = input('Введите имя пользователя:\n')
        title = input('Введите заголовок заметки:\n')
        content = input('Введите описание задачи:\n')
        status_options = {
    '1': 'выполнено',
    '2': 'в процессе',
    '3': 'отложено'}
        while True:
            print('\n')
            for [valye, key] in status_options.items():
                print(f'{valye}: {key}')
            choice = input('Ваш выбор(номер статуса):')
            if choice in status_options:
                current_status = status_options[choice]
                print(f'Статус заметки обновлен на:\n{current_status}')  # Запрашивает у пользователя номер статуса
                break
            else:
                print(
                    'Некорректный выбор. Пожалуйста выберите 1, 2 или 3')
        created_date = input('Введите сегодняшнее число дд-мм-гг:\n')
        from datetime import datetime
        from sys import exception
        from time import strptime

        while True:

            try:
                issue_date = input('Введите дату дедлайна дд-мм-гг:\n')
                issue_date = datetime.strptime(issue_date, "%d-%m-%y").date()
                current_datetime = datetime.now().date()

                if issue_date < current_datetime:
                    print('Дедлайн истек!')
                elif issue_date > current_datetime:
                    different_date = (issue_date - current_datetime).days
                    print(f'До дедлайна осталось {different_date} дней!')
                else:
                    print('Дедлайн сегодня!')

                break
            except ValueError:
                print('Некорректный формат даты')

        note = {'Имя': username,
                'Заголовок': title,
                'Описание': content,
                'Статус': current_status,
                'Дата создания': created_date,
                'Дата дедлайна': issue_date}
        notes.append(note)
        continue_choice=input('Хотите добавить ещё одну заметку? (да/стоп)\n')
        if continue_choice == 'стоп':
            break
    print('Список всех созданных заметок:\n')
    for i, note in enumerate(notes, start=1):
        print(f'Заметка {i}:')
        for key, value in note.items():
            print(f'{key}:{value}')
    return notes
result_notes = vvod()



def delete_notes(notes):
    delete_choice = input('Введите имя пользователя или заголовок для удаления заметки:\n').strip() #для ввода строк
    delete1_choice = len(notes)
    # Для того чтобы удалить заметку по двум путям: имя пользователя или заголовок
    notes [:] = [note for note in notes if note['Имя'] != delete_choice and note['Заголовок'] != delete_choice]
    if len(notes) < delete1_choice:
        print(f'Успешно удалено. Остались доступны следующие заметки: {notes}')
    else:
        print('Заметок с таким именем пользователя или заголовком не найдено.')
    if notes:
        print('Оставшиеся заметки:\n')
    for i, note in enumerate(notes, start=1):
        print(f'Заметка {i}:')
        for key, value in note.items():
            print(f'{key}: {value}')
    else:
        print('Вы удалили все заметки')
    return result_notes
print(delete_notes(notes=result_notes))