from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,home):
        self.home=home

    @abstractmethod
    def bedroom(self):
        pass

class home1(Car):
    def bedroom(self):
        print(f"{self.home} home has 2 bedroom.")
class home2(Car):
    def bedroom(self):
        print(f"{self.home} home has 3 bedroom..")

h1=home1("ali's")
h1.bedroom()
h2=home2("Hamid's")
h2.bedroom()
