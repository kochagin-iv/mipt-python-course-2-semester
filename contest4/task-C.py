'''
Напишите декоратор @takes, который будет проверять правильность типов входных аргументов функции.
Декоратор принимает на вход типы аргументов и декорирует функцию таким образом, что она генеририрует исключение TypeError, если хотя бы один из аргументов имеет неверный тип.
Если аргументов больше, чем типов, то ошибку генерировать не нужно (возможно, точный тип известен только для первых аргументов, его, как раз, надо проверить).
Если типов больше, чем аргументов, то это тоже ошибка только в случае, если переданные аргументы не подходят под соответствующие им по порядку типы. (декоратор может быть применен к функциям с переменным числом аргументов).

Декоратор должен вести себя порядочно, то есть не должен затирать основные аргументы функции (__name__, __doc__, __module__).

Для простоты можно считать, что у функции нет именованных аргументов.

Генерацию исключений воспринимайте пока как волшебный способ просигнализировать об ошибке. Делается это так: raise TypeError

Формат ввода
Ваш код должен иметь такой вид:

import sys

...

ваши импорты и реализация

декоратор должен называться "takes"

...

exec(sys.stdin.read())

(Программа выполнит код, записанный во входном файле)

Пример 1
Ввод
# this is for similar behaviour in python 2 and python 3
from __future__ import print_function


@takes(int, str)
def f(a, b):
    print(a, b)

try:
    f(1, 'abcd')
except Exception as e:
    print(type(e).__name__)

Вывод
1 abcd

Пример 2
Ввод
# this is for similar behaviour in python 2 and python 3
from __future__ import print_function


@takes(int, str)
def f(a, b):
    print(a, b)
    
try:
    f(1, 2)
except Exception as e:
    print(type(e).__name__)

Вывод
TypeError
'''

import sys
import functools


def takes(*args1):
    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args2):
            iter1 = args1.__iter__()
            iter2 = args2.__iter__()
            print(args1, args2, file=sys.stderr)
            try:
                elem1 = next(iter1)
            except StopIteration:
                return func(*args2)
            try:
                elem2 = next(iter2)
            except StopIteration:
                return func(*args2)

            while 1:
                if not isinstance(elem2, elem1):
                    raise TypeError
                try:
                    elem1 = next(iter1)
                except StopIteration:
                    return func(*args2)
                try:
                    elem2 = next(iter2)
                except StopIteration:
                    return func(*args2)

        return wrapper

    return wraps


exec(sys.stdin.read())

