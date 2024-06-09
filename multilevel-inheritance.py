class Food:
  def fun1(self):
    print("This food is famous.")

class Restaurant(Food):
  def fun2(self):
    print("This restaurant has best food.")

class Person(Restaurant):
  print("I enjoied this food and restaurant.")

p = Person()
print(p.fun2())
