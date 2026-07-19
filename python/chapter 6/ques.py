# # 1. Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
c = int(input("Enter the number 3 : "))
d = int(input("Enter the number 4 : "))
if(a>b and a>c and a>d):
    print("This is the greatest number from four : ",a)
elif(b>a and b>c and b>d):
    print("This is the greatest number from four : ",b)
elif(c>a and c>b and c>d):
    print("This is the greatest number from four : ",c) 
else:
    print("This is the greatest number from four : ",d)

# # 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. 
# # Assume 3 subjects and take marks as an input from the user.
m1 = int(input("Enter you marks 1 here : "))
m2 = int(input("Enter you marks 2 here : "))
m3 = int(input("Enter you marks 3 here : "))
marks = m1+m2+m3
if(marks>=120 and m1 >= 33 and m2 >= 33 and m3 >= 33):
    print("Passed ")
else:
    print("Failed")

# # 3. A spam comment is defined as a text containing following keywords:

# # "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

comment = input("Enter the comment : ")
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
if( p1 in comment ):
    print("Spam")
elif(p2 in comment):
    print("Spam")
elif(p3 in comment):
    print("Spam")
elif(p4 in comment):
    print("Spam")
else:
    print("Not spam")

# # 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username : ")
if(len(username)<10):
    print("This username contains less than 10 character")
else:
    print("This username contains more than 10 character")
    
# 5. Write a program which finds out whether a given name is present in a list or not.
l = ["Hardeep","Singh","Panwar"]
name = input("Enter your name")
if(name in l):
    print("Name is present in list")

# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 - 100 =>Ex
# 80 - 90 =>A
# 70 -80 Rightarrow B
# 60 - 70 =>C
# 50 -60 Rightarrow D
# < 50 Rightarrow>F
grade = int(input("Enter your marks : "))

if(grade<=100 and grade >=90):
    print("Ex")
elif(grade<90 and grade >= 80):
    print("A")
elif(grade<80 and grade >= 70):
    print("B")
elif(grade<70 and grade >= 60):
    print("C")
elif(grade<60 and grade >= 50):
    print("D")
else:
    print("F")

# # 7. Write a program to find out whether a given post is talking about "Harry" or not.
talking = input("Enter the post : ")
h = "Harry"
if(h in talking):
    print("The given post is talking about Harry")
else:
    print("The given post is not talking about Harry")
