# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class progerammer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = progerammer("Anuj",30000, 110085)
print(p.name, p.salary, p.pin)
r = progerammer("Rohan",300080, 110065)
print(r.name, r.salary, r.pin)

# 2. Write a class "calculator" capable of finding square, cube and square root of a number.

class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square of n is {self.n*self.n}")

    def cube(self):
        print(f"The cube of n is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of n is {self.n**1/2}")

num = calculator(4)
num.square()
num.cube()
num.squareroot()

# 3. Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. Does this change the class attribute?

class demo:
    a = 4
o = demo()
print(o.a)
o.a = 0
print(o.a)
print(demo.a)

# 4. Add a static method in problem 2, to greet the user with hello.

class calc:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square of n is {self.n*self.n}")

    def cube(self):
        print(f"The cube of n is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of n is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there!!")

num = calc(4)
num.hello()
num.square()
num.cube()
num.squareroot()

# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class train:
    def __init__(self,trainNo,fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to
    def book(self,fro, to):
        print(f"The train no is {self.trainNo} from {self.fro} to {self.to}")

    def getStatus(self):
        print(f"The train no {self.trainNo} is on time ")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no {self.trainNo} from {self.fro} to {self.to} is {randint(222,5555)}")

t = train(123456,"Dehradun","Delhi")
t.book("Dehradun","Delhi")
t.getStatus()
t.getFare("Dehradun","Delhi")

# 6. Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects.

class trai:
    def __init__(slf,trainNo,fro, to):
        slf.trainNo = trainNo
        slf.fro = fro
        slf.to = to
    def book(self,fro, to):
        print(f"The train no is {self.trainNo} from {self.fro} to {self.to}")

    def getStatus(self):
        print(f"The train no {self.trainNo} is on time ")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no {self.trainNo} from {self.fro} to {self.to} is {randint(222,5555)}")

t = train(123456,"Dehradun","Delhi")
t.book("Dehradun","Delhi")
t.getStatus()
t.getFare("Dehradun","Delhi")
