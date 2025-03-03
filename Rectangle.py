class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
rectangle = Rectangle(10, 5)
print("Area:", rectangle.area())  # Output: 50
print("Perimeter:", rectangle.perimeter())  # Output: 30
