class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    
    def area(self):
        return self.__height *self.__width
    
    def __str__(self):
        return '[{}] {}/{}'.format(Rectangle.__name__, self.__width, self.__height)
    

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size",size)
        self.__size = size
    
    def __str__(self):
        return "[{}] {}/{}".format(Square.__name__, self.__size, self.__size)


s = Square(13)

print(s)
print(s.area())