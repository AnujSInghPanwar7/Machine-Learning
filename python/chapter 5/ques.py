# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
translation = {
    "Namaste":"Hello",
    "Aja":"Come",
    "Pyaar":"Love"
    }
print(translation)
word = input("Enter the hindi word : ")
print(translation[word])

# 2. Write a program to input eight numbers from the user and display all the unique numbers (onсе).
s = set()
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)
x = int(input("Enter all unique number : "))
s.add(x)

print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
p = {18,"18"}
print(p,type(p))

# 4. What will be the length of following set s:
y = set()
y.add(20)
y.add(20.0)
y.add('20') #length of s after these operations?

print(y,len(y))

# 5. s = {}
# What is the type of 's'?
# empty dictionary

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})
name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})
name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})
name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})
print(d)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
r = {
    "A":"c",
    "A":"f",
}
print(r)

# 8. If languages of two friends are same; what will happen to the program in problem 6?
t = {
    "A":"f",
    "B":"f"
}
print(t)

# 9. Can you change the values inside a list which is contained in set S?
# m = { 8, 7, 12, "Harry", [1,2]}