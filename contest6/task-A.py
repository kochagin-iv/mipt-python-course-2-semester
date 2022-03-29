'''
Напишите класс, который является расширением стандартного класса list. Сделайте так, чтобы, помимо обычных атрибутов в нем присутствовали такие:

reversed (с коротким псевдонимом R), который содержит тот же список, но с элементами в обратном порядке.
first (с коротким псевдонимом F), который содержит первый элемент списка. Должна присутствовать возможность изменять этот атрибут (и вместе с ним должен меняться и сам список). Атрибут не обязан работать корректно, если список пустой.
last (с коротким псевдонимом L), который содержит последний элемент списка. Должна присутствовать возможность изменять этот атрибут (и вместе с ним должен меняться и сам список). Атрибут не обязан работать корректно, если список пустой.
size (с коротким псевдонимом S), который содержит размер списка. Должна присутствовать возможность изменять этот атрибут: при увеличении размера в конец должны добавляться значения None, а при уменьшении последние элементы должны удаляться.
Обратите внимание, что все перечисленные атрибуты не являются методами (см. пример). Однако их рекомендуется не хранить, а вычислять «на лету».

Формат ввода
Ваш код должен иметь такой вид:

import sys

...

ваши импорты и реализация

класс должен называться «ExtendedList»

...

exec(sys.stdin.read())

(Программа выполнит код, записанный во входном файле)

Пример
Ввод	Вывод
# this is for similar behaviour in python 2 and python 3
from __future__ import print_function


l = ExtendedList([1, 2, 3])
print(l.reversed)
print(l.first)
l.F = 0
print(l)
l.append(4)
print(l.L)
l.size = 2
print(l)
[3, 2, 1]
1
[0, 2, 3]
4
[0, 2]
Примечания
Указание: от стандартного класса list можно наследоваться.
'''

import sys


class ExtendedList(list):
    @property
    def L(self):
        return self[-1]

    @L.setter
    def L(self, value):
        self[-1] = value

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, value):
        self[-1] = value

    @property
    def F(self):
        return self[0]

    @property
    def first(self):
        return self[0]

    @F.setter
    def F(self, value):
        self[0] = value

    @first.setter
    def first(self, value):
        self[0] = value

    @property
    def R(self):
        return self[::-1]

    @property
    def reversed(self):
        return self[::-1]

    @property
    def S(self):
        return len(self)

    @S.setter
    def S(self, value):
        while len(self) < value:
            self.append(None)
        while len(self) > value:
            self.pop()

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        while len(self) < value:
            self.append(None)
        while len(self) > value:
            self.pop()


exec(sys.stdin.read())

