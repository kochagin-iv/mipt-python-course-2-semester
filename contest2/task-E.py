'''
Переведите число из десятеричной системы счисления в некоторую другую

Формат ввода
На вход подается одна строка, в которой записано число в десятеричной системе счисления и основание новой (не превышающее 9)

Формат вывода
Введите число в новой системе счисления

Пример 1
Ввод	Вывод
10 9
11
Пример 2
Ввод	Вывод
16 2
10000
'''
n, m = map(int, input().split())
ans = ""
while n != 0:
    ans += str(n % m)
    n //= m
print(int(ans[::-1]))

