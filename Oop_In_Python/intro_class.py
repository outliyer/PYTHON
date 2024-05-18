#classes and object basic
class person:
    name="delat"
    contact=630
    id:119
    def info (self):
     print(f"{self.name}contact info is {self.id}")
a=person()
a.name="alpha"
a.id= 1
b=person()
b.name="beta"
b.id=3
a.info()
b.info()

