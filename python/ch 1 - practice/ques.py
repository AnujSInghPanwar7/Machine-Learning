# Write a code to print twinkle twinkle little star poem
print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')

#Run a external module
import pyttsx3
engine = pyttsx3.init()
engine.say("T will speak this text")
engine.runAndWait()

#Print the content of the directory using the os model.
import os
#specify the directory you want to list
directory_path ='/Users'
#List all the files and directory in the specifiesd path
contents = os.listdir(directory_path)
#Print each file and directory name
for item in contents :
 print(item)