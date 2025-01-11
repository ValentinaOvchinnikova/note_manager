

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
