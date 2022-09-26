#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void


def get_square():
    print("Введите координаты двух диагональных точек прямоугольника:")
    Figure.p1 = R2Point()
    Figure.p3 = R2Point()
    Figure.p2 = R2Point(Figure.p1.x, Figure.p3.y)
    Figure.p4 = R2Point(Figure.p3.x, Figure.p1.y)


f = Void()
try:
    get_square()
    print("Введите координаты точек выпуклой оболочки")
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, "
              f"a = {round(f.summary_angle(), 1)}\n"
              )
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
