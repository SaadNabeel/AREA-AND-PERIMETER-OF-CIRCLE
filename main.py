import math  

class Circle:
    def __init__(self, radius):
        
        self.radius = radius

    def area(self):
        
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    
    print("The area of the circle with radius", radius, "is:", circle.area())
    print("The perimeter of the circle with radius", radius, "is:", circle.perimeter())
