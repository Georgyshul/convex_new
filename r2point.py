from math import sqrt, acos, pi


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

    # Угол пересечения двух векторов
    @staticmethod
    def angle(p1, p2, p3, p4):
        if R2Point.intersect(p1, p2, p3, p4):
            a = R2Point(p2.x - p1.x, p2.y - p1.y)
            b = R2Point(p4.x - p3.x, p4.y - p3.y)
            prod = abs(R2Point.dot(a, b))
            angle = acos(prod / (p1.dist(p2) * p3.dist(p4))) * 180 / pi
            return round(angle, 1)
        else:
            return 0.0

    # Пересекаются ли два отрезка?
    @staticmethod
    def intersect(p1, p2, p3, p4):
        d1 = R2Point.area(p3, p4, p1)
        d2 = R2Point.area(p3, p4, p2)
        d3 = R2Point.area(p1, p2, p3)
        d4 = R2Point.area(p1, p2, p4)

        if d1 * d2 < 0 and d3 * d4 < 0:
            return True
        elif d1 == 0 and p1.is_inside(p3, p4):
            return True
        elif d2 == 0 and p2.is_inside(p3, p4):
            return True
        elif d3 == 0 and p3.is_inside(p1, p2):
            return True
        elif d4 == 0 and p4.is_inside(p1, p2):
            return True
        else:
            return False

    @staticmethod
    def intersect_square(p, q, a, b, c, d):
        angle = R2Point.angle(p, q, a, b)
        angle += R2Point.angle(p, q, b, c)
        angle += R2Point.angle(p, q, c, d)
        angle += R2Point.angle(p, q, d, a)
        return angle

    # Скалярное произведение двухмерных векторов
    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y

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
    print(R2Point.angle(p1, p2, p3, p4))
