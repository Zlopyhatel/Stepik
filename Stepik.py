"""""
print("I'm", 'Just', 'Ken', "!")

print('Как тебя зовут?')     # вывод текста
print('Привет,', input())    # ввод текста и вывод текста

variable_name = input()
print('Вы ввели текст:', variable_name)

name = input()
print(name, "- чемпион!")

str1 = input()
str2 = input()
str3 = input()

print(str3)
print(str2)
print(str1)
#23/02/2026
print('I','like','Python', sep='***')

name = input()
print('Привет,', name, end='!')


sep = input()
arg1 = input()
arg2 = input()
arg3 = input()
print(arg1, arg2, arg3, sep=sep)

x = int(input())
print(x)
print(x + 1)
print(x + 2)

x = int(input())
y = int(input())
z = int(input())
w = int(input())
print((x + y + z + w)*3)

a = int(input())
b = int(input())
c = 3*(a+b)**3 + 275*b**2 - 127*a - 41
print(c)

x = int(input())
print('Следующее за числом',x, 'число:',x+1)
print('Для числа',x, 'предыдущее число:',x-1)

a = int(input())
print('Объем =',a**3)
print('Площадь полной поверхности =',6*a**2)

a = int(input())
b = int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)

a1 = int(input())
d = int(input())
n = int(input())
print(a1 + d*(n-1))

x = int(input())
print(x, x*2, x*3, x*4, x*5, sep='---')

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

a = 82 // 3**2 % 7
print(a)

b = int(input())
q = int(input())
n = int(input())
print(b * q**(n-1))

cm = int(input())
print(cm // 100)

n = int(input()) #students
k = int(input()) #mandarin
print(k // n)
print(k % n)

x = int(input())
print(-(-x // 2))

#Stepik samples
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Число десятков =', first_digit)
print('Число единиц =', last_digit)

num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Сумма цифр =', last_digit + first_digit)

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')
#end of Stepik samples

#https://stepik.org/lesson/284816/step/21?unit=266160
num = int(input().strip())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)


#https://stepik.org/lesson/284816/step/22?unit=266160
num = int(input().strip())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep='')
print(digit1, digit3, digit2, sep='')
print(digit2, digit1, digit3, sep='')
print(digit2, digit3, digit1, sep='')
print(digit3, digit1, digit2, sep='')
print(digit3, digit2, digit1, sep='')

#https://stepik.org/lesson/284816/step/23?unit=266160
num = int(input().strip())
digit4 = num % 10
digit3 = (num // 10) % 10
digit2 = (num // 100) % 10
digit1 = num // 1000
print('Цифра в позиции тысяч равна',digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)


i = 54321
print(i // 10000)

#exam
print("раз", "два, "три")
print("Told you not to worry", "But maybe that's a lie", sep=' :) ')
print("Honey, what's your hurry", end='?')

print('*****************',sep='')
print('*               *',sep='')
print('*               *',sep='')
print('*****************',sep='')

a = int(input())
b = int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

n = int(input())
print(n + int(str(n)+str(n)) + int(str(n)+str(n)+str(n)))
n = input()
print(int(n)+int(n+n)+int(n+n+n))

#4  Условный оператор
word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')
#https://stepik.org/lesson/265081/step/12?unit=246029
str1 = input()
str2 = input()
if str1 == str2:
    print('Пароль принят')
else:
    print('Пароль не принят')

#https://stepik.org/lesson/265081/step/13?unit=246029
n = int(input())
if n%2 != 0:
    print('Нечетное')
else:
    print('Четное')

#https://stepik.org/lesson/265081/step/14?unit=246029
n = int(input())
if n >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

#https://stepik.org/lesson/265081/step/15?unit=246029
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)

#05/03/2026
#https://stepik.org/lesson/265081/step/16?unit=246029
a = int(input())
b = int(input())
c = int(input())
if c-b == b-a and c == b + (b-a):
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/265081/step/17?unit=246029
#сумма первой и последней цифр равна разности второй и третьей цифр.
num=int(input())
digit4 = num % 10
digit3 = (num // 10) % 10
digit2 = (num // 100) % 10
digit1 = num // 1000
if (digit1 + digit4) == (digit2 - digit3):
    print('ДА')
else:
    print('НЕТ')

#https://stepik.org/lesson/265081/step/18?unit=246029
#считывает три числа и подсчитывает сумму только положительных чисел
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum_positive = 0
if num1 > 0:
    sum_positive += num1
if num2 > 0:
    sum_positive += num2
if num3 > 0:
    sum_positive += num3
print(sum_positive)

#https://stepik.org/lesson/265081/step/19?unit=246029
#по введённому возрасту пользователя сообщает, к какой возрастной группе он относится
num = int(input())
if num <= 13:
    print('детство')
if 14 <= num <= 24:
    print('молодость')
if 25 <= num <= 59:
    print('зрелость')
if num >= 60:
    print('старость')

#https://stepik.org/lesson/265081/step/20?unit=246029
#которая определяет наименьшее из четырёх чисел
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num = num1
if num > num2:
    num = num2
if num > num3:
    num = num3
if num > num4:
    num = num4
print(num)

#examples
#https://stepik.org/lesson/265083/step/2?unit=246031
#Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')
    
#Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')
    
#Напишите программу, которая по координатам точки, не лежащей на осях координат,
# определяет номер координатной четверти, в которой она находится.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

"""""
