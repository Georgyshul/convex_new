from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Угол пересечения двух отрезков
    # Если не пересекаются, возвращаемая величина 0
    @staticmethod
    def intersect(p1, p2, p3, p4):
        d1 = R2Point.area(p3, p4, p1)
        d2 = R2Point.area(p3, p4, p2)
        d3 = R2Point.area(p1, p2, p3)
        d4 = R2Point.area(p1, p2, p4)

        if d1 * d2 < 0 and d3 * d4 < 0:
           return 1
        elif d1 == 0 and R2Point.on_segment(p3, p4, p1):
           return 1
        elif d2 == 0 and R2Point.on_segment(p3, p4, p2):
           return 1
        elif d3 == 0 and R2Point.on_segment(p1, p2, p3):
           return 1
        elif d4 == 0 and R2Point.on_segment(p1, p2, p4):
            return 1
        else:
            return 0

    @staticmethod
    def on_segment(a, b, c):
        return (min(a.x, b.x) <= c.x <= max(a.x, b.x)
               and min(a.y, b.y) <= c.y <= max(a.y, b.y))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == "__main__":
    p1, p2, p3, p4 = R2Point(), R2Point(), R2Point(), R2Point()

    print(R2Point.intersect(p1, p2, p3, p4))
