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


#06/03/2026
a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)


#https://stepik.org/lesson/265083/step/15?unit=246031
#На вход программе подаётся целое число.  Если точка выколотая, то граница не включается.
# Если же точка закрашенная, то граница включается
x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

#https://stepik.org/lesson/265083/step/16?unit=246031
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам
x = int(input())
if -3 >= x or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

#https://stepik.org/lesson/265083/step/17?unit=246031
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

#https://stepik.org/lesson/265083/step/18?unit=246031
# Назовём число красивым, если оно является четырёхзначным и делится нацело на 7 или на 17.
# Напишите программу, определяющую, является ли введённое число красивым.
# Программа должна вывести «YES» (без кавычек), если число является красивым, или «NO» (без кавычек) в противном случае.
x = int(input())
if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')    

#https://stepik.org/lesson/265083/step/19?unit=246031
# Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.
a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and c + a > b:
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/265083/step/20?unit=246031
# Напишите программу, которая определяет, является ли год с данным номером високосным.
# Если год является високосным, то выведите «YES» (без кавычек), иначе выведите «NO» (без кавычек).
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
x = int(input())
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/265083/step/21?unit=246031
# Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала
# для первой клетки, потом для второй клетки.
# Программа должна вывести «YES» (без кавычек), если из первой клетки ходом ладьи можно попасть во вторую,
# или «NO» (без кавычек) в противном случае.
# На вход программе подаются четыре числа от 1 до 8.
a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if a1 - a == 0 and 0 < b <= 8 or b1 - b == 0 and 0 < a <= 8:
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/265083/step/22?unit=246031
#Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет, может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала
# для первой клетки, потом для второй клетки.
# Программа должна вывести «YES» (без кавычек),
# если из первой клетки ходом короля можно попасть во вторую, или «NO» (без кавычек) в противном случае.
a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if abs(a1 - a) <= 1 and abs(b1 - b) <= 1:
    print('YES')
else:
    print('NO')

angle = 2
if angle > 30:
    print('Больше 30')
elif angle < 60:
    print('Меньше 60')
if angle != 90:
    print('Непрямой')

n = int(input())
k = int(input())
if n > k:
    print("NO")
elif n < k:
    print("YES")
else:
    print("Don't know")

#https://stepik.org/lesson/265082/step/15?unit=246030
#Напишите программу, которая классифицирует треугольник на основе длин его сторон.
# Программа должна принимать три числа, каждое из которых представляет собой длину одной из его сторон.
# В результате программа должна определить, является ли треугольник равносторонним, равнобедренным или разносторонним.
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or c == a or c == b:
    print('Равнобедренный')
else:
    print('Разносторонний')

#https://stepik.org/lesson/265082/step/16?unit=246030
#Даны три различных целых числа. Напишите программу, которая находит серединное значение из этих чисел.
a, b, c = int(input()), int(input()), int(input())
if b < a < c or c < a < b:
    print(a)
elif a < b < c or a > b > c:
    print(b)
else:
    print(c)

#https://stepik.org/lesson/265082/step/17?unit=246030
#Дан порядковый номер месяца (1,2,…,12).
# Напишите программу, которая выводит на экран количество дней в этом месяце.
# Принять, что год является невисокосным.
x = int(input())
d31 = [1,3,5,7,8,10,12]
d30 = [4,6,9,11]
if x in d31:
    print(31)
elif x in d30:
    print(30)
else:
    print(28)

#https://stepik.org/lesson/265082/step/18?unit=246030
# Известен вес боксёра-любителя (целое число).
# Известно, что вес таков, что боксер может быть отнесён к одной из трёх весовых категорий:
# Легкий вес – до 60 (невключительно);
# Первый полусредний вес – до 64 (невключительно);
# Полусредний вес – до 69 (невключительно).
# Напишите программу, определяющую, в какой категории будет выступать данный боксёр.
x = int(input())
if 60 <= x < 64:
    print('Первый полусредний вес')
elif 64 <= x < 69:
    print('Полусредний вес')
else:
    print('Легкий вес')
m = int(input())

if m < 60:
    print('Легкий вес')
elif m < 64:
    print('Первый полусредний вес')
elif m < 69:
    print('Полусредний вес')    

#https://stepik.org/lesson/265082/step/19?unit=246030
# Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
# то выведите результат применения этой операции к введённым ранее числам,
# в противном случае выведите «Неверная операция» (без кавычек).
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!» (без кавычек).
a, b, c = int(input()), int(input()), input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')

#https://stepik.org/lesson/265082/step/20?unit=246030
#Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.
a, b = input(), input()
valid_colors = {'красный', 'синий', 'желтый'}
if a not in valid_colors or b not in valid_colors:
    print('ошибка цвета')
else:
    if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('оранжевый')
    elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
        print('зеленый')
    else:
        print(a)


#09/03/2026
#https://stepik.org/lesson/265082/step/21?unit=246030
#Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
x = int(input())
if x == 0:
    print('зеленый')
elif 1 <= x <= 36:
    if x % 2 != 0:
        if 1 <= x <= 10 or  19 <= x <= 28:
            print('красный')
        else:
            print('черный')
    else:
        if 1 <= x <= 10 or  19 <= x <= 28:
            print('черный')
        else:
            print('красный')
else:
    print('ошибка ввода')

#https://stepik.org/lesson/265082/step/22?unit=246030
#На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение.
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

left = a1 if a1 > a2 else a2      # max(a1, a2) без функции
right = b1 if b1 < b2 else b2     # min(b1, b2) без функции

if left < right:
    print(left, right)
elif left == right:
    print(left)
else:
    print('пустое множество')

#exam
#1
x = int(input())
d = x % 10
c = (x // 10) % 10
if c == d == 0:
    print('YES')
else:
    print('NO')
#https://stepik.org/lesson/292172/step/2?unit=273659

x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')


#https://stepik.org/lesson/292172/step/3?unit=273659
age = int(input())
male = input()
if 10 <= age <= 15 and male == 'f':
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/292172/step/4?unit=273659
x = int(input())
if 1 <= x <= 10:
    if x == 1:
        print('I')
    elif x == 2:
        print('II')
    elif x == 3:
        print('III')
    elif x == 4:
        print('IV')
    elif x == 5:
        print('V')
    elif x == 6:
        print('VI')
    elif x == 7:
        print('VII')
    elif x == 8:
        print('VIII')
    elif x == 9:
        print('IX')
    elif x == 10:
        print('X')
else:
    print('ошибка')

#https://stepik.org/lesson/292172/step/5?unit=273659
x = int(input())
if x % 2 != 0:
    print('YES')
elif 2 <= x <= 5 and x % 2 == 0:
    print('NO')
elif 6 <= x <= 20 and x % 2 == 0:
    print('YES')
elif x > 20 and x % 2 == 0:
    print('NO')

#https://stepik.org/lesson/292172/step/6?unit=273659
x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/292172/step/7?unit=273659
x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/292172/step/8?unit=273659
x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/265105/step/15?unit=246053
a, b = float(input()), float(input())
print(a * b * 0.5)

#https://stepik.org/lesson/265105/step/16?unit=246053
s, v1, v2 = float(input()), float(input()), float(input())
print(s / (v1 + v2))

#https://stepik.org/lesson/265105/step/17?unit=246053
# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
x = float(input())
if x != 0:
    print(x ** -1)
else:
    print('Обратного числа не существует')

#https://stepik.org/lesson/265105/step/18?unit=246053
#Напишите программу, которая определяет,
# какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.
x = float(input())
print(5 / 9 * (x - 32))

#https://stepik.org/lesson/265105/step/19?unit=246053
#На вход программе подаётся число n – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах по следующему алгоритму:
# в течение первых двух лет собачий год равен 10.5 человеческим годам,
# после этого каждый год собаки равен 4 человеческим годам.
x = float(input())
if x <= 2:
    age = x * 10.5
else:
    age = 21 + (x-2) * 4
print(age)

age = x * 10.5 if x <= 2 else 21 + (x-2) * 4
print(age)

#https://stepik.org/lesson/265105/step/20?unit=246053
#Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
x = float(input())
print(int(x * 10 % 10))

#https://stepik.org/lesson/265105/step/21?unit=246053
#Дано положительное действительное число. Выведите его дробную часть.
x = float(input())
print(x - int(x))

#https://stepik.org/lesson/265105/step/27?unit=246053
#Напишите программу, которая находит наименьшее и наибольшее из пяти чисел и выводит текст в следующем формате:
x1, x2, x3, x4, x5 = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(x1, x2, x3, x4, x5))
print('Наибольшее число =', max(x1, x2, x3, x4, x5))

#https://stepik.org/lesson/265105/step/28?unit=246053
#Даны пять чисел. Напишите программу, которая вычисляет сумму их модулей
x1, x2, x3, x4, x5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(x1) + abs(x2) + abs(x3) + abs(x4) + abs(x5))

#10/03/2026
#https://stepik.org/lesson/265105/step/29?unit=246053
# Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет, интересное число или нет.
# Если число интересное, следует вывести текст «Число интересное» (без кавычек),
# иначе – «Число неинтересное» (без кавычек).
x = int(input())
c = x % 10
b = x //10 % 10
a = x // 100
avg = a + b + c - max(a, b, c) - min(a, b, c)
if max(a, b, c) - min(a, b, c) == avg:
    print('Число интересное')
else:
    print('Число неинтересное')

# https://stepik.org/lesson/265105/step/30?unit=246053
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
a,b,c = int(input()), int(input()), int(input())
print(max(a, b, c))
print((a + b + c) - max(a, b, c) - min(a, b, c))
print(min(a, b, c))

#https://stepik.org/lesson/265105/step/31?unit=246053
# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены,
# вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
# Напишите программу, определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))

#https://stepik.org/lesson/265115/step/12?unit=246063
# Напишите программу, которая выводит текст
print('"Python is a great language!",' + ' said Fred.' + ' "I' + " don't" + ' ever remember having this much fun before."')

#https://stepik.org/lesson/265115/step/13?unit=246063
# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя – и выводит фразу
name, lname = input(), input()
print('Hello ' + name + ' ' + lname + '! You have just delved into Python')

#https://stepik.org/lesson/265115/step/14?unit=246063
# Напишите программу, которая считывает с клавиатуры название футбольной команды
# и выводит информацию о ней в следующем формате
name = input()
print('Футбольная команда ' + name + ' имеет длину ' + str(len(name)) + ' символов')

#https://stepik.org/lesson/265115/step/15?unit=246063
# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city1, city2, city3 = input(), input(), input()
cityl1, cityl2, cityl3 = len(city1), len(city2), len(city3)
if min(cityl1, cityl2, cityl3) == cityl1:
    print(city1)
elif min(cityl1, cityl2, cityl3) == cityl2:
    print(city2)
else:
    print(city3)

if max(cityl1, cityl2, cityl3) == cityl1:
    print(city1)
elif max(cityl1, cityl2, cityl3) == cityl2:
    print(city2)
else:
    print(city3)

#https://stepik.org/lesson/265115/step/16?unit=246063
# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.
a, b, c = input(), input(), input()
la, lb, lc = len(a), len(b), len(c)
a1, a3 = min(la, lb, lc), max(la, lb, lc)
a2 = la + lb + lc - a1 - a3
if a2 - a1 == a3 - a2:
    print('YES')
else:
    print('NO')
print(a1,a2,a3)

#11/03/2026
# https://stepik.org/lesson/265115/step/21?unit=246063
# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек),
# если во введённой строке есть подстрока «синий», или «NO» (без кавычек) в противном случае.
if 'синий' in input():
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/265115/step/22?unit=246063
# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек),
# если во введённой строке есть подстрока «суббота» или «воскресенье», или «NO» (без кавычек) в противном случае.
text = input()
print('YES' if 'суббота' in text or 'воскресенье' in text else 'NO')

#https://stepik.org/lesson/265115/step/23?unit=246063
# Будем считать email адрес корректным, если в нём есть символы собачки (@) и точки (.).
# Напишите программу, проверяющую корректность email адреса.
text = input()
print('YES' if '@' in text and '.' in text else 'NO')

import math

num1 = math.sqrt(2)     # вычисление квадратного корня из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

#https://stepik.org/lesson/265110/step/4?unit=246058
# Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R
import math
R = float(input())
print(math.pi * pow(R, 2))
print(2 * math.pi * R)

#https://stepik.org/lesson/265110/step/5?unit=246058
# Напишите программу, которая принимает на вход действительное число x и вычисляет по нему значение
import math
x = float(input())
print(math.floor(x) + math.ceil(x))

#https://stepik.org/lesson/265110/step/6?unit=246058
# На плоскости евклидово расстояние ρ между двумя точками
import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2)))

#https://stepik.org/lesson/265110/step/7?unit=246058
# Напишите программу, вычисляющую значение тригонометрического выражения по заданному числу градусов x
import math
x = float(input())
res = math.sin(math.radians(x)) + math.cos(math.radians(x)) + pow(math.tan(math.radians(x)),2)
print(res)

#https://stepik.org/lesson/265110/step/8?unit=246058
# Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
# Даны два числа: натуральное число n и действительное число a.
# Напишите программу, которая находит площадь указанного правильного многоугольника
import math
n, a = int(input()), float(input())
print(n * pow(a, 2) / (4 * math.tan(math.pi / n)))

#https://stepik.org/lesson/265110/step/9?unit=246058
# На вход программе подаются два положительных действительных числа a и b каждое на отдельной строке.
# Программа должна вывести 4 числа (каждое на отдельной строке) – среднее арифметическое,
# геометрическое, гармоническое и квадратичное.
import math
a, b = float(input()), float(input())
print((a + b) / 2)
print(math.sqrt(a * b))
print(2 * a * b / (a + b))
print(math.sqrt((math.pow(a,2) + math.pow(b,2))/2))

#https://stepik.org/lesson/265110/step/10?unit=246058
# Даны три действительных числа a, b, c. Напишите программу, которая находит действительные корни квадратного уравнения
import math
a, b, c = float(input()), float(input()), float(input())
D = pow(b, 2) - 4 * a * c
if D < 0:
    print('Нет корней')
elif D == 0:
    print(-b/(2*a))
elif D > 0:
    x = ((-b - math.sqrt(D)) / (2*a))
    y = ((-b + math.sqrt(D)) / (2*a))
    print(min(x,y))
    print(max(x,y))

#https://stepik.org/lesson/265118/step/7?unit=246067
#Напишите программу, которая выводит текст «Python is awesome!» (без кавычек) 10 раз
for i in range(10):
    print('Python is awesome!')

#https://stepik.org/lesson/265118/step/8?unit=246067
# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

#https://stepik.org/lesson/265118/step/9?unit=246067
# Дано предложение и количество раз, сколько его надо повторить.
# Напишите программу, которая повторяет данное предложение нужное количество раз.
text = input()
count = int(input())
for i in range(count):
    print(text)

#https://stepik.org/lesson/265118/step/10?unit=246067
# На вход программе подаётся натуральное число n
# Напишите программу, которая печатает звёздный прямоугольник размерами
n = int(input())
for i in range(n):
    print('*******************')

for i in range(27):
    j = i + 1
    print('i-',i)
print('j-',j)

total = 0
for i in range(3):
    total = total - i
    print(total)

total = 0
for i in range(10):
    total = total + i
    print(total)
    if i == 9:
        total = 1
print(total)

#12/03/2026
#https://stepik.org/lesson/265118/step/18?unit=246067
#Напишите программу, которая считывает одну строку текста и выводит 10 строк,
# пронумерованных от 0 до 9 каждая, с указанной строкой текста
s = input()
for i in range(10):
    print(i, s)

#https://stepik.org/lesson/265118/step/19?unit=246067
# На вход программе подаётся натуральное число n.
# Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит текст в следующем формате
n = int(input())
for i in range(n+1):
    print('Квадрат числа', i, 'равен', i ** 2)

#https://stepik.org/lesson/265118/step/20?unit=246067
# На вход программе подаётся натуральное число n (n ≥ 2 )
# n(n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звёздный треугольник в соответствии с примером
n = int(input())
for i in range(n):
    print('*' * (n-i))

#https://stepik.org/lesson/265118/step/21?unit=246067
#На вход программе подаются три натуральных числа m, p, n:
#m: стартовое количество организмов;
#p: среднесуточное увеличение в %;
#n: количество дней для размножения.
#Напишите программу, которая предсказывает размер популяции организмов с 1-го по n-й день (включительно).
#Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m * (1 + p/ 100)

for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)

Напишем программу, которая выводит все четные числа из промежутка [56;170].
for i in range(56, 171, 2):
    print(i)

#13/03/2026
for i in range(10, 0, -2):
    print(i)

for i in range(1, 10, 3):
    print(i, sep='?')

for i in range(2, 6, 2):
    print(i, end=',')

#https://stepik.org/lesson/265120/step/14?unit=246069
#Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно
m, n = int(input()), int(input())
if m <= n:
    for i in range(m, n + 1):
        print(i)
if n < m:
    for i in range(n, m + 1):
        print(i)

#https://stepik.org/lesson/265120/step/15?unit=246069
#Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n (от 1 до 10 включительно).
n = int(input())
for i in range(1,11):
    print(n, 'x', i, '=', n * i )

#https://stepik.org/lesson/265120/step/16?unit=246069
m, n = int(input()), int(input())
if m <= n:
    for i in range(m, n + 1):
        if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
            print(i)

#https://stepik.org/lesson/265120/step/17?unit=246069
# Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечётные целые числа от m до n (включительно) в порядке убывания.
m, n = int(input()), int(input())
if m > n:
    for i in range(m, n - 1, -1):
        if i % 2 != 0:
            print(i)

m, n = int(input()), int(input())
start = m + (m % 2 - 1)  # делаем m нечётным
for i in range(start, n - 1, -2):
    print(i)

#https://stepik.org/lesson/265120/step/18?unit=246069
# Даны два целых числа m и n.
# Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания,
# если m < n, или в порядке убывания в противном случае.
m, n = int(input()), int(input())
if m > n:
    for i in range(m, n - 1, -1):
            print(i)
elif m < n:
    for i in range(m, n + 1,):
        print(i)
else:
    print(m)

#18/03/2026
counter = 0                                             # создаём переменную счётчика
for _ in range(10):
    num = int(input())
    if num > 10:                                        # при выполнении условия
        counter = counter + 1                           # увеличиваем значение cчётчика

print('Было введено', counter, 'чисел, больших 10.')

counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)

total = 0
for _ in range(10):
    num = int(input())
    total = total + num
average = total / 10
print('Среднее значение равно', average)

total_len = 0
for _ in range(3):
    word = input()
    total_len = total_len + len(word)
print(total_len)

#Сириус
#Кассиопея
#Каллисто


total = 0
for i in range(1, 6):
    total += i
    print(total, end='')

flag = False
for _ in range(5):
    word = input()
    if len(word) < 5:
        flag = True
print(flag)


#19/03/2026
#https://stepik.org/lesson/294243/step/1?unit=275922
#На вход программе подаются два целых числа.
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b (включительно),
# куб которых оканчивается на 4 или 9.
a, b = int(input()), int(input())
count = 0
for i in range(a, b + 1):
    if pow(i,3) % 10 == 4 or pow(i,3) % 10 == 9:
        count += 1
print(count)

#https://stepik.org/lesson/294243/step/2?unit=275922
#На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введённых чисел (не включая само число n).
n = int(input())
res = 0
for _ in range(n):
    number = int(input())
    res += number
print(res)

#https://stepik.org/lesson/294243/step/3?unit=275922
#На вход программе подаётся натуральное число n. Напишите программу, которая вычисляет значение выражения
import math
n = int(input())
res1 = 0
res = 0
for i in range(1, n + 1):
    res1 += (1/i)
res = res1 - math.log(n)
print(res)

#https://stepik.org/lesson/294243/step/4?unit=275922
#На вход программе подаётся натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно),
# квадрат которых оканчивается на 2, на 5 или на 8.
n = int(input())
res = 0
for i in range(1, n + 1):
    if pow(i,2) % 10 == 2 or pow(i,2) % 10 == 5 or pow(i,2) % 10 == 8:
        res += i
if res == 0:
    print('0')
else:
    print(res)

#https://stepik.org/lesson/294243/step/5?unit=275922
#На вход программе подаётся натуральное число n.
# Напишите программу, которая вычисляет n!
import math
print(math.factorial(int(input())))

#https://stepik.org/lesson/294243/step/6?unit=275922
#Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
res = 1
for _ in range(10):
    n = int(input())
    if n != 0:
        res *= n
print(res)

#https://stepik.org/lesson/294243/step/7?unit=275922
#На вход программе подаётся натуральное число n.
# Напишите программу, которая вычисляет сумму всех его делителей.
n = int(input())
res = 0
for i in range(1, n + 1):
    if n % i == 0:
        res += i
print(res)

#https://stepik.org/lesson/294243/step/8?unit=275922
#Напишите программу, которая считывает последовательность из 10 целых чисел и определяет,
# является ли каждое из них чётным или нет.
res1 = 0
res2 = 0
for _ in range(10):
    n = int(input())
    res1 += n
    if n % 2 == 0:
        res2 += n
if res1 == res2:
    print('YES')
if res1 != res2:
    print('NO')
#example
f = 'YES'
for _ in range(10):
    if int(input())%2:
        f = 'NO'
print(f)

#https://stepik.org/lesson/294243/step/9?unit=275922
#На вход программе подаётся натуральное число n. Напишите программу вычисления знакочередующейся суммы
n = int(input())
res = 0
for i in range(1,n + 1):
    if i % 2 != 0:
        res += i
    else:
        res -= i
print(res)

#https://stepik.org/lesson/294243/step/10?unit=275922
#На вход программе подаются натуральное число n (n ≥ 2), а затем n различных натуральных чисел последовательности,
# каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
n = int(input())
max1 = 0
max2 = 0

for _ in range(n):
    m = int(input())
    if m > max1:
        max2 = max1  # сохраняем предыдущий max1
        max1 = m
    elif m > max2:
        max2 = m
print(max1)
print(max2)

#https://stepik.org/lesson/294243/step/11?unit=275922
#Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
#AI
n = int(input())
a, b = 1, 1
result = []
for _ in range(n):
    result.append(a)
    a, b = b, a + b
print(' '.join(map(str, result)))

#Stepik
n = int(input())
a, b = 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b


#20/03/2026
text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()
print('Сумма чисел равна', total)

num = int(input())
total = 0
while abs(num) <= 5:
    total += num
    num = int(input())
print(total)

num = int(input())
total = 0
while abs(num) <= 5:
    total += num
    num = int(input())
print(total)

count = 1
while count < 10:
    print('Python awesome!')

num = int(input())
counter = 0
while '0' not in str(num):
    counter += 1
    print(counter)
    num = int(input())
    print(num)
print(counter)

num = int(input())
counter = 0
while '0' not in str(num):
    counter += 1
print(counter)

num = int(input())
total = 0
while num > -4:
    num = int(input())
    total += num
    print(total)
print(total)

i = 7
a = 5
while i < 11:
    a += i
    i += 2
print(a)

total = 1
while total < 10:
    num = int(input())
    total *= num
    print(total)


#23/03/2026

#https://stepik.org/lesson/265121/step/16?unit=246070
#На вход программе подаётся последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек).
# При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя её окончание.
# Напишите программу, которая выводит члены данной последовательности.
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()

#https://stepik.org/lesson/265121/step/17?unit=246070
#На вход программе подаётся последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» или «конец» (без кавычек).
# При этом сами слова «КОНЕЦ» и «конец» не входят в последовательность, лишь символизируя её окончание.
# Напишите программу, которая выводит члены данной последовательности.
text = input()
while text.upper() != 'КОНЕЦ':
    print(text)
    text = input()

#https://stepik.org/lesson/265121/step/18?unit=246070
#На вход программе подаётся последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трёх слов: «стоп», «хватит», «достаточно» (без кавычек).
# Сами эти слова в последовательность не входят, лишь символизируя её окончание.
# Напишите программу, которая выводит общее количество членов данной последовательности.
text = input()
counter = 0
while text not in ['стоп','хватит','достаточно']:
    counter += 1
    text = input()
print(counter)

#https://stepik.org/lesson/265121/step/19?unit=246070
#На вход программе подаётся последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число, не делящееся на 7
# (само это число в последовательность не входит, лишь символизируя её конец).
# Напишите программу, которая выводит члены данной последовательности.
num = int(input())
flag = True
while flag:
    if num % 7 == 0:
        flag = True
        print(num)
        num = int(input())
    else:
        flag = False

n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())

#https://stepik.org/lesson/265121/step/20?unit=246070
#На вход программе подаётся последовательность целых чисел, каждое число на отдельной строке.
# Признаком окончания последовательности является любое отрицательное число,
# при этом в саму последовательность оно не входит.
# Напишите программу, которая выводит сумму всех членов данной последовательности.

n = int(input())
s = 0
while n >= 0:
    s = s + n
    n = int(input())
print(s)

#https://stepik.org/lesson/265121/step/21?unit=246070
#На вход программе подаётся последовательность целых чисел от 1 до 5, характеризующее оценку ученика,
# каждое число на отдельной строке.
# Концом последовательности является любое неположительное число либо число, большее 5.
# Напишите программу, которая выводит количество пятерок.

n = int(input())
s = 0
while 1 <= n <= 5:
    if n == 5:
        s += 1
    n = int(input())
print(s)

#https://stepik.org/lesson/265121/step/22?unit=246070
#У Тимура есть список никнеймов соцсети FriendsGram.
# Напишите программу, которая выводит первый никнейм, не содержащий символ нижнего подчёркивания

name = input()
while '_' in name:
    name = input()
print(name)

#https://stepik.org/lesson/265121/step/23?unit=246070
#На блиц-игру с шахматным компьютером AlphaZero выстроилась очередь людей.
# Сэм болеет за Александру и Левона и не хочет смотреть игры других участников.
# Сэму интересно, сколько людей стоят в очереди между Александрой и Левоном, потому что если придётся долго ждать,
# Сэм отлучится на перекус 🍔 в кафе.
# Также известно, что Александра пришла раньше Левона, поэтому будет стоять в очереди перед ним.

name = input()
count = 0
while 'Александра' not in name:
    name = input()
name = input()
while 'Левон' not in name:
    count = count + 1
    name = input()
print(count)

#https://stepik.org/lesson/265121/step/24?unit=246070
#Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево.
# К тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
# В мире ведьмака существуют монеты с номиналами 1,5,10,25.
#Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.

n = int(input())
c = 0
if n >= 25:
    c += n // 25
    n %= 25
if n >= 10:
    c += n // 10
    n %= 10
if n >= 5:
    c += n // 5
    n %= 5
if n >= 1:
    c += n // 1
    n %= 1
print(c)

#AI
n = int(input())
count = 0
# Берём максимально возможное количество монет каждого номинала
count += n // 25  # монеты по 25
n %= 25           # остаток
count += n // 10  # монеты по 10
n %= 10
count += n // 5   # монеты по 5
n %= 5
count += n // 1   # монеты по 1
print(count)

n = int(input())
coins = [25, 10, 5, 1]
count = 0
for coin in coins:
    count += n // coin
    n %= coin
print(count)

#https://stepik.org/lesson/265121/step/25?unit=246070
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
time1 = h1* 60 + m1
time2 = h2* 60 + m2
while time1 <= time2:
    while m1 <= m2 and m1 < 60 and h1 <= h2:
        print(h1,':',m1, sep ='' )
        m1 += 1
        if m1 == 59:
            h1 += 1

#AI
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
# Конвертируем в общее количество минут
start = h1 * 60 + m1
end = h2 * 60 + m2
# Перебираем все минуты от start до end включительно
for total_minutes in range(start, end + 1):
    # Конвертируем обратно в часы и минуты
    hours = total_minutes // 60
    minutes = total_minutes % 60
    # Выводим в формате hh:mm с ведущими нулями
    print(f"{hours:02d}:{minutes:02d}")    

#(num // 10 ** (n - i)) % 10
#где n – количество разрядов числа, i – номер цифры числа (слева направо, начиная с 1).

#24/03/2026

num = 1576
has_seven = False                                 # сигнальная метка (флаг)
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10
if has_seven == True:
    print('YES')
else:
    print('NO')

num = int(input())                                # считываем число
n = len(str(num))                                 # количество разрядов числа
for i in range(1, n + 1):                         # проходим по всем разрядам числа от 1 до n
    digit = num // 10 ** (n - i) % 10
    print(i,digit)

num = 813
while num > 0:
    last_digit = num % 10
    num //= 10
    print(last_digit, sep='=', end='')

num = 725
while num != 0:
    last_digit = num % 10
    num //= 10
    print(last_digit, sep='', end='$')

num = 586
while num > 0:
    last_digit = num % 10
    print(last_digit, sep='*', end='#')
    num //= 10
    print()

#https://stepik.org/lesson/265122/step/12?unit=246071
#Дано натуральное число.
# Напишите программу, которая выводит его цифры в столбик в обратном порядке
num = int(input())
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num //= 10

#https://stepik.org/lesson/265122/step/13?unit=246071
#Дано натуральное число.
# Напишите программу, которая меняет порядок цифр числа на обратный.
num = int(input())
while num > 0:
    last_digit = num % 10
    print(last_digit,end='')
    num //= 10

#https://stepik.org/lesson/265122/step/14?unit=246071
#Дано натуральное число n(n≥10).
# Напишите программу, которая определяет его максимальную и минимальную цифры и выводит текст в следующем формате:
num = int(input())
max_digit = 0
min_digit = num % 10
while num > 0:
    current_digit = num % 10
    if current_digit > max_digit:
        max_digit = current_digit
    if current_digit < min_digit:
        min_digit = current_digit
    num //= 10
print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)

#https://stepik.org/lesson/265122/step/15?unit=246071
#Дано натуральное число. Напишите программу, которая вычисляет:
#сумму его цифр;
#количество цифр в нем;
#произведение его цифр;
#среднее арифметическое его цифр;
#его первую цифру;
#сумму его первой и последней цифры.
num = int(input())
sum_digit = 0
length_digit = len(str(num))
first_digit = (num // 10 ** (length_digit-1) % 10)
sum_extreme = first_digit + (num % 10)
mul_digit = 1
while num > 0:
    current_digit = num % 10
    sum_digit = current_digit + sum_digit
    mul_digit = current_digit * mul_digit
    num //= 10
print(sum_digit)
print(length_digit)
print(mul_digit)
print(sum_digit/length_digit)
print(first_digit)
print(sum_extreme)

#https://stepik.org/lesson/265122/step/16?unit=246071
#Дано натуральное число n(n>9).
# Напишите программу, которая определяет его вторую (с начала) цифру.
num = input()
print(num[1])

num = int(input())
length_num = len(str(num))
digit = num // 10 ** (length_num - 2) % 10
print(digit)

#https://stepik.org/lesson/265122/step/17?unit=246071
#Дано натуральное число.
# Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
digit = num % 10
flag = True
for digit_char in str(num):
    if int(digit_char) == digit:
        flag = True
    else:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')

#AI
num = input()
if all(digit == num[0] for digit in num):
    print('YES')
else:
    print('NO')
    
num = input()  # оставляем строкой, не конвертируем в int
first_digit = num[0]  # берём первую цифру как эталон
for digit in num:
    if digit != first_digit:
        print('NO')
        break
else:  # ← выполнится, если цикл не прервался через break
    print('YES')

#https://stepik.org/lesson/265122/step/18?unit=246071
#Дано натуральное число.
# Напишите программу, которая определяет, является ли последовательность
# его цифр при просмотре справа налево упорядоченной по неубыванию.
num = int(input())
last_digit = num % 10
num //= 10
while num > 0:
    digit = num % 10
    if digit < last_digit:
        print('NO')
        break
    last_digit = digit
    num //= 10
else:
    print('YES')

#https://stepik.org/lesson/265122/step/19?unit=246071
#На вход программе подаётся натуральное число n.
# Напишите программу, которая выводит для каждой четной
# цифры данного числа текст в следующем формате:
num = int(input())
count = 1
for digit in str(num):
    if int(digit) % 2 == 0:
        print(count,'-я четная цифра равна ',digit, sep='')
        count += 1
        num //= 10
if count == 1:
    print('Четных цифр в числе нет')

#https://stepik.org/lesson/265122/step/20?unit=246071 Глоссарий


#25/03/2026
#break, continue, else
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа
if flag:  # эквивалентно if flag == True:
    print('Число простое')
else:
    print('Число составное')

result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)

for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)

num = 8673
while num != 0:
    last_digit = num % 10
    num //= 10
    if 2 <= last_digit <= 6:
        continue
    print(last_digit)

for i in range(10):
    print(i, end='*')
    if i > 6:
        break

n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')

mult = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i % 9 == 0:
        break
    mult *= i
print(mult)

#https://stepik.org/lesson/298794/step/12?unit=280621
#На вход программе подаётся число n(n>1).
# Напишите программу, которая выводит его наименьший отличный от 1 делитель.
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break

#https://stepik.org/lesson/298794/step/13?unit=280621
#На вход программе подаётся натуральное число n.
# Напишите программу, которая выводит числа от 1 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.
n = int(input())
for i in range(1, n + 1):
    if i in range(5,10) or i in range(17,38) or i in range(78,88):
        continue
    print(i)

num = 3
total = 0
for i in range(num):
    if i % 2 == i:
        total += 1
else:
    print(total)
print(total + 1)

num = 4
while num < 10:
    num += 2
    print(num)
else:
    print('Цикл завершен.')

num = 7
while num < 12:
    num += 2
    if num == 11:
        break
    print(num)
else:
    print('Цикл завершен.')

num = 2
while True:
    num += 1
    if num >= 5:
        break
    print(num)
else:
    print('Цикл завершен.')


#26/03/2026
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:
        flag = False
if num == 1:
    print('Число равно 1')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')
    
num = int(input())
flag = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
if num == 1:
    print('Число равно 1')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')

#https://stepik.org/lesson/311433/step/5?unit=293861
while True:
    answer = input()
    if answer ==  'Python':
        print('Молодец! Вы получили 5 баллов за задачу!')
        break
    else:
        print('Неверно! Попробуйте еще раз.')

#https://stepik.org/lesson/311433/step/7?unit=293861
#На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран произведение цифр введённого числа.
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 3).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
product = n % 10
while n >= 10:
    n //= 10
    digit = n % 10
    product = product * digit
print(product)

#https://stepik.org/lesson/311433/step/8?unit=293861
#На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран его первую (старшую) цифру.
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 2).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
while n >= 10:
    n //= 10
print(n)

#https://stepik.org/lesson/311433/step/9?unit=293861
#На обработку поступает последовательность из 7 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности.
# Если таких чисел нет, программа должна вывести 0.
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)

#https://stepik.org/lesson/311433/step/10?unit=293861
#На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая выводит на экран количество
# неотрицательных чисел последовательности и их произведение.
# Если неотрицательных чисел нет, требуется вывести на экран «NO» (без кавычек).
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
count = 0
p = 1
for i in range(0, 10):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

#https://stepik.org/lesson/311433/step/11?unit=293861
#На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3.
# Если в числе нет цифр, кратных 3, требуется на экран вывести «NO» (без кавычек).
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 5).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

#https://stepik.org/lesson/311433/step/12?unit=293861
#В свободное от модерации курсов время Сэм пишет спам-ботов на заказ.
# Для каждого бота он формирует никнейм по простому (но странному) алгоритму.
# Сначала Сэм вводит стартовую строку – произвольное имя.
# Дальше, пока длина строки меньше 10 символов, он повторяет правило:
# если текущая длина строки кратна 4, прибавляет справа символ x
# иначе, если текущая длина строки кратна 5, прибавляет справа символ y
# в противном случае прибавляет слева символ z
# В конце Сэм добавляет слева символ @ и завершает формирование никнейма.
# Перед вами программа, которая частично реализует алгоритм Сэма, но содержит ошибки.
# Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 5),
# так, чтобы она правильно формировала никнейм по алгоритму Сэма.
s = input()
while len(s) < 10:
    if len(s) % 4 == 0:
        s = s + 'x'
    elif len(s) % 5 == 0:
        s = s + 'y'
    else:
        s = 'z' + s
s = '@' + s
print(s)

#https://stepik.org/lesson/311433/step/13?unit=293861
#Майк и Дастин обмениваются цифровыми сообщениями через приёмник.
# Каждое сообщение представляет собой целое число.
# Майк и Дастин договорились, что последнее сообщение будет оканчиваться на 11, после него переписка прекращается.
# Лукас перехватывает сообщения Майка и Дастина и хочет посчитать, у скольких из них длина более 7 символов.
# Для этого Лукас написал программу, однако допустил в ней несколько ошибок из-за того,
# что прогуливал уроки информатики в школе.
# Исправьте программу Лукаса так, чтобы она корректно находила количество
# сообщений длиной более 7 символов и выводила текст в следующем виде:
# Примечание 1. Лукас не знает, сколько ошибок он допустил. ☹️
# Примечание 2. Последнее сообщение также нужно учитывать при подсчёте сообщений длиной более
# 7 символов и общего количества сообщений.
num = 0
cnt = 0
total = 0
while num % 100 != 11:
    num = int(input())
    if len(str(num)) > 7:
        cnt += 1
    total += 1
print(cnt, '/', total, sep='')

#https://stepik.org/lesson/311433/step/14?unit=293861
#На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Известно, что вводимые числа по абсолютной величине не превышают 10**6.
# Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и
# максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO» (без кавычек).
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 5).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
max_num = -999999
s = 0
for i in range(10): #1
    x = int(input())
    if x < 0:
        s += x #2
        if x > max_num:
            max_num = x
if s != 0: #3
    print(s)
    print(max_num)
else:
    print('NO')


#27/03/2026
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

for i in range(8):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(2):
    for j in range(3):
        print('C' * i + '+' * j)

for i in range(1, 2):
    print(i * 'C')
    for j in range(2, 4):
        print(j * '♨️')
    for k in range(3, 1, -1):
        print(k * '🐳')
print('#')

for i in range(1, 3):
    for j in range(1, 3):
        print(i * '🐍' + j * '🐝')
    print(i * '🦀')

for i in range(1, 4):
    for j in range(3, 6):
        print(i, j)

for i in range(2):
    print(i, end='*')
    for j in range(2):
        print('/', end='+')

for i in range(2):
    for j in range(2):
        print('*', end='#')
    for k in range(3):
        print('%', end='&')
    print()

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')

counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)

#https://stepik.org/lesson/298795/step/10?unit=280622
#Дано натуральное число n(n≤9).
# Напишите программу, которая печатает таблицу размером n×3, состоящую из данного числа (числа отделены одним пробелом).
n = int(input())
for i in range(n):
    for k in range(3):
        print(n, end=' ')
    print()

#https://stepik.org/lesson/298795/step/11?unit=280622
#Дано натуральное число n(n≤9).
# Напишите программу, которая печатает таблицу размером n×5,
# где в i-ой строке указано число i (числа отделены одним пробелом).
n = int(input())
for i in range(1, n+1):
    for k in range(5):
        print(i, end=' ')
    print()

#https://stepik.org/lesson/298795/step/12?unit=280622
#Дано натуральное число n(n≤9).
# Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n(включительно) в соответствии с примером.
n = int(input())
for i in range(1, n + 1):
    for k in range(1, 10):
        print(i, '+', k, '=', i + k)
    print()

#https://stepik.org/lesson/298795/step/13?unit=280622
#Дано натуральное число n.
# Напишите программу, которая печатает численный треугольник в соответствии с примером:
n = int(input())
for m in range(1, n+1):
    for k in range(m,m+1):
        print(str(k) * k, end='\n')

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end="")
    print()

#https://stepik.org/lesson/298795/step/14?unit=280622
#Дано нечётное натуральное число n.
# Напишите программу, которая печатает равнобедренный звёздный треугольник с основанием, равным n, в соответствии с примером:
n = int(input())
for i in range(1, n+1):
        if i <= (n+1)/2:
            for j in range(i):
                print('*', end="")
            print()
        else:
            for g in range((n+1)-i):
                print('*', end="")
            print()
            
#Stepik
n = int(input())
for i in range(n):
    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
    for j in range(cur_cnt):
        print("*", end="")
    print()


#30/03/2026
total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Общее количество натуральных решений =', total)

total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)

#https://stepik.org/lesson/298795/step/16?unit=280622
#Решите уравнение в натуральных числах 28n+30k+31m=365
total = 0
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)

#https://stepik.org/lesson/298795/step/17?unit=280622
#Сколько быков, коров и телят можно купить ровно на 100 рублей, если
# плата за быка – 10 рублей,
# за корову – 5 рублей,
# за телёнка – 0.5 рубля и надо купить
# 100 голов скота?
total = 0
for b in range(1, 10):
    for k in range(1, 20):
        for t in range(1, 200):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
                total += 1
                print('b =', b, 'k =', k, 't =', t)
print('Общее количество натуральных решений =', total)

#Гипотеза Эйлера о сумме степеней
total = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        total += 1
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
                        print(a + b + c + d + e)
print('Общее количество натуральных решений =', total)

total = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                # Вычисляем левую часть один раз
                left_sum = a**5 + b**5 + c**5 + d**5
                for e in range(1, 150):
                    if left_sum == e**5:
                        total += 1
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
                        print(a + b + c + d + e)
print('Общее количество натуральных решений =', total)

total = 0
max_val = 149
# Используем a <= b <= c <= d, чтобы не проверять перестановки
for a in range(1, max_val + 1):
    for b in range(a, max_val + 1):  # b начинается с a
        for c in range(b, max_val + 1):  # c начинается с b
            for d in range(c, max_val + 1):  # d начинается с c
                left_sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
                if left_sum > max_val ** 5:
                    continue
                for e in range(1, max_val + 1):
                    if left_sum == e ** 5:
                        total += 1
                        print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
                        print(f'Сумма = {a + b + c + d + e}')
print('Общее количество натуральных решений =', total)

total = 0
max_val = 149

# Предвычисляем степени
powers = [0] * (max_val + 1)
for i in range(1, max_val + 1):
    powers[i] = i ** 5

# Используем симметрию и ограничения
for a in range(1, max_val + 1):
    for b in range(a, max_val + 1):
        for c in range(b, max_val + 1):
            for d in range(c, max_val + 1):
                left_sum = powers[a] + powers[b] + powers[c] + powers[d]

                # Если сумма больше максимальной степени, дальше можно не искать
                if left_sum > powers[max_val]:
                    continue

                # Ищем e (можно использовать while или просто проверить все)
                for e in range(1, max_val + 1):
                    if left_sum == powers[e]:
                        total += 1
                        print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
                        print(f'Сумма = {a + b + c + d + e}')
                        break  # нашли, дальше не ищем

print(f'Общее количество натуральных решений = {total}')

total = 0
max_val = 149
# Предвычисляем степени
powers = [0] * (max_val + 1)
for i in range(1, max_val + 1):
    powers[i] = i ** 5
sums_list = []  # Список для хранения всех сумм
for a in range(1, max_val + 1):
    for b in range(a, max_val + 1):
        for c in range(b, max_val + 1):
            for d in range(c, max_val + 1):
                left_sum = powers[a] + powers[b] + powers[c] + powers[d]
                if left_sum > powers[max_val]:
                    continue
                for e in range(1, max_val + 1):
                    if left_sum == powers[e]:
                        total += 1
                        numbers_sum = a + b + c + d + e
                        sums_list.append(numbers_sum)
                        print(f'Решение #{total}: ({a}, {b}, {c}, {d}, {e})')
                        print(f'Сумма = {numbers_sum}')
                        print('-' * 40)
                        break
print(f'\nОбщее количество решений = {total}')
if sums_list:
    print(f'Минимальная сумма = {min(sums_list)}')
    print(f'Максимальная сумма = {max(sums_list)}')
    print(f'Средняя сумма = {sum(sums_list) / len(sums_list):.2f}')

#https://stepik.org/lesson/298796/step/1?unit=280623
#На вход программе подаётся натуральное число n.
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов +, сколько делителей у этого числа.
n = int(input())
count = 0
for i in range(1, n + 1):
    print(i,end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end='')
    print()

#https://stepik.org/lesson/298796/step/2?unit=280623
#Дано натуральное число n.
# Напишите программу, которая печатает численный треугольник с высотой, равной n, в соответствии с примером:
n = int(input())
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num,sep=' ',end=' ')
        num += 1
    print()

#https://stepik.org/lesson/298796/step/3?unit=280623
#На вход программе подается два натуральных числа a и b(a<b)
# Напишите программу, которая находит все простые числа от a до b включительно
a, b = int(input()), int(input())
for i in range(a, b+1):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

#https://stepik.org/lesson/298796/step/4?unit=280623
#Дано натуральное число n.
# Напишите программу, которая выводит значение суммы
n = int(input())
factorial = 1
s = 0
for i in range(1, n+1):
    factorial *= i
    s += factorial
print(s)

n = int(input())
s = 0
for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    s += factorial
print(s)

#https://stepik.org/lesson/298796/step/5?unit=280623
#На вход программе подаются натуральные числа n и m.
# Под эмодзи 🍌, 💎, 🦌 спрятаны целые числа от 1 до n (не включительно).
# Имеется следующий ребус
n, m = int(input()), int(input())
flag = True
for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a + b * 3 + c * 2 == m:
                print(a, ' + 3×',b, ' + 2×',c, ' = ', m, sep='')
                flag = False
if flag:
    print('При заданных n и m решений не существует.')


#31/03/2026

# #https://stepik.org/lesson/298796/step/6?unit=280623
a, b = int(input()), int(input())
max_sum = 0
max_dividend = 0
for i in range(a, b+1):
    sum_divider = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum_divider += j
            #print('i =', i, 'j =', j, sum_divider)
    if sum_divider >= max_sum:
        max_dividend = i
        max_sum = sum_divider
print(max_dividend, max_sum)

#https://stepik.org/lesson/298796/step/7?unit=280623
#Дано натуральное число n.
# Напишите программу, которая печатает численный треугольник с высотой, равной n, в соответствии с примером
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j,end='')
    for g in range(i-1, 0, -1):
        print(g,end='')
    print()

#https://stepik.org/lesson/298796/step/8?unit=280623
#На вход программе подаётся натуральное число n.
# Найдите все моменты времени, для которых выполняется данная формула,
# и выведите их в порядке возрастания в формате hh:mm, каждый на отдельной строке.
# Программа должна вывести в формате hh:mm все моменты времени в соответствии с условием задачи.
n = int(input())
for hours in range(0, 24):
    for minutes in range(0, 60):
        if hours ** n == minutes:
            print(f"{hours:02d}:{minutes:02d}")
#Stepik
n = int(input())
for h in range(24):
    for m in range(60):
        if h**n == m:
            if h < 10:
                h = '0' + str(h)
            if m < 10:
                m = '0' + str(m)
            print(h, m, sep=':')
            h, m = int(h), int(m)

#https://stepik.org/lesson/298796/step/9?unit=280623
#Цифровым корнем числа n называется число, получающееся следующим образом:
# вычисляется сумма цифр числа n, затем сумма цифр у получившегося числа и так далее,
# пока не получится однозначное число. Например, цифровой корень числа 9875 равен 2:
n = int(input())
if n < 10:
    print(n)
else:
    while n >= 10:
        current_number = 0
        while n:
            current_digit = n % 10
            n //= 10
            current_number += current_digit
        n = current_number
    print(current_number)

n = int(input())
#Stepik
while n > 9:
    new_n = 0
    while n > 0:
        new_n += n % 10
        n //= 10
    n = new_n
print(n)


#01/04/2026
#Exam

#Factorial
n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)

#выводит минимальный делитель числа, отличный от единицы - почему?
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

#https://stepik.org/lesson/294080/step/1?unit=275759
#На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа или 0, если чётных цифр в записи нет.
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их может быть одна или несколько).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
s = 0
while n:
    if (n % 10) % 2 == 0:
        s += n % 10
    n//= 10
print(s)

#https://stepik.org/lesson/294080/step/2?unit=275759
n = 8
count = 0
maximum = -1000000000000
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

#https://stepik.org/lesson/294080/step/3?unit=275759
n = 4
count = 0
maximum = -100000000
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

#https://stepik.org/lesson/294080/step/4?unit=275759
#На вход программе подаётся натуральное число n(3≤n≤19).
# Напишите программу, которая печатает звёздную рамку размерами n×19.
n = int(input())
for i in range(1, n+1):
    if i==1 or i== n:
        print('*******************')
    else:
        print('*                 *')
#Stepik
n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        cur_sep = "*"
    else:
        cur_sep = " "
    print("*", "*", sep=cur_sep * 17)

#https://stepik.org/lesson/294080/step/5?unit=275759
#Дано натуральное число n(n>99).
# Напишите программу, которая определяет его третью (с начала) цифру.
n = int(input())
num = 0
while len(str(n)) > 3:
    n //= 10
    print(n)
num = n % 10
print(num)

#https://stepik.org/lesson/294080/step/6?unit=275759
#Дано натуральное число. Напишите программу, которая вычисляет:
# количество цифр 3 в нём;
# сколько раз в нём встречается последняя цифра;
# количество чётных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести её);
# сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
n = int(input())
three = 0
ln = n % 10
last_number = 0
even = 0
bigger_five = 0
bigger_seven = 1
zero_five = 0
while n:
    current_number = n % 10
    if current_number == 3: # количество цифр 3 в нём;
        three += 1
    if current_number % 2 == 0: # количество чётных цифр;
        even += 1
    if current_number > 5: # сумму его цифр, больших пяти;
        bigger_five += current_number
    if current_number > 7: # произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести её);
        bigger_seven *= current_number
        last_bigger_seven = current_number
    if current_number == 0 or current_number == 5: # сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
        zero_five += 1
    n //= 10
    if current_number == ln: # сколько раз в нём встречается последняя цифра;
        last_number += 1
print(three)
print(last_number)
print(even)
print(bigger_five)
print(bigger_seven)
print(zero_five)

#https://stepik.org/lesson/294080/step/7?unit=275759

#AI
def find_taxi_numbers(n):
    found = []
    num = 1
    while len(found) < n:
        ways = []
        limit = int(num ** (1 / 3)) + 1
        for a in range(1, limit):
            for b in range(a, limit):
                if a ** 3 + b ** 3 == num:
                    ways.append((a, b))
        if len(ways) >= 2:
            found.append(num)
            print(f"{len(found)}. {num}")
            for a, b in ways:
                print(f"   {a}³ + {b}³")
        num += 1
    return found
# Находим первые 5 чисел
result = find_taxi_numbers(5)
print("\nПервые 5 чисел Рамануджана:")
print(result)

for a in range(1, 43):
    for b in range(1, 43):
        for c in range(1, 43):
            for d in range(1, 43):
                if a != b and b != c and c != d and a!=c and a!=d and pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                    print(pow(a, 3) + pow(b, 3))


#02/04/2026
s = 'All you need is love'
if 'love' in s:
    print('❤️')
else:
    print('💔')

s = 'abcdef'
for i in range(len(s)):
    print(s[i])

s = 'abcdef'
for c in s:
    print(c)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')
#https://stepik.org/lesson/284101/step/5?unit=265440
#https://stepik.org/lesson/284101/step/6?unit=265440
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7],s[-10])

#https://stepik.org/lesson/284101/step/7?unit=265440
#На вход программе подаётся одна строка. 
#Напишите программу, которая выводит элементы строки с чётными индексами
s = input()
for i in range(0, len(s), 2):
    print(s[i])

#https://stepik.org/lesson/284101/step/8?unit=265440
#На вход программе подаётся одна строка.
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
s = input()
for i in range(-1, -len(s)-1, -1):
    print(s[i])

#https://stepik.org/lesson/284101/step/9?unit=265440
#На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке).
# Напишите программу, которая выводит инициалы человека.
#res = ''
s1, s2, s3 = input(), input(), input()
#res = s2[0] + s1[0] + s3[0]
print(s2[0] + s1[0] + s3[0])
#Stepik
a, b, c = input()[0], input()[0], input()[0]
print(b, a, c, sep="")

#https://stepik.org/lesson/284101/step/10?unit=265440
#Персонажи мультфильма «Мадагаскар» планируют побег из Африки.
# Они выстроились в очередь на самолёт, построенный шимпанзе.
# На вход программе подаётся строка из эмодзи-символов – очередь животных на борт самолёта.
# Для каждого животного из очереди вам необходимо вывести его эмодзи и номер в очереди (начиная с 1) в следующем формате:
s = input()
counter = 1
for i in range(0, len(s)):
    print(counter,') ', s[i], sep="")
    counter += 1
#Stepik
queue = input()
for i in range(len(queue)):
    print(i + 1, ') ', queue[i], sep='')

#https://stepik.org/lesson/284101/step/11?unit=265440
#На вход программе подаётся одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки.
s = input()
summa = 0
for i in range(len(s)):
    summa += int(s[i])
print(summa)

#https://stepik.org/lesson/284101/step/12?unit=265440
#На вход программе подаётся одна строка.
# Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру.
# В противном случае вывести сообщение «Цифр нет» (без кавычек).
s = input()
has_digit = False
for digit in '0123456789':
    if digit in s:
        has_digit = True
        break
if has_digit:
    print('Цифра')
else:
    print('Цифр нет')
#Stepik
for i in input():
    if i in '01234567890':
        print("Цифра")
        break
else:
    print("Цифр нет")

#https://stepik.org/lesson/284101/step/13?unit=265440
#На вход программе подаётся одна строка.
# Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *, и выводит текст в следующем формате:
plus = 0
star = 0
for i in input():
    if '+' in i:
        plus += 1
    if '*' in i:
        star += 1
print(f'Символ + встречается {plus} раз')
print(f'Символ * встречается {star} раз')

n = input()
print("Символ + встречается", n.count("+"), "раз")
print("Символ * встречается", n.count("*"), "раз")

#https://stepik.org/lesson/284101/step/14?unit=265440
#На вход программе подаётся одна строка.
# Напишите программу, которая определяет, сколько в ней пар одинаковых соседних символов.
#AI 50/50
s = input()
pairs = 0
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        pairs += 1
print(pairs)

#https://stepik.org/lesson/284101/step/15?unit=265440
#На вход программе подаётся одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных букв и выводит текст в следующем формате:
s = input()
glas = 0
soglas = 0
for i in s:
    i = i.lower()
    if i in 'ауоыиэяюе':
        glas += 1
    if i in 'бвгджзйклмнпрстфхцчшщ':
        soglas +=1
print(f'Количество гласных букв равно {glas}')
print(f'Количество согласных букв равно {soglas}')

#https://stepik.org/lesson/284101/step/16?unit=265440
#На вход программе подаётся натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.
n = int(input())
s = ''
while n:
    current_number = n % 2
    n = n // 2
    s += str(current_number)
for i in range(-1, -len(s)-1, -1):
    print(s[i],end='')

n = int(input())
res = ""
while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)


#03/04/2026
s = 'abcdefghij'
print(s[2:5])
print(s[0:6])
print(s[2:7])

s = s[:4] + 'X' + s[5:]
print(s)

s = 'abcdefg'
print(s[2:5])
s = 'abcdefg'
print(s[3:])
s = 'abcdefg'
print(s[:3])
s = 'abcdefg'
print(s[:])

s = 'abcdefg'
print(s[::-3])

#https://stepik.org/lesson/302627/step/11?unit=284520
#На вход программе подаётся одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет, является ли оно палиндромом.
s = input()
if s == s[::-1]:
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/302627/step/12?unit=284520
#На вход программе подаётся одна строка. Напишите программу, которая выводит:
#общее количество символов в строке;
#исходную строку, повторённую 3 раза;
#первый символ строки;
#первые три символа строки;
#последние три символа строки;
#строку в обратном порядке;
#строку с удалённым первым и последним символами.
s = input()
print(len(s))   #общее количество символов в строке;
print(s*3)      #исходную строку, повторённую 3 раза;
print(s[:1])    #первый символ строки;
print(s[:3])    #первые три символа строки;
print(s[-3:])    #последние три символа строки;
print(s[::-1])  #строку в обратном порядке;
print(s[1:-1])  #строку с удалённым первым и последним символами.

#https://stepik.org/lesson/302627/step/13?unit=284520
#На вход программе подаётся одна строка. Напишите программу, которая выводит
#третий символ этой строки;
#предпоследний символ этой строки;
#первые пять символов этой строки;
#всю строку, кроме последних двух символов;
#все символы с чётными индексами;
#все символы с нечётными индексами;
#все символы в обратном порядке;
#все символы строки через один в обратном порядке, начиная с последнего.
s = input()
print(s[2:3])  #третий символ этой строки;
print(s[-2:-1])    #предпоследний символ этой строки;
print(s[:5])    #первые пять символов этой строки;
print(s[:-2])    #всю строку, кроме последних двух символов;
print(s[::2])    #все символы с чётными индексами;
print(s[1::2])    #все символы с нечётными индексами;
print(s[::-1])    #все символы в обратном порядке;
print(s[::-2])    #все символы строки через один в обратном порядке, начиная с последнего.

#https://stepik.org/lesson/302627/step/14?unit=284520
#На вход программе подаётся строка текста.
# Напишите программу, которая разрежет её на две равные части, переставит их местами и выведет на экран.
import math
s = input()
if len(s) == 1:
    print(s)
else:
    print(s[math.ceil(-len(s)/2)::] + s[:math.ceil(len(s)/2):])
#Stepik
s = input()
n = len(s)
a = s[:(n + 1) // 2]
b = s[(n + 1) // 2:]
print(b + a)


 #06/04/2026
s = 'foo123#BAR#.'
print(s.capitalize())

s = 'the sun also rises'
print(s.title())

s = 'FOO Bar 123 baz qUX'
print(s.lower())

s = 'FOO Bar 123 baz qUX'
print(s.upper())

s1 = 'a'
s2 = s1.upper()
print(s1, s2)

#https://stepik.org/lesson/296416/step/10?unit=278136
#На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом. 
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
s = input()
s1 = s.title()
if s == s1:
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/296416/step/11?unit=278136
#На вход программе подаётся строка.
# Напишите программу, которая меняет регистр символов – заменяет все строчные символы заглавными и наоборот.
s = input()
print(s.swapcase())

#https://stepik.org/lesson/296416/step/12?unit=278136
#На вход программе подаётся строка текста.
# Напишите программу, которая определяет, является ли оттенок текста хорошим или нет.
# Текст имеет хороший оттенок, если содержит подстроку «хорош» (без кавычек) во всевозможных регистрах.
s = input()
if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/296416/step/13?unit=278136
#На вход программе подаётся строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
s = input()
counter = 0
for c in s:
    if c.isalpha() and c.lower() == c:
        counter += 1
print(counter)
#Stepik
s = input()
cnt_al_lower = 0
for el in s:
    if el != el.upper():
        cnt_al_lower += 1
print(cnt_al_lower)

#Метод capitalize() возвращает копию строки s, в которой первый символ имеет верхний регистр, а все остальные символы имеют нижний регистр.
#✅ Метод swapcase() возвращает копию строки s, в которой все символы, имеющие верхний регистр, преобразуются в символы нижнего регистра и наоборот.
#✅ Метод title() возвращает копию строки s, в которой первый символ каждого слова переводится в верхний регистр.
#✅ Метод lower() возвращает копию строки s, в которой все символы имеют нижний регистр.
#✅ Метод upper() возвращает копию строки s, в которой все символы имеют верхний регистр.
#✅ Строковые методы не изменяют исходную строку: вместо этого они возвращают новую строку.


#07/04/2026

#Методы count()
#Метод startswith() startswith(<prefix>, <start>, <end>)
#Метод endswith()
#Метод find()
#Метод rfind()
#Метод index()
#Метод rindex()
#Метод strip()
#Метод lstrip()
#Метод rstrip()
#Метод replace()

s = 'foo goo moo'
print(s.count('oo')) #3
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ #2

s = 'foobar'
print(s.startswith('foo')) #True
print(s.startswith('baz')) #False

s = 'foobar'
print(s.endswith('bar'))    #True
print(s.endswith('baz'))    #False

s = 'foo bar foo baz foo qux'
print(s.find('foo'))    #0
print(s.find('bar'))    #4
print(s.find('qu'))     #20
print(s.find('python')) #-1

s = '     foo bar foo baz foo qux      '    #foo bar foo baz foo qux
print(s.strip())

s = '     foo bar foo baz foo qux      '
print(s.lstrip())                           #foo bar foo baz foo qux⎵⎵⎵⎵⎵⎵

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))   #grault bar grault baz grault qux

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))    #grault bar grault baz foo qux

s = '-+-+abc+-+-'
print(s.strip('+-'))    #abc
print(s.rstrip('+-'))   #-+-+abc
print(s.lstrip('+-'))   #abc+-+-

s = 'https://pygen.ru'
print(s.endswith('.ru') == True)
s = 'https://pygen.ru'
print(s.endswith('.ru'))

s = 'aabbAAccDDaa'
s = s.lower()
print(s.count('a')) #6

s = 'www.stepik.org'
print(s.startswith('www')) #True

s = 'www.stepik.org'
print(s.endswith('.ru')) #False

s = 'I learn Python language. Python - awesome!'
print(s.find('Python')) #8

s = '     I learn Python language               '
print(s.strip())

s = 'abcdababa'
print(s.replace('ab', '123'))

#https://stepik.org/lesson/303083/step/8?unit=284990
#На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.

s = input()
print(s.count(' ')+ 1)

#https://stepik.org/lesson/303083/step/9?unit=284990
#На вход программе подаётся строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин) и Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина,
# гуанина, цитозина и тимина входит в данную строку генетического кода.
s = input()
a = s.count('а')
a1 = s.count('А')
print('Аденин:', a + a1)
g = s.count('Г')
g1 = s.count('г')
print('Гуанин:', g + g1)
c = s.count('Ц')
c1 = s.count('ц')
print('Цитозин:', c + c1)
t = s.count('Т')
t1 = s.count('т')
print('Тимин:', t + t1)

#Stepik
genetic_code = input().upper()            # Ввод строки генетического кода
adenine_count = genetic_code.count("А")   # Подсчет количества аденина
guanine_count = genetic_code.count("Г")   # Подсчет количества гуанина
cytosine_count = genetic_code.count("Ц")  # Подсчет количества цитозина
thymine_count = genetic_code.count("Т")   # Подсчет количества тимина

# Вывод результатов
print("Аденин:", adenine_count)
print("Гуанин:", guanine_count)
print("Цитозин:", cytosine_count)
print("Тимин:", thymine_count)

#https://stepik.org/lesson/303083/step/10?unit=284990
#Джим Хоппер с помощью радиоприёмника пытается получить сообщение Оди.
# На приёмник ему поступает n различных последовательностей кода Морзе.
# Декодировав их, он получает последовательности из цифр и букв строчного латинского алфавита.
# При этом только в сообщениях Оди содержится число 11, причём минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.
n = int(input())
messages = 0
for _ in range(n):
    counter = 0
    s = input()
    counter += s.count('11')
    if counter >= 3:
        messages += 1
print(messages)

#Stepik
n = int(input())
cnt = 0
for _ in range(n):
    message = input()
    if message.count("11") >= 3:
        cnt += 1
print(cnt)

#https://stepik.org/lesson/303083/step/11?unit=284990
#На вход программе подаётся строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.
s = input()
s_without_digits = s
for digit in '0123456789':
    s_without_digits = s_without_digits.replace(digit, '')
print(len(s) - len(s_without_digits))

#Stepik
text = input()
cnt = 0
for i in range(10):
    cnt += text.count(str(i))
print(cnt)

#https://stepik.org/lesson/303083/step/12?unit=284990
#На вход программе подаётся строка текста.
# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
s = input()
if s.endswith('.ru') or s.endswith('.com'):
    print('YES')
else:
    print('NO')

#https://stepik.org/lesson/303083/step/13?unit=284990
#На вход программе подаётся строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
s = input()
m = 0
l = ''
for i in s:
    count = 0
    count += s.count(i)
    if count >= m:
        m = count
        l = i
print(l)
#Stepik
s = input()
most_common = s[0]
for el in s:
    if s.count(el) >= s.count(most_common):
        most_common = el
print(most_common)

#https://stepik.org/lesson/303083/step/14?unit=284990
#На вход программе подаётся строка текста.
# Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раза, выведите индексы её первого и последнего вхождения на одной строке,
# разделённые символом пробела.
# Если буква «f» в данной строке не встречается, следует вывести «NO» (без кавычек).
s = input()
if s.find('f') == -1:
    print('NO')
elif s.find('f') == s.rfind('f'):
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))

#https://stepik.org/lesson/303083/step/15?unit=284990
#На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.
s = input()
f = s.find('h')
l = s.rfind('h')
if f == l == -1:
    print(s)
else:
    print(s[:f]+s[(l+1):])

"""""
#08/04/2026
