class Rectangle:
  def __init__(self, width, height):
    self.height=height
    self.width=width

  def set_width(self,width):
    self.width=width

  def set_height(self,height):
    self.height=height
  
  def get_area(self):
    return self.height*self.width

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if(self.height>50 or self.width>50):
      return  "Too big for picture."
    pic=""
    for h in range(self.height):
      for w in range(self.width):
        pic=pic+"*"
      pic=pic+"\n"
    return pic

  def get_amount_inside(self,shape):
    return int(self.get_area()/shape.get_area())

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side):
    self.height=side
    self.width=side
    self.side=side

  def set_width(self,side):
    self.height=side
    self.width=side
    self.side=side

  def set_height(self,side):
    self.height=side
    self.width=side
    self.side=side
    
  def set_side(self,side):
    self.height=side
    self.width=side
    self.side=side

  def __str__(self):
    return f"Square(side={self.side})"
