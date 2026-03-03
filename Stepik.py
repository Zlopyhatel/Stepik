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
"""""
