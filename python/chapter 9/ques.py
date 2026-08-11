# 1. Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
with open("poem.txt") as f:
    content = f.read().lower()
    if "twinkle" in content:
        print("The word 'twinkle' is present in file")
    else:
        print("The word 'twinkle' is not present in file")

# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game():
    print("You are playing the game")
    score = random.randint(1,62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score {score}")
    if(score > hiscore):
        # fetch the hiscore and update accordingly
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()



# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year old.
import os

os.makedirs("13_year_old", exist_ok=True)

for n in range(2,21):
    with open(f"13_year_old/table_{n}.txt","w") as f:
        for i in range(1,11):
            f.write(f"{n} X {i} = {n*i}\n")

# 4. A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.
word = "donkey"
with open("donkey.txt","r") as f:
    content = f.read()
    contentNew = content.replace("donkey","######")
with open("donkey.txt","w") as f:
    f.write(contentNew)

# 5. Repeat program 4 for a list of such words to be censored.
words = ["donkey","bad","ganda"]
with open("donkey.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"#"*len(word))

with open("donkey.txt","w") as f:
    f.write(content)

# 6. Write a program to mine a log file and find out whether it contains 'python'.
with open("log.txt") as f:
    content = f.read()
    if "python" in content:
        print("yes, python is in log file")
    else:
        print("no, python is not log file")

# 7. Write a program to find out the line number where python is present from ques 6.
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"yes, python is in log file at line no {lineno}")
        break
    lineno +=1
else:
    print("no, python is not log file")

# 8. Write a program to make a copy of a text file "this. txt"
with open("this.txt") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)

# 9. Write a program to find out whether a file is identical & matches the content of another file.
with open("this.txt") as f:
    content1 = f.read()
with open("this_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes these file are identical")
else:
    print("No these file are not identical")

# 10. Write a program to wipe out the content of a file using python.
with open("this_copy.txt","w") as f:
    f.write("")

# 11. Write a python program to rename a file to "renamed_by_python.txt.
with open("this_copy.txt") as f:
    content = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(content)