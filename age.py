class person:

    def __init__(self,age):
        self.age = age


    def _set_age(self,age):
        
        if age < 0:
            raise ValueError(f"Invalid age {age!r}")
        else:
            self._age = age


    def _get_age(self):
        return self._age

    age = property(_get_age,_set_age) 

A=int(input("Enter your age: "))
p=person(20)
p.age=A
print(p.age)
