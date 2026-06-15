
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        # Порівнюю площі двох прямокутників
        return self.get_square() == other.get_square()

    def __add__(self, other):
        # Обчислюю нову сумарну площу
        new_square = self.get_square() + other.get_square()
        # Повертаю новий екземпляр, - щоб площа зійшлася, беру сторони 1 та new_square
        return Rectangle(1, new_square)

    def __mul__(self, n):
        # Збільшую площу поточного прямокутника в n разів
        new_square = self.get_square() * n
        # Так само повертаю новий екземпляр зі сторонами 1 та new_square
        return Rectangle(1, new_square)

    def __str__(self):
        # Роблю гарний вивід для прінта (необов'язково для assert, але хороший тон)
        return f"Прямокутник зі сторонами {self.width} та {self.height} (Площа: {self.get_square()})"

# Перевіряю що вийшло
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("Всі тести пройдено успішно!")
