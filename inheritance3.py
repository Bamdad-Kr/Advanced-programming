class Store:
  def __init__(self,store):
    self.s=store

class Hyper(Store):
  def __init__(self,store,produt):
    super().__init__(store)
    self.p=produt

class HomeAppliances(Store):
    def __init__(self,store,appliances):
     super().__init__(store)
     self.a=appliances

class Meson(Store):
  def __init__(self,store,clothes):
    super().__init__(store)
    self.c=clothes

obj1=Store("bigstore")
obj3=HomeAppliances("bigstore","appliances")
obj4=Meson("bigstore","clothes")
print(obj4.c)
