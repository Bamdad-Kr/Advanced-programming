from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,car):
        self.car=car

    @abstractmethod
    def prise(self):
        pass

class Benz(Car):
    def prise(self):
        print(f"{self.car} is an expensive car.")
class Samand(Car):
    def prise(self):
        print(f"{self.car} is a cheep car.")

f1=Benz("Benz")
f1.prise()
f2=Samand("Samand")
f2.prise()
