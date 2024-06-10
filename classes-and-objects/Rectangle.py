class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def claclArea(self):
        area = self.length * self.width
        print(f'{"Area of the rectangle is "}{area}')
    
    def calcPerimeter(self):
        peri = 2*(self.length + self.width)
        print(f'{'Perimeter of a triangle is '}{peri}')

