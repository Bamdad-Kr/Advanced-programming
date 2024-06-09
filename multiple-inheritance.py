class Fly:
  def fly(self):
    print("bird is flying")
class Hunt:
  def hunt(self):
    print("bird need to hunt")
class Land:
  def land(self):
    print("bird is landing")
class Bird(Fly, Hunt, Land):
  pass

b = Bird()
print(b.fly())
print(b.hunt())
print(b.land())
