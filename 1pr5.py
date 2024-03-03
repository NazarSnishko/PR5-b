class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    @staticmethod
    def input_matrix():
        rows = int(input("Введіть кількість рядків: "))
        cols = int(input("Введіть кількість стовпців: "))
        matrix = []
        print("Введіть елементи матриці:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = float(input(f"Елемент [{i + 1}][{j + 1}]: "))
                row.append(element)
            matrix.append(row)
        return Matrix(matrix)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розміри матриць повинні бути однакові для додавання")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розміри матриць повинні бути однакові для віднімання")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Кількість стовпців у першій матриці повинна бути рівною кількості рядків у другій матриці")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        
        return Matrix(result)

    def __truediv__(self, other):
        if other.rows != other.cols != 1:
            raise ValueError("Ділення підтримується тільки на скалярні значення")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] / other.matrix[0][0])
            result.append(row)
        
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


# Введення першої матриці
print("Введення першої матриці:")
matrix1 = Matrix.input_matrix()

# Введення другої матриці
print("\nВведення другої матриці:")
matrix2 = Matrix.input_matrix()

print("\nМатриця 1:")
print(matrix1)

print("\nМатриця 2:")
print(matrix2)

# Додавання
print("\nДодавання:")
try:
    print(matrix1 + matrix2)
except ValueError as e:
    print(e)

# Віднімання
print("\nВіднімання:")
try:
    print(matrix1 - matrix2)
except ValueError as e:
    print(e)

# Множення
print("\nМноження:")
try:
    print(matrix1 * matrix2)
except ValueError as e:
    print(e)

# Ділення
print("\nДілення:")
scalar = Matrix([[float(input("Введіть скалярне значення для ділення: "))]])
try:
    print(matrix1 / scalar)
except ValueError as e:
    print(e)

