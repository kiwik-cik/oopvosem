class Vector:
    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])

    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        return "Вектор(" + ", ".join(str(value) for value in self.values) + ")"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[value + other for value in self.values])
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Сложение векторов разной длины недопустимо"
            return Vector(*[self.values[i] + other.values[i] for i in range(len(self.values))])
        else:
            return f"Вектор нельзя сложить с {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[value * other for value in self.values])
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Умножение векторов разной длины недопустимо"
            return Vector(*[self.values[i] * other.values[i] for i in range(len(self.values))])
        else:
            return f"Вектор нельзя умножать с {other}"


# Пример использования:
v1 = Vector(3, 1, 4, 2)
print(v1)  # Вектор(1, 2, 3, 4)

v2 = Vector(5, 6, 7, 8)
print(v2)  # Вектор(5, 6, 7, 8)

v3 = Vector()
print(v3)  # Пустой вектор

v4 = v1 + v2
print(v4)  # Вектор(6, 8, 10, 12)

v5 = v1 + 3
print(v5)  # Вектор(4, 5, 6, 7)

v6 = v1 + "abc"  # Вектор нельзя сложить с abc
print(v6)

v7 = v1 * v2
print(v7)  # Вектор(5, 12, 21, 32)

v8 = v1 * 2
print(v8)  # Вектор(2, 4, 6, 8)

v9 = v1 * "abc"  # Вектор нельзя умножать с abc
print(v9)