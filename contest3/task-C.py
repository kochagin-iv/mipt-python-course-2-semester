'''
Вам дана строка и целое положительное число N. Составьте словарь с частотами вхождения всех подстрок длины N исходной строки. В качестве ответа на задачу выведите отсортированный в лексикографическом порядке список подстрок, которые встречаются в исходной подстроке 2 или более раз.

Формат ввода
Строка и целое положительное число через стандартный ввод. Считать их можно, два раза вызвав функцию input()

Формат вывода
Отсортированный в лексикографическом порядке список строк, удовлетворяющий условию задачи.

Пример
Ввод	Вывод
abbccc
1

['b', 'c']
'''

s = input()
n = int(input())
mas = dict()
for i in range(len(s) - n + 1):
    mas[s[i:i + n]] = 0

for i in range(len(s) - n + 1):
    mas[s[i:i + n]] += 1
ans = []
for u, v in mas.items():
    if v >= 2:
        ans.append(u)
ans.sort()
print(ans)

