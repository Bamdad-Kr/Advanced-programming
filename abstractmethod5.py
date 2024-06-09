from abc import ABC, abstractmethod
class Parents(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def color_eyes(self):
        pass

class child1(Parents):
    def color_eyes(self):
        print(f"{self.name} has  brown eyes...")
class child2(Parents):
    def color_eyes(self):
        print(f"{self.name} has  black eyes...")

h1=child1("Nazi")
h1.color_eyes()
h2=child2("Kati")
h2.color_eyes()
