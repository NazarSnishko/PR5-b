import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

class Triangle:
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

    def perimeter(self):
        return self.line1.length() + self.line2.length() + self.line3.length()

# Введення координат точок від користувача
x1, y1 = map(float, input("Введіть координати точки 1 (x y): ").split())
x2, y2 = map(float, input("Введіть координати точки 2 (x y): ").split())
x3, y3 = map(float, input("Введіть координати точки 3 (x y): ").split())

# Створення об'єктів Point
point1 = Point(x1, y1)
point2 = Point(x2, y2)
point3 = Point(x3, y3)

# Створення об'єктів Line
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# Створення об'єкта Triangle
triangle = Triangle(line1, line2, line3)

# Виведення результату
print("Периметр трикутника:", triangle.perimeter())
