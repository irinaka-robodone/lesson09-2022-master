from microbit import *
import music
import random

while True:
    start = False
    time = random.randrange(5,15)

    display.clear()
    while not button_a.was_pressed():
        pass
    start = True
    sleep(time*1000)
    
    music.pitch(400, 1)
    while start:
        if pin0.is_touched():
            display.show(Image.ARROW_W)
            sleep(3000)
            break
        elif pin2.is_touched():
            display.show(Image.ARROW_E)
            sleep(3000)
            break