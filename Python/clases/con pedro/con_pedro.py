class TriangleRectangle:
    def __init__(self, base, height):
        self.base = base
        self.__height = height
        self.area = None
        self.perimeter = None
        self.hipotenusa = None

    def calcArea(self):
        self.area = (self.base * self.__height) / 2
        print("El area de un triangulo de base", end=" ")
        print(f"{self.base}cm y altura {self.__height}cm es igual a {self.area}cm2")

    def calcPerimeter(self):
        self.hipotenusa = (((self.base)**2) + ((self.__height)**2))**0.5
        self.perimeter = self.base + self.__height + self.hipotenusa
        print("El perimetro de un triangulo de", end=" ")
        print(f"base {self.base}cm y altura {self.__height}cm es igual a {self.perimeter:.2f}cm")


triangulin = TriangleRectangle(5, 10)
triangulin.calcArea()
triangulin.calcPerimeter()

