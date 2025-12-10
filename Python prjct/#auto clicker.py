import mouse
import keyboard as key



if key.is_pressed("F6"):
    while True:
        mouse.click("Left")

        if key.is_pressed("F6"):
            break





