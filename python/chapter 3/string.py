name='Anuj'
# name="Anuj"
# name='''Anuj'''

# string slicing
nameshort = name[0:3]   # start from 0 to 3 excluding 3
print(nameshort)
print(name[-3:-1])  #negative slicing start from the end with -1 till the first with -5 excluding -5
print(name[1:3]) #we can just use positive of negative slicing if it doesnt start or end from edge
print(name[:3])  # is same as [1:3]
print(name[1:])  # is same as [1:5]
print(name[0: 5: 2]) # is same as [0:5] then it will jump by 1