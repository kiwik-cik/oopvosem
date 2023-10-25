class Quadrilateral:
    def __init__(self, width, height=None):
        if height is None:
            # Если передан только один аргумент, делаем квадрат
            self.width = width
            self.height = width
        else:
            # Если передано два аргумента, делаем прямоугольник
            self.width = width
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f"Квадрат размером {self.width}x{self.height}"
        else:
            return f"Прямоугольник размером {self.width}x{self.height}"

    def __bool__(self):
        return self.width == self.height


# Пример использования:
square = Quadrilateral(5)
print(square)  # Квадрат размером 5x5
print(bool(square))  # True

rectangle = Quadrilateral(4, 6)
print(rectangle)  # Прямоугольник размером 4x6
print(bool(rectangle))  # False