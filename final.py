username=input('Как Вас зовут?') # Имя пользователя:
title1=input('Введите первый заголовок заметки:') # Заголовок заметки:
title2=input('Введите второй заголовок заметки')
title3=input('Введите третий заголовок заметки')
title_result=[title1,title2,title3]
content=input('Введите описание задачи') # Описание заметки:
status=input('Вы завершили задачу? ')# Статус заметки:
created_date = input('Введите сегодняшнее число дд/мм/гг:')  # Дата создания заметки:
issue_date = input('Введите дату дедлайна дд/мм/гг:')  # Дата истечения заметки:

note=[
      username,
      title_result,
      content,
      status,
      created_date,
      issue_date]
print('Собранные данные от пользователя',"\n"
      'Имя пользователя:', note[0],"\n",
      'Список заголовков заметки:', note[1],"\n",
      'Описание задачи:', note[2],"\n",
      'Статус заметки:', note[3],"\n",
      'Дата создания заметки:', note[4],"\n",
      'Дата истечения заметки:', note[5],"\n")