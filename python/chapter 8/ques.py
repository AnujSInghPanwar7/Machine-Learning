# 1. Write a program using functions to find greatest of three numbers.
def greatOfThree(a,b,c):
    if(a>b and a>c):
        return(a)
    elif(b>a and b>c):
        return( b)
    else:
        return( c)
n = greatOfThree(55,66,22)
print(f"greatest of three numbers : {n}")
print(end = "")

# 2. Write a python program using function to convert Celsius to Fahrenheit.
# c/5 = (f-32)/9
def celToFahr(c):
    f=((9*c)+32)/5 
    return f
C = int(input("Enter temperature in C: "))
c = celToFahr(C)

print(f"{round(c,2)}degree celsious")
print(end = "")

# 3. How do you prevent a python print() function to print a new line at the end.
print(end = "")
# 4. Write a recursive function to calculate the sum of first n natural numbers.
def sumOfNat(n):
    if(n==0):
        return 0
    return n + sumOfNat(n-1)

n = int(input("Enter the natural number: "))
print(f"the sum of first n natural numbers is: {sumOfNat(n)}")
print(end = "")

# 5. Write a python function to print first n lines of the following pattern:
# ***
# **
# *
# - for n = 3
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

n = int(input("Enter the n: "))
print(f"this is the pattern {pattern(n)}")
print(end = "")

# 6. Write a python function which converts inches to cms.
def inchToCms(inch):
    return inch*2.54

inch = int(input("Enter the inch: "))
print(f"The inch when converted to cms is: {inchToCms(inch)}")
print(end = "")

# 7. Write a python function to remove a given word from a list ad strip it at the same time.
def rem(l,word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["Harry","Anuj","Panwar","an"]
print(rem(l,"an"))
print(end = "")

# 8. Write a python function to print multiplication table of a given number.
def multiplication(n):
    for i in range(1,11):
        print(n*i)
n = int(input("Enter the n: "))
multiplication(n)