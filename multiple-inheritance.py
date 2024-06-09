class Flay:
  def flay(self):
    print("bird is flaying")
class Hunt:
  def hunt(self):
    print("bird need to hunt")
class Land:
  def land(self):
    print("bird  is landing")
class Bird(Flay,Hunt,Land):
  pass

b = Bird()
print(b.flay())
print(b.hunt())
print(b.land())
