'''
Студент Петя в совершенстве отточил навык придумывания новых паролей и теперь объясняет студентке Ане какие пароли можно использовать, а какие нет. Помогите ему написать программку для оценки силы аниного пароля.

Правила простые: сильным может считаться только тот пароль, в котором есть буквы в разных регистрах и цифры. Пароли длины менее 8, пароли состоящие менее чем из 4 уникальных символов, и пароли в которых встречается слово anna (в любом регистре букв) считаются слабыми.

Формат ввода
Непустая строка с паролем

Формат вывода
строка 'weak' или 'strong'

Пример
Ввод	Вывод
Anna12345
weak
'''

s = input()
strong = 0
arr = []
for i in s:
    if i in arr:
        continue
    arr.append(i)
digit = 0
for i in s:
    if i.isdigit():
        digit = 1
if s.lower() != s and s.upper() != s and digit:
    strong = 1
if len(s) < 8 or len(arr) < 4 or 'anna' in s.lower():
    strong = 0
print('weak' * (1 - strong) + 'strong' * strong)
