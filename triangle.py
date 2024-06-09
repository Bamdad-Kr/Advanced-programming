class Triangle ():
  def __init__(self,a,b,c):
    self.z1=a
    self.z2=b
    self.z3=c
    if a < b+c and b < a+c and c<a+b:
      print("trangle is True")
    else:
      print("traingle false")

  def perim(self):
    return self.z1+self.z2+self.z3

  def Area(self):
    s=(self.z1+self.z2+self.z3)/2
    return(s*(s-self.z1)*(s-self.z2)*(s-self.z3))**0.5

  def is_triangle(self):
    if (self.z1+self.z2)>self.z3 and (self.z1+self.z3)>self.z2 and (self.z2+self.z3)>self.z1:
      return True
    else:
      return False

  def __del__(self):
    print("Triangle deleted")
    return -1


t=Triangle(5,7,6)
print(t.perim())
print(t.Area())
print(t.is_triangle())
print(t.z1)
del t
