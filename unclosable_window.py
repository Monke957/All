import turtle as t
import tkinter as tk
import threading
import mouse
import time

colors = ['blue', 'green', 'red', 'pink', 'purple', 'black', 'lime', 'orange', 'yellow']
text = ["F", "U", "C", "K", " ", "Y", "O", "U"]  # The text to be displayed

# Manually set the width of each letter and the spacing between them
letter_width = 50  # Width of each letter (in pixels)
letter_spacing = 10  # Spacing between the letters (in pixels)


def turtle_draw(on_complete_callback):
    # Initialize the turtle screen
    screen = t.Screen()
    screen.bgcolor('black')
    screen.setup(width=screen.window_width(), height=screen.window_height())  # Fullscreen
    screen.screensize(screen.window_width(), screen.window_height())  # Fill the screen with drawing area

    # Hide the turtle icon
    t.hideturtle()
    t.speed(15)
    t.color('green')

    # Move the turtle to the center of the screen
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    t.penup()  # Lift the pen to avoid drawing during the movement
    t.goto(-screen_width // -2.2, screen_height // 11)  # Move to the center
    t.pendown()  # Start drawing

    b = 200
    while b > 0:
        t.left(b)
        t.forward(b * 3)
        b = b - 1

    # Notify the completion of turtle drawing
    on_complete_callback()

    t.bye()  # Finish the turtle graphics


def show_letter(char, index, start_x):
    # Create the label for each letter
    label = tk.Label(window, text=char, font=("Arial", 48), fg="white", bg="black")

    # Position the label with an offset based on the starting position
    x_position = start_x + index * (letter_width + letter_spacing)
    label.place(x=x_position, y=175)


def apper():
    # Get the screen width dynamically to support fullscreen mode
    screen_width = window.winfo_screenwidth()

    # Calculate the starting X position to center the text
    total_text_width = len(text) * (letter_width + letter_spacing) - letter_spacing  # subtract extra space
    start_x = (screen_width - total_text_width) // 2

    # Start displaying each letter with the proper offset
    delay = 1250  # 10 seconds total / 8 letters = 1.25s per letter
    for i, char in enumerate(text):
        window.after(i * delay, show_letter, char, i, start_x)


def click():
    print("Blocked close")


def mouse_click():
    while True:
        print("Mouse click triggered.")
        mouse.move(660, 400)  # Move the mouse to the specified location
        mouse.click('left')  # Perform left click
        time.sleep(0.1)  # A small delay between each move and click


def stuck():
    while True:
        mouse.move(660, 400)  # Move the mouse continuously without clicking
        time.sleep(0.05)  # A small delay between each move


def start_gui():
    global window
    window = tk.Tk()
    window.attributes("-fullscreen", True)  # Fullscreen mode
    window.geometry("800x400+100+400")
    window.overrideredirect(True)
    window.attributes("-topmost", True)
    window.protocol("WM_DELETE_WINDOW", click)

    # Start background threads
    threading.Thread(target=color_loop, daemon=True).start()

    window.after(1000, apper)
    window.mainloop()


def color_loop():
    while True:
        for color in colors:
            window.configure(bg=color)
            window.update()
            time.sleep(0.2)


def turtle_complete():
    # Start mouse click in a separate thread after the turtle drawing is complete
    threading.Thread(target=mouse_click, daemon=True).start()


# Start the stuck function to move the mouse continuously
threading.Thread(target=stuck, daemon=True).start()

# Start the turtle graphics in a separate thread and pass the callback to start mouse click
turtle_thread = threading.Thread(target=turtle_draw, args=(turtle_complete,))
turtle_thread.start()

# Wait for the turtle drawing to finish before starting the GUI
turtle_thread.join()  # Wait until the turtle drawing is complete

# Now, start the Tkinter GUI in the main thread
start_gui()
