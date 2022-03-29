'''
Вам необходимо написать программу для вывода i-го простого числа.

Формат ввода
Одно число i - порядковый номер простого числа.

Формат вывода
i-е простое число.

Пример 1
Ввод	Вывод
1
2
Пример 2
Ввод	Вывод
2
3
Пример 3
Ввод	Вывод
5
11
'''
def check(y):
    j = 1
    kol1 = 0
    while j * j <= y:
        if y % j == 0:
            kol1 += 1
        if kol1 > 1:
            return 0
        j += 1
    if kol1 > 1:
        return 0
    return 1


i = int(input())
i1 = 2
kol = 0
anss = 0
while kol != i:
    if check(i1):
        kol += 1
        anss = i1
    i1 += 1
print(anss)

