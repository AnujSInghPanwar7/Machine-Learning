a = int(input("Enter you age : "))

# IF ELIF ELSE LADDER

if(a>=18):
    print("You are above the age of consent")
elif(a==0):
    print("Enter valid age")
elif(a<0):
    print("Your age cant be in negative")
else:
    print("Your are below the age of consent")