import random
n = random.randint(1,100)
a = -1
guesess = 0
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesess +=1 
    elif(a<n):
        print("Higher number please")
        guesess +=1 

print(f"You guessed the correct number in {guesess} attempt")