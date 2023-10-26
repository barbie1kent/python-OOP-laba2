class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    def getSquare(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return self.__width * 2 + self.__height * 2

rectangle = Rectangle(10, 10)
print(rectangle.getPerimeter())

