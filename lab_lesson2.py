# Реализуйте рекурсивную функцию нарезания прямоугольника с
# заданными пользователем сторонами a и b на квадраты с
# наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и
# кол-во полученных квадратов.

#import sys
#sys.setrecursionlimit(10000)

def digit_check(digit):
    while (not digit.isdigit()) or (("0" in digit) == True):
        if ("0" in digit) == True:
            print("Вы ввели 0! Попытайтесь еще раз...")
        elif ("-" in digit) == True:
            print("Вы ввели отрицатльное! Попытайтесь еще раз...")
        elif(not digit.isdigit()):
            print("Вы ввели не число! Попытайтесь еще раз...")
        digit = input("\n")


a_side = input("Введите длинну стороны a : \n ")
digit_check(a_side)
b_side = input("Введите длинну стороны b: \n ")
digit_check(b_side)
side_length = []


def check(a, b):
    if a == b:
        side_length.append(a)
        return 1
    if a > b:
        side_length.append(b)
        return check(a - b, b)
    side_length.append(a)
    return check(a, b - a)


check(int(a_side), int(b_side))
counter = 1
for i in side_length:
    print("Длина стороны", counter, "-го квадрата :", i, '\n')
    counter += 1
print("Количество квадратов:", counter - 1)
