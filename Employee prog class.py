class employee():
    name=""
    desig=""
    salary=0
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
    def display(self):
        print("name: ",self.name ,"designation: ",self.desig ,"Salary: ",self.salary)
    def calculate(self):
        if (self.salary<10000):
            self.salary=self.salary+(self.salary*0.05)
        elif ((self.salary>=10000) and (self.salary<=25000)):
            self.salary=self.salary+(self.salary*0.1)
        elif ((self.salary>=25001) and (self.salary<=40000)):
            self.salary=self.salary+(self.salary*0.15)
        else :
            self.salary=self.salary+(self.salary*0.2)
n=input("name: ")
d=input("designation: ")
s=int(input("salary: "))
a=employee(n,d,s)
a.display()
a.calculate()
a.display()
