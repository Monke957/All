import os
import random
import keyboard
import time
from tkinter import *
import ctypes


ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )




def Submit():
    answer2 = answer.get()
    if answer2 == '12345':
        print('CORRECT')
        os.system(command=r'attrib -s -h "C:\Users\11EDM001\Microsoft Teams chattfiler\Skrivbordet\Python prjct"')
        os.system(command=r'attrib -s -h "C:\Users\11EDM001\Microsoft Teams chattfiler\Skrivbordet\.BAT filer"')
        os.system(command=r'attrib -s -h "C:\Users\11EDM001\Microsoft Teams chattfiler\Skrivbordet\python-3.13.1-amd64.exe"')
        
    else:
        print('INCORRECT')
        os.system(command=r'attrib +s +h "C:\Users\11EDM001\Microsoft Teams chattfiler\Skrivbordet\Python prjct"')
        os.system(command=r'attrib +s +h"C:\Users\11EDM001\Microsoft Teams chattfiler\Skrivbordet\.BAT filer"')


os.system('cls' if os.name == 'nt' else 'clear')

window = Tk()
window.overrideredirect(True)


window.geometry('400x35')
window.config()
window.title('Passwrd')


answer = Entry()
answer.config(
    font=('Arial',20), 
    bg='black',
    fg='lightgreen',)
answer.place(x=0,y=0, width=300,height=35)

submit = Button(window,
                 text='submit',
                 font=('Arial',15,'bold'),
                 bg='red',
                 activebackground='red')
submit.config(command=Submit)
submit.place(height=35,width=100,x=300,y=0)


window.mainloop()


