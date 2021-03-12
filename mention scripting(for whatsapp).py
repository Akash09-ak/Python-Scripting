import keyboard
import time
time.sleep(2)

for i in range(10): #number of members count
    keyboard.press_and_release('shift+@')           # here in this function we are using shift +@ for mentioning

    for j in range(i):
        keyboard.press_and_release('down')          # after getting @ getting hotkey 'down'
    keyboard.press_and_release('enter')             # this function provide enter key
    time.sleep(1)                                   # for taking 1 sec hault 
