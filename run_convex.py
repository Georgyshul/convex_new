#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void

f = Void()
try:
    Figure.get_square()
    print("Введите координаты точек выпуклой оболочки")
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, a = {f.summary_angle()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
