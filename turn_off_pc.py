import mouse
import time

def shutdown():
    mouse.move(31,695)
    time.sleep(0.1)
    mouse.click('left')

    time.sleep(0.2)
    mouse.move(575,630)
    time.sleep(0.1)
    mouse.click('left')


    time.sleep(0.2)
    mouse.move(575,550)
    time.sleep(0.1)
    mouse.click('left')
    mouse.click('left')
    mouse.click('left')
    mouse.click('left')
    mouse.click('left')