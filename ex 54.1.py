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

rectangle = Rectangle(1, 1)
print(rectangle.width)
print(rectangle.height)

rectangle.width = 1
rectangle.height = 1
print(rectangle.width)
print(rectangle.height)