username = input('Как Вас зовут?\n')
title_result = []
while True:
    title = input(
        'Введите заголовок заметки (или напишите "Стоп" если хотите завершить)\n')  # Пользователь вводит заголовки заметки
    if title.lower() == 'стоп':  # если заголовков больше нет пользователь вводит "стоп" и цикл останавливается, программа продолжает свою последовательную работу
        break
    if title == '':  # Если пользователь оставляет пустой ввод то происходит перебрасывание на новый заголовок оставляя предыдущий пустым
        continue
    title_result.append(title)  # добавляет заголовки в список
    title_result = list(set(title_result))  # не дает повторов заголовков
content = input('Введите описание задачи\n')
current_status = 'В процессе'  # исходный статус заметки
print(f"Текущий статус заметки:\n{current_status}")
print("Выберите статус заметки:", "\n"
                                  '1. Выполнено', '\n'
                                                  '2. В процесce', '\n'
                                                                   '3. Отложено',
      '\n')  # Предлагает пользователю выбрать из списка статус
status_options = {
    '1': 'выполнено',
    '2': 'в процессе',  # Нужно для цикла
    '3': 'отложено'}
while True:
    choice = input('Ваш выбор(номер статуса):')
    if choice in status_options:
        current_status = status_options[choice]
        print(f'Статус заметки обновлен на:\n{current_status}')  # Запрашивает у пользователя номер статуса
        break
    else:
        print(
            'Некорректный выбор. Пожалуйста выберите 1, 2 или 3')  # Если статус введен некорректно запрашивает его еще раз
created_date = input('Введите сегодняшнее число дд/мм/гг:\n')

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
note = [
    username,
    title_result,
    content,
    current_status,
    created_date,
    issue_date]
print('Собранные данные от пользователя:', "\n",
      'Имя пользователя:', note[0], "\n",
      'Список заголовков заметки:', *note[1], "\n",
      'Описание задачи:', note[2], "\n",
      'Статус заметки:', note[3], "\n",
      'Дата создания заметки:', note[4], "\n",
      'Дата истечения заметки:', note[5], "\n")
