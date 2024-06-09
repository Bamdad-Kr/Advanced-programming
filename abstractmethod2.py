from abc import ABC, abstractmethod
class Flower(ABC):
    def __init__(self,flower):
        self.flower=flower

    @abstractmethod
    def color(self):
        pass

class Rose(Flower):
    def color(self):
        print(f"{self.flower} is red.")
class Yas(Flower):
    def color(self):
        print(f"{self.flower} is white.")

f1=Rose("Rose")
f1.color()
f2=Yas("Yas")
f2.color()                
