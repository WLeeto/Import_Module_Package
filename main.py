from application.db.people import get_employees
from application.salary import calculate_salary
import datetime as dt
from colorama import Fore, Back, Style

if __name__ == '__main__':
    now = dt.datetime.now()

    print(Fore.GREEN + f'\nТекущая дата: {now.day}.{now.month}.{now.year}')
    print(f'Текущее время {now.hour}:{now.minute}\n')

    # другой способ:
    now_2 = now.strftime("%H:%M %d-%m-%Y")
    print(Back.YELLOW, Fore.BLACK + f'Текущее время и дата: {now_2}')
    print(Back.RESET)
    print(Style.BRIGHT)
    get_employees()
    calculate_salary()
    print(Style.RESET_ALL, Back.RESET)

    print('Пример работы tkinter: https://github.com/WLeeto/MagicBall')
    print('Пример работы BeautifulSoup: https://github.com/WLeeto/BeautifulSoup')
    print('colorama использована в текущем модуле')
