# file read
f = open("file1.txt")
data = f.read()
print(data)
f.close()

# file create and write

st = "If i become a good person will i be able to become free"
f = open("myfile.txt","w")
f.write(st)
f.close()

# read line by line of file

f = open("file2.txt")

line1 = f.readline()
print(line1,type(line1))

line2 = f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))

line4 = f.readline()
print(line4,type(line4))

line5 = f.readline()
print(line5,type(line5))

# the same can be done with a loop
f = open("file3.txt") 
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()

# see here
f = open("file4.txt")
print(f.read())
f.close()

# The same can be wriiten by with statement
with open("file4.txt") as f:
    print(f.read())
# you dont have to explicitly close the file