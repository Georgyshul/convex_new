#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

def get_square():
    print("Введите координаты двух диагональных точек квадрата")
    a = R2Point()
    b = R2Point()
    c = R2Point(a.x, b.y)
    d = R2Point(b.x, a.y)
    return a, b, c, d

f = Void()
try:
    get_square()
    print("Введите координаты точек выпуклой оболочки")
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, a = {f.summary_angle()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
