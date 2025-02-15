# Install an external module and use it to perform an operation of your interest
# commit 1 to run number 2 and vice versa these both are different modules 

# 1
 import pyttsx3
 engine = pyttsx3.init()
 engine.say("Run Run ")
 engine.runAndWait()

# 2

 from emoji import emojize 
 print(emojize(":thumbs_up:")) 
