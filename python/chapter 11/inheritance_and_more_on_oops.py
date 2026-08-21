#   multiple level inhertence 
class employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.company}")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language {self.language}")

class programmer(employee,coder): #multiple level inhertence 
    company = "ITC INFOTECH"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = employee()
b = programmer()

print(a.company,b.company)
b.show()
b.showLanguage()
b.printLanguage()

# Multi level inheretence
class emp:
    def __init__(self):
        print("Constructor of emp")
    a = 1
class code(emp):
    def __init__(self):
        print("Constructor of code")
    b = 2
class prog(code):
    def __init__(self):
        super().__init__()                  # Super key used to call parent class constructor 
        print("Constructor of prog")
    c = 3

o = emp()
print(o.a)
o = code()
print(o.a,o.b)
o = prog()
print(o.a,o.b,o.c)

#CLass Method , property , name setter
class meth:
    a = 1
    @classmethod
    def sho(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}{self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


m = meth()
m.a = 45

m.name = "Anuj Panwar"
print(m.fname,m.lname)
m.sho()

# Operator Overload
class number:
    def __init__(self,n):
        self.n = n
    def __add__(self, num):
        return self.n + num.n

n = number(1)
m = number(2)

print(n+m)
