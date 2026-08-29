# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank you")

l = [1,2,3,4,5,6,7,8,9]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)

#Write a list to comprehension to print a list which contains the multiplication table of  a user entered number.
n = int(input("Enter the number: "))

table = [n*i for i in range(1,11)]
print(table)

#Write a program to display a/b where a  and b are integers. If b = 0, display infinite by handling the 'ZeroDivisionError'.
try:
    a = int(input("Enter the number a: "))
    b = int(input("Enter the number b: "))
    print(a/b)
except ZeroDivisionError as z:
    print("infinite")

#Store the multiplication tables generated in problem 3 in a file named Tables.txt.
m = int(input("Enter the number: "))

table = [m*j for j in range(1,11)]
with open("tables.txt","a") as f:
    f.write(f"Table of {m}: {str(table)} \n")