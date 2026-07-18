# Dictionaary
d = {} #Empty dictionary
marks = {
    "Anuj" : 99,
    "Singh" : 90,
    "Panwar" : 91,
}

print(marks,type(marks))
print(marks["Anuj"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Anuj":100,"Uk" : 12})
print(marks)
print(marks.get("Anuj"))
print(marks.get("Anu")) #Prints none
# print(marks["Anu"])     #Prints an error

# Sets
e = set() #Don't use s = {} as it will create an empty dictionary
s = {1,2,3,"Anuj",5,1,1,1,2,3,4}
print(s)

s.add(578)
print(s)
s.remove(1)
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6}

print(s1.union(s2))
print(s1.intersection(s2))