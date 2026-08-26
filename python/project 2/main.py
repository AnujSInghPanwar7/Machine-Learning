import random
n = random.randint(1,100)
a = -1
guesess = 0
while(a != n):
    guesess +=1
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")
print(f"You guessed the correct number in {guesess} attempt")