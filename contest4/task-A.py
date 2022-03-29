'''
Напишите генератор, возвращающий бесконечную последовательность чисел из треугольника Паскаля.
Сдавать нужно только код самого генератора, тестирующий код импортирует его и прогонит набор тестов.
Последовательность, возвращаемая генератором, должна выглядеть так:
1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1 1 6 15 20 15 6 1 1 7 21 35 35 21 7 1 1 8 28 56 70 56 28 8 1 1 9 36 84 126 126 84 36 9 1 ...

Формат ввода
Требуется реализовать генератор в виде функции без аргументов с именем pascal_triangle.
Текст програмы должен содержать генератор pascal_triangle и все необходимые импорты.

Файл с решением должен называться solution.py
'''

def pascal_triangle():
    start1 = [1]
    k = 0
    ans = []
    for i in start1:
        ans.append(i)
    while(1):
        mas = [None] * (k + 1)
        mas[0] = 1
        for i in range(1, k):
            mas[i] = start1[i - 1] + start1[i]
        mas[-1] = 1
        start1 = mas
        k += 1
        for i in mas:
            yield i

