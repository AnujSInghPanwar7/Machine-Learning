# List
friends = ["Apple" , "Orange" , 5 , 34.567 , "Anuj" , "Anuj(inner self)"]
print(friends[0])

friends[0] = "Banana" # Unlike string list are mutable
print(friends[0])

print(friends[0:4])

friends.append("Love")
print(friends)

l1 = [1,5,3,9,5,38,6]
print(l1)

l1.sort() # ye list ko sort krdega
print(l1)

l1.reverse() # ye list ko reverse krega na ki sort
print(l1)

l1.insert(3,14) # we insert 14 such that its index is 3 in list
print(l1)

print(l1.pop(3))
print(l1)

#Tuple
z = (1)
print(type(z))

y = (1,)
print(type(y))

a = ("Apple" , "Orange" , 5 , 34.567 , "Anuj" ,5, "Anuj(inner self)")

no = a.count(5)
print(no)

i = a.index(34.567)
print(i)

print(len(a))