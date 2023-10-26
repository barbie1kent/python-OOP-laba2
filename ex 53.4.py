import tkinter as tk
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius**2

    def calculate_circumference(self):
        return 2 * math.pi * self.__radius

    def draw(self, canvas):
        canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)

area = Circle.calculate_area()
print(area)
circumference = circle.calculate_circumference()
print(circumference)

root = tk.Tk()

canvas = tk.Canvas(root, width=350, height=350)
canvas.pack()
circle = Circle(180, 180, 100)
circle.draw(canvas)

root.mainloop()
