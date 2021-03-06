'''
На вход подаётся строка. Необходимо посчитать для каждого входящего в неё символа длину наибольшей подстроки, состоящей только из символов, ему равных.
Формат ввода
Одна строка с текстом. Длина строки не превосходит 100 символов. В строку входят только символы с ASCII-кодом от 32 до 126 включительно.
Формат вывода
Нужно вывести N строк, где N — количество различных символов в строке.
В каждой из этих строк сначала должен идти символ, для которого она пишется, затем, через пробел, длина максимальной подстроки, состоящей только из такого символа.
Строки вывода должны быть отсортированы лексикографически.

Пример 1
Ввод	Вывод
correct your mistakes
  1
a 1
c 1
e 1
i 1
k 1
m 1
o 1
r 2
s 1
t 1
u 1
y 1
Пример 2
Ввод	Вывод
bee gees
  1
b 1
e 2
g 1
s 1
'''

s = input()
a = dict()
for i in s:
    ans = 1
    while (ans + 1) * i in s:
        ans += 1
    a[i] = ans
for key, value in sorted(a.items()):
    print(key, value)

