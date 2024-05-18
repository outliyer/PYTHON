

#using the property method for read only data_type
class family:
    all=[]
    def __init__(self,name,age,profession,income):
     self.name=name
     self.age=age
     self.profession=profession
     self.income=income
     family.all.append(self )
    def __repr__(self):
        return f"'{self.name}','{self.age}','{self.income}',"
    @property
    def read_only(self,name):
        self.name= name
        return self.__name

member1=family("mom",48,"house_wife","null")
member2=family("dad",54,"employee","40k")
member3=family("brother",24,"bank-manager","30k")
member4=family("my_self",19,"student","null")
'''for insta in family.all:
     print(insta.age)'''
print(family.all)
family.read_only

print(member1.name)
##############.....work_in_progress.......##################