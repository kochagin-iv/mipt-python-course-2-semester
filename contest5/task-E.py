'''
Вам дан неизвестный файл import_me.py. Он лежит в одной директории с вашим решением. Решите задачу, импортировав его.

Решение должно иметь имя solution.py.

Подсказка: функция help() недоступна, хотя она пригодилась бы. Чем бы её можно заменить?

И загляните в лог компиляции, когда ваше решение будет падать, там может оказаться что-то полезное :)

В этой задаче выбирайте компилятор Make, в остальных – Python.
'''

import import_me
from inspect import getmembers, isfunction


def get_all_functions():
    ans = []
    for key, value in getmembers(import_me, isfunction):
        ans.append(key)
    return ans

