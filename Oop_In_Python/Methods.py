#inheritance or child classes
#working on different class:
class employee:
    pay_rate=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def emp_salary(self):
        self.pay=employee.pay_rate*self.pay
        return self.pay
    @classmethod
    def salary_incri(cls,new_rate):
        cls.pay_rate=new_rate
    @classmethod
    def self_const(cls,string):
        first,last,pay=string.split(',')
        return cls(first,last,pay)
        

emp_1=employee("mohammed","rizwan",45000)
emp_2=employee("riyaz","ali",35000)
emp_3=employee("iam","bot",50000)
employee.salary_incri(1.5)
emp_1.emp_salary()
print(employee.pay_rate)
#print(emp_1.pay)
#inheritance
class developer(employee):
    pay_rate=1.07
    def __init__(self,first,last,pay,prog_lan):
        super().__init__(first,last,pay)
        self.prog_lan=prog_lan
    def salary_pay(self,sal):
       pass
    #work in progress on inheritance
dev=developer("shaik","aftab",20000,"python")

print(dev.first,dev.last) #even the developer class is empty 
#still it can aqurie the parent chars
