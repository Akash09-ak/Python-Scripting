import keyboard
import time
time.sleep(2)             # to give some time for interpreter to execute
for i in range(10):        # here we are using loop for how many time we need to run our script
    keyboard.write("hy \n")      # write() function take the text as input 
    keyboard.press_and_release("enter") # here press_and_release() function used to enter hotkeys(like enter , shift+@, etc)
