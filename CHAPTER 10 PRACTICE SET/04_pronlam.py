class Vector:
    def __init__(self, values):
        self.values = values

    # Overloading + operator
    def __add__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(result)

    # Overloading * operator (Dot Product)
    def __mul__(self, other):
        dot_product = 0
        for i in range(len(self.values)):
            dot_product += self.values[i] * other.values[i]
        return dot_product

    # To print vector nicely
    def __str__(self):
        return str(self.values)


# Creating vectors
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Vector Addition
sum_vector = v1 + v2
print("Vector Addition:", sum_vector)

# Dot Product
dot = v1 * v2
print("Dot Product:", dot)