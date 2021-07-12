class person():
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.sex=s
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Sex: ',self.sex)
class publication():
    def __init__(self,NRP,NB,NA):
        self.NRP=NRP
        self.NB=NB
        self.NA=NA
    def display(self):
        print('Number of Research papers Published: ',self.NRP)
        print('Number of Books Published: ',self.NB)
        print('Number of Articles Published: ',self.NA)
class faculty(person,publication):
    def __init__(self,n,a,s,des,dep,NRP,NB,NA):
        person.__init__(self,n,a,s)
        self.des=des
        self.dep=dep
        publication.__init__(self,NRP,NB,NA)
    def displaydata(self):
        person.display(self)
        print('DESIGNATION: ',self.des)
        print('DEPARTMENT: ',self.dep)
        publication.display(self)
n=input('Name: ')
a=int(input('Age: '))
s=input('Sex: ')
NRP=int(input('Number of research paper: '))
NB=int(input('Number of books: '))
NA=int(input('Number of articles: '))
des=input('Designation: ')
dep=input('Department: ')
f=faculty(n,a,s,des,dep,NRP,NB,NA)
f.displaydata()
