class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        string=""
        if self.width>50 or self.height>50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                string+=("*")
            string+="\n"
        return string
    def get_amount_inside(self,shape):
        return (self.get_area())//shape.get_area()
    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_side(self,value):
        self.width=value
        self.height=value
    def set_width(self,width):
        self.width=width
        self.height=width
    def set_height(self,height):
        self.height=height
        self.width=height
    def __str__(self):
        return f"{self.__class__.__name__}(side={self.width})"
