'''Даны два момента времени в пределах одних и тех же суток. Для каждого момента указан час, минута и секунда. Известно, что второй момент времени наступил не раньше первого.

Определите сколько секунд прошло между двумя моментами времени.

Формат ввода
Программа на вход получает шесть целых чисел через перевод строки. Первые три целых числа соответствуют часам, минутам и секундам первого момента, следующие три числа соответствуют второму моменту.

Часы задаются числом от 0 до 23 включительно. Минуты и секунды – от 0 до 59.

Формат вывода
Выведите число секунд между этими моментами времени.

Пример
Ввод	Вывод
1
1
1
2
2
2
3661
'''

ch1 = int(input())
m1 = int(input())
s1 = int(input())
ch2 = int(input())
m2 = int(input())
s2 = int(input())
ans = (ch2 - ch1) * 3600 + (m2 - m1) * 60 + s2 - s1
ans += 3600 * 24
print(ans % (3600 * 24))
