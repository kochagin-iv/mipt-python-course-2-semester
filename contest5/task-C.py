'''
Напишите программу для переформатирования вывода команды git log.
Формат ввода
На вход программе подаётся лог с описанием коммитов, каждая строка которого отвечает формату: <sha-1>\t<date>\t<author>\t<email>\t<message>
Формат вывода
На выход нужно подать строки лога в формате: <первые 7 символов sha-1>...<message>. Длина строки должна быть 80 символов. Предполагается, что вход всегда корректный.
Пример
Ввод
0cd8619f18d8ecad1e5d2303f95ed206c2d6f92b	Fri Sep 23 10:59:32 2016 -0700	Brett Cannon	brettcannon@users.noreply.github.com	Update PEP 512 (#107)
94dbee096b92f10ab83bbcf88102c6acdc3d76d1	Thu Sep 22 12:39:58 2016 +0100	Thomas Kluyver	takowl@gmail.com	Update PEP 517 to use pyproject.toml from PEP 518 (#51)

Вывод
0cd8619....................................................Update PEP 512 (#107)
94dbee0..................Update PEP 517 to use pyproject.toml from PEP 518 (#51)
'''

import sys
p = []
for i in sys.stdin:
    p.append(i)
for i in p:
    y = i.split('\t')
    ans_str = ''
    ans_str += y[0][:7]
    if y[-1][-1] == '\n':
        y[-1] = y[-1][:len(y[-1]) - 1]
    for j in range(80 - 7 - len(y[-1])):
        ans_str += '.'
    ans_str += y[-1]
    if ans_str != '':
        print(ans_str)
