class Color:
  def __init__(self,color1,color2):
    self.color1=color1
    self.color2=color2
class Artist(Color):
  def __init__(self,color1,color2,color3):
    super().__init__(color1,color2)
    self.color3=color3


c=Artist("blue","red","yellow")
print(c.color3)
