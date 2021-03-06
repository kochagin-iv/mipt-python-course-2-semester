'''
Как известно, счастливым билетиком называется такой, у которого сумма первых и последних трёх цифр равны. Напишите программу, которая для данного номера билетика найдёт ближайший к нему счастливый.
Формат ввода
Целое число X, составленное из шести цифр (100000≤X≤999999).
Формат вывода
Ближайшее к данному число из шести цифр, в котором сумма трёх первых цифр равна сумме трёх последних. Если ответов несколько, выведите любой.
Пример 1
Ввод	Вывод
223840
223700
Пример 2
Ввод	Вывод
223700
223700
'''
def check(x1):
    a1 = int(str(x1)[0])
    a2 = int(str(x1)[1])
    a3 = int(str(x1)[2])
    a4 = int(str(x1)[3])
    a5 = int(str(x1)[4])
    a6 = int(str(x1)[5])
    return a1 + a2 + a3 == a4 + a5 + a6


x = int(input())
x1 = x
x2 = x
while x1 < 10 ** 7:
    if check(x1):
        break
    x1 += 1
while x2 > 10 ** 5:
    if check(x2):
        break
    x2 -= 1
fl = 0
if check(x2) * check(x1) == 0:
    if check(x1):
        print(x1)
        fl = 1
    if check(x2):
        print(x2)
        fl = 1
if not fl:
    if x1 - x < x - x2:
        print(x1)
    else:
        print(x2)

