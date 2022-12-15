class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, width):
    self.width = width;

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2*self.width + 2*self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    retStr = "";
    for i in range(0,self.height):
      retStr += "*"*self.width + "\n"
    return retStr

  def get_amount_inside(self, box):
    print( f"  I am {self.width} x {self.height}")
    print( f"box is {box.width} x {box.height}")
    amount = min(self.width//box.width, self.height//box.height)
    print( f"amount is {amount}")
    return amount



class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side,side)

  def __str__(self):
    return f"Square(side={self.width})"
  
  def set_side(self,side):
    self.set_width(side)
    self.set_height(side)
