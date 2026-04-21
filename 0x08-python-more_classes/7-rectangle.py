#!/usr/bin/python3
"""Module define a Rectangle classe that define a rectangle"""


class Rectangle:
    """Define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    """intializer for the new object created"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """Geter for the private instance attribute width"""
    @property
    def width(self):
        return self.__width

    """Seter for the private instance attribute width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Geter for the private instance attribute height"""
    @property
    def height(self):
        return self.__height

    """Setter for the private instance attribute height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Return the rectangle area"""
    def area(self):
        return self.__width * self.__height

    """Return the rectangle perimeter"""
    def perimeter(self):
        if self.__height and self.__width:
            return self.__width * 2 + self.__height * 2
        else:
            return 0
    """Return a pritable object of rectangle"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.width
            if i < self.__height - 1:
                result += "\n"
        return result

    """Return a printable user freindly format"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """Print a message when a instance of Rectangle is deleted"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
