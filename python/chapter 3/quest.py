# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name : ")
print(f"Good Afternoon {name}")
# 2. Write a program to fill in a letter template given below with name and date.

# letter =

# Dear </Name>,

# You are selected!

# <|Date|>

letter = '''Dear </Name>,
You are selected!
<|Date|>'''

print(letter.replace("</Name>","Anuj").replace("<|Date|>","10 october 2029"))

# 3. Write a program to detect double space in a string.
a="Hello Everyone  nya"
print(a.find("  "))

# 4. Replace the double space from problem 3 with single spaces.
print(a.replace("  "," "))
# 5. Write a program to format the following letter using escape sequence characters.

Letter = "Dear Harry,\n\t this python course is nice.\n Thanks!"
print(Letter)