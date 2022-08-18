from microbit import *
import music
import random

while True:
    # display.scroll("Hello, World!")
    is_geme_str=False



    while not button_a.is_pressed() : 
        pass

    sleepjikan=random.randrange(1, 5)
    sleep(sleepjikan*1000)
    is_geme_str=True
    music.pitch(400,10)
    while is_geme_str:
        if pin0.is_touched():
            display.show(Image.ARROW_W)
            sleep(3000)
            break
        elif pin2.is_touched():
            display.show(Image.ARROW_E)
            sleep(3000)
            break
    display.clear()