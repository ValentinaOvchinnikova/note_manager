username = input('Как Вас зовут?\n')
title_result = []
while True:
    title = input('Введите заголовок заметки (или напишите "Стоп" если хотите завершить)\n') #Пользователь вводит заголовки заметки
    if title.lower() == 'стоп': #если заголовков больше нет пользователь вводит "стоп" и цикл останавливается, программа продолжает свою последовательную работу
        break
    if title=='': #Если пользователь оставляет пустой ввод то происходит перебрасывание на новый заголовок оставляя предыдущий пустым
        continue
    title_result.append(title) # добавляет заголовки в список
    title_result=list(set(title_result)) # не дает повторов заголовков
content = input('Введите описание задачи\n')  # Описание заметки:
status = input('Вы завершили задачу?\n')  # Статус заметки:
created_date = input('Введите сегодняшнее число дд/мм/гг:\n')  # Дата создания заметки:
issue_date = input('Введите дату дедлайна дд/мм/гг:\n')  # Дата истечения заметки:

note = [
    username,
    title_result,
    content,
    status,
    created_date[0:5],
    issue_date[:5]]
print('Собранные данные от пользователя:', "\n",
      'Имя пользователя:', note[0], "\n",
      'Список заголовков заметки:', *note[1], "\n",
      'Описание задачи:', note[2], "\n",
      'Статус заметки:', note[3], "\n",
      'Дата создания заметки:', note[4], "\n",
      'Дата истечения заметки:', note[5], "\n")




