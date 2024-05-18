#program to print all the instants in the class
class ROOM:
    all=[]
    # magic method for EASY code all the instants in the class
    def __init__(self,name,age,work):
     self.name=name
     self.age=age
     self.work=work
     ROOM.all.append(self)
     #to get proper representation we use magicmethod2
    def __repr__ (self):#it blindily returns the string
        return f"ROOM({self.name},{self.age},{self.work})"
#we get all the innstants in the list from the above function
person1=ROOM("irfan",19,"heavy_driver")
person2=ROOM("aftab",22,"driver")
person3=ROOM("jassem",20,"rapido")
#method one to print the one of the atributes of instance
for instance in ROOM.all:
    print(instance.name)
    #method2 for getting the instants in list
print(ROOM.all)
