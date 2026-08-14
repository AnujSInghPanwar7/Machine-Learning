class employee:
    language = "py"   # This is class atttribute
    salary = 1200000

    def __init__(self):
        print("I am crearting an object")   # dunder method which is called automatically
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

Anuj = employee()
Anuj.name = "Anuj"
print(Anuj.name, Anuj.language, Anuj.salary)
print()
Rohan = employee()
Rohan.name = "Rohan"   # This is an object atttribute
print(Rohan.name, Rohan.language, Rohan.salary)
print()

# Here name is object attribute and language and salary are class attribute as they directly belong to class

Rohan = employee()
Rohan.language = "C++"   # This is an instance attribute and it take prefernce over class attribute
print(Rohan.language, Rohan.salary)  
print()

Eren = employee()
Eren.language = "Java"
Eren.getInfo()
Eren.greet()
print()

class employeee:
    language = "py"   # This is class atttribute
    salary = 1200000

    def __init__(self, name, language, salary):
        print("I am crearting an object")   # dunder method which is called automatically
        self.name = name
        self.language = language
        self.salary = salary
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

panwar = employeee("Panwar","Javascript",190000)
print(panwar.name, panwar.language, panwar.salary)
print()
