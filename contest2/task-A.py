'''
Cейчас многие компании на программистских собеседованиях проводят предварительное тестирование. Классическая задача для такого тестирования — задача FizzBuzz.

Вам дано натуральное число N. Требуется вывести последовательность чисел от 1 до N. Но если число кратно 3, то выводится "Fizz"; если кратно 5, то "Buzz"; а если кратно 15, то "Fizz Buzz".

Поверьте, даже с такой простой задачей многие претенденты не справляются.

Формат ввода
Одно число — N.

Формат вывода
Искомая последовательность через запятую и пробел.

Пример
Ввод	Вывод
15
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz
'''
n = int(input())
s = ""
for i in range(1, n + 1):
    if i % 15 == 0:
        s += "Fizz Buzz" + ", "
        continue
    if i % 5 == 0:
        s += "Buzz" + ", "
        continue
    if i % 3 == 0:
        s += "Fizz" + ", "
        continue
    s += str(i) + ", "
print(s[:-2])
