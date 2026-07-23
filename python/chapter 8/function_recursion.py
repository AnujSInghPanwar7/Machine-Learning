# Funtion defination
def avg():
    a = int(input("Enter you number 1 : "))
    b = int(input("enter your number 2 : "))
    c = int(input("enter your number 3 : "))
    print((a+b+c)/3)
avg()
print()

# funtion with argument
def goodDay(name, ending):
    print("Good Day " + name)
    print(ending)

a = goodDay("Anuj","Thank you")
print(a)

print()

def badDay(name, ending):
    print("bad Day " + name)
    print(ending)
    return "Done"

b = badDay("Anuj","Welcome")
print(b)
print()

# Default parameters

def goodDay(name, ending="Thank you"):
    print(f"Good Day ",{name} )
    print(ending)

goodDay("Anuj")
goodDay("anuj", "Thanks")
print()

# Recursion
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter your number to get factorial : "))
print(f"The factorial is : {factorial(n)}")