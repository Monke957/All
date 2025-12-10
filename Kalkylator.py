from tkinter import *

def number(num):
    current = answer.get()
    answer.delete(0, END)
    answer.insert(0, current + str(num))



def click1():
    button2.config(state='normal')
    global first_num
    global operation
    first_num = int(answer.get())
    operation = 'add'
    answer.delete(0, END)

def click2():
    button1.config(state='normal')
    global first_num
    global operation
    first_num = int(answer.get())
    operation = 'subtract'
    answer.delete(0, END)

def click3():
    button3.config(state='normal')
    global first_num
    global operation
    first_num = int(answer.get())
    operation = 'multiply'
    answer.delete(0, END)

def click4():
    button2.config(state='normal')
    global first_num
    global operation
    first_num = int(answer.get())
    operation = 'divide'
    answer.delete(0, END)

def equal():
    second_num = int(answer.get())
    if operation == 'add':
        result = first_num + second_num
        print(result)
    elif operation == 'subtract':
        result = first_num - second_num
        print(result)
    elif operation == 'multiply':
        result = first_num * second_num
        print(result)
    elif operation == 'divide':
        result = first_num / second_num
        print(result)
    answer.delete(0, END)
    answer.insert(0, str(result))

def delete():
    answer.delete(0, END)

window = Tk()
window.geometry('700x500')
window.title('Kalkylator')
#windowIcon = PhotoImage(file= "C:\\Users\\11EDM001\\Microsoft Teams chattfiler\\Skrivbordet\\Python prjct\\python bilder\\kalkylatorbild.png")
#window.iconphoto(True,windowIcon)
window.config(background='gray')

label = Label(window,
              text='Kalkylator',
              font=('Arial',50,'bold'),
              bg='gray',
              relief=SUNKEN,
              bd=10,
              padx=10,
              pady=10,
              #image=windowIcon,
              compound=TOP)
label.place(x=300,y=0)
#place(x=150,y=0)

answer = Entry()
answer.config(
    font=('Arial',40), 
    bg='black',
    fg='white',
    state=NORMAL)#DISABLED)
answer.place(x=0,y=0, width=296, height=150)


button1 = Button(window,
                 text='add',
                 font=('Arial',20,'bold'),
                 bg='lightblue')
button1.config(command=click1)
button1.place(x=380,y=150)




button2 = Button(window,
                 text='subtract',
                 font=('Arial',20,'bold'),
                 bg='lightblue')
button2.config(command=click2)
button2.place(x=522,y=150)

button3 = Button(window, 
                 text='sum',
                 font=('Arial',20,'bold'),
                 bg='lightgreen')
button3.config(command=equal)
button3.place(x=295,y=150)

button4 = Button(window,text='CC',bg='red',font=('Arial',20,'bold'))
button4.config(command=delete)
button4.place(x=456,y=150)

button5 = Button(window, 
                 text='Multiply', 
                 font=('Arial',20,'bold'),
                 bg='lightblue')
button5.place(x=165,y=150)
button5.config(command=click3)

button6 = Button(window, 
                 text='Divide', 
                 font=('Arial',20,'bold'),
                 bg='lightblue')
button6.place(x=55,y=150)
button6.config(command=click4)

buttons = [
    ('1', 390, 240), ('2', 440, 240), ('3', 490, 240),
    ('4', 390, 300), ('5', 440, 300), ('6', 490, 300),
    ('7', 390, 360), ('8', 440, 360), ('9', 490, 360),
    ('0', 440, 420)
]
for (text, x, y) in buttons:
    button = Button(window, text=text, font=('Arial',20,), command=lambda num=text: number(num))
    button.place(x=x, y=y)

first_num = None
operation = None

window.mainloop()