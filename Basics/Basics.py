from math import sqrt
import sys, os
try:
    a = int(input("Напишите длину первой стороны треугольника: "))
    b = int(input("Напишите длину второй стороны треугольника: "))
    c = int(input("Напишите длину третьей стороны треугольника: "))
except (TypeError, ValueError):
    print("Не является числом")
try:
    if a+b<=c:
        print("Это не треугольник")
    elif a+c<=b:
        print("Это не треугольник")
    elif b+c<=a:
        print("Это не треугольник")
    elif a+b>=c:
        p = (a + b + c) / 2
        x = p * (p - a) * (p - b) * (p - c)
        S = sqrt(x)
        print("Площадь этого треугольник:  " );print(S)
except(NameError):
    print("")