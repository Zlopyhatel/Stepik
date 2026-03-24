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
"""""
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


