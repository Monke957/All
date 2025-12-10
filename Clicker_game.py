from tkinter import *
import time

amount = 0
amountearn = 1
rockclick_double = 10
magmaclick = 0
magmacost = 25


def add_lava():
    global amount
    amount += 1
    Lavamnt.config(text=amount)

    gamewin.after(1000, add_lava)

    

def lavagain():
    global amount, amountearn
    amount += amountearn
    Lavamnt.config(text=amount)

def rockclick():
    global amount, amountearn, rockclick_double
    if amount < rockclick_double:
        print('Not enough money')

    else:
        amount -= rockclick_double
        Lavamnt.config(text=amount)
        rockclick_double += 23
        amountearn += 1
        rocks.config(text=f'1+ Per click Cost: {rockclick_double} lava')

def magmabut():
    global amount,amountearn,magmacost
    if amount < magmacost:
        print('Not enough money')
    else:
        amount -= magmacost
        magmacost += 25
        Lavamnt.config(text=amount)
        magma.config(text=f'1+ every sec cost: {magmacost} lava')
        add_lava()



    

gamewin = Tk()
gamewin.geometry('1200x600+35+20')
gamewin.title('LAVA CLICKER')
gamewin.config(bg='orange')

Clicker = Button(gamewin)
Clicker.config(height='2',width='8',text='LAVA',font=('Arial',20,'bold'), command=lavagain)
Clicker.place(x=0,y=230)

rocks = Button(gamewin)
rocks.config(text=f'1+ Per click. Cost: {rockclick_double} lava',font=('Arial',15,'bold'),command=rockclick)
rocks.place(x=225,y=0)

magma = Button(gamewin)
magma.config(text=f'1+ Every sec cost: {magmacost} lava',font=('Arial',15,'bold'),command=magmabut)
magma.place(x=225,y=50)

Lavamnt = Label(gamewin)
Lavamnt.config(height='2',width='8',text=amount,font=('Arial',30,'bold'))
Lavamnt.place(x=0,y=130)


gamewin.mainloop()