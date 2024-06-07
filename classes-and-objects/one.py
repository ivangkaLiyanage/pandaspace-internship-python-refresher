# Create a class `Rectangle` with attributes `length` and `width`. Include methods to calculate the area and perimeter.
# create a class
# create attributes

class Rectangle:
    length = 12
    width = 6

    def calc(obj):
        area = obj.length * obj.width
        print(area)

Rectangle.calc = classmethod(Rectangle.calc)
Rectangle.calc()
