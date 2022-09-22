#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q, "black")


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first(), "black")
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

try:
    Figure.get_square()
    print("\nВведите координаты точек выпуклой оболочки")
    while True:
        f = f.add(R2Point())
        tk.clean()

        r = "red"
        tk.draw_line(Figure.p1, Figure.p2, r)
        tk.draw_line(Figure.p2, Figure.p3, r)
        tk.draw_line(Figure.p3, Figure.p4, r)
        tk.draw_line(Figure.p4, Figure.p1, r)

        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, a = {f.summary_angle()}\n")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
