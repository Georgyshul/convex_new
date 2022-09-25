from pytest import approx
from math import sqrt
from r2point import R2Point


class TestR2Point:

    # Расстояние от точки до самой себя равно нулю
    def test_dist1(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(1.0, 1.0)) == approx(0.0)

    # Расстояние между двумя различными точками положительно
    def test_dist2(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(1.0, 0.0)) == approx(1.0)

    def test_dist3(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(0.0, 0.0)) == approx(sqrt(2.0))

    # Площадь треугольника равна нулю, если все вершины совпадают
    def test_area1(self):
        a = R2Point(1.0, 1.0)
        assert R2Point.area(a, a, a) == approx(0.0)

    # Площадь треугольника равна нулю, если все вершины лежат на одной прямой
    def test_area2(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 1.0), R2Point(2.0, 2.0)
        assert R2Point.area(a, b, c) == approx(0.0)

    # Площадь треугольника положительна при обходе вершин против часовой
    # стрелки
    def test_area3(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.area(a, b, c) > 0.0

    # Площадь треугольника отрицательна при обходе вершин по часовой стрелке
    def test_area4(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.area(a, c, b) < 0.0

    # Точки могут лежать внутри и вне "стандартного" прямоугольника с
    # противопложными вершинами (0,0) и (2,1)
    def test_is_inside1(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 0.5).is_inside(a, b) is True

    def test_is_inside2(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 0.5).is_inside(b, a) is True

    def test_is_inside3(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 1.5).is_inside(a, b) is False

    # Ребро [(0,0), (1,0)] может быть освещено или нет из определённой точки
    def test_is_light1(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, 0.0).is_light(a, b) is False

    def test_is_light2(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(2.0, 0.0).is_light(a, b) is True

    def test_is_light3(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, 0.5).is_light(a, b) is False

    def test_is_light4(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, -0.5).is_light(a, b) is True

    # Тесты метода intersect
    def test_intersect1(self):
        p1, p2 = R2Point(0.0, 0.0), R2Point(2.0, 2.0)
        p3, p4 = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point.intersect(p1, p2, p3, p4) is True

    def test_intersect2(self):
        p1, p2 = R2Point(0.0, 0.0), R2Point(2.0, 2.0)
        p3, p4 = R2Point(0.0, -1.0), R2Point(1.0, 0.0)
        assert R2Point.intersect(p1, p2, p3, p4) is False

    def test_intersect3(self):
        p1, p2 = R2Point(0.0, 0.0), R2Point(2.0, 2.0)
        p3, p4 = R2Point(-1.0, -1.0), R2Point(3.0, 3.0)
        assert R2Point.intersect(p1, p2, p3, p4) is True

    # Тесты метода angle
    def test_angle1(self):
        p1, p2 = R2Point(0.0, 0.0), R2Point(2.0, 2.0)
        p3, p4 = R2Point(0.0, -1.0), R2Point(1.0, 0.0)
        assert R2Point.angle(p1, p2, p3, p4) == 0

    def test_angle2(self):
        p1, p2 = R2Point(0.0, 0.0), R2Point(2.0, 2.0)
        p3, p4 = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point.angle(p1, p2, p3, p4) == 45.0

    def test_angle3(self):
        p1, p2 = R2Point(0.0, 0.0), R2Point(2.0, 2.0)
        p3, p4 = R2Point(0.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.angle(p1, p2, p3, p4) == 0

    def test_square_angle1(self):
        p, q = R2Point(-1, -1), R2Point(5, 5)
        a, b, c, d = R2Point(0, 0), R2Point(0, 3), R2Point(3, 3), R2Point(3, 0)
        assert R2Point.intersect_square(p, q, a, b, c, d) == 180

    def test_square_angle2(self):
        p, q = R2Point(0, 4), R2Point(5, 5)
        a, b, c, d = R2Point(0, 0), R2Point(0, 3), R2Point(3, 3), R2Point(3, 0)
        assert R2Point.intersect_square(p, q, a, b, c, d) == 0

    def test_square_angle3(self):
        p, q = R2Point(1, 0), R2Point(2, 0)
        a, b, c, d = R2Point(0, 0), R2Point(0, 3), R2Point(3, 3), R2Point(3, 0)
        assert R2Point.intersect_square(p, q, a, b, c, d) == 0
