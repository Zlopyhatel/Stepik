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
"""""
