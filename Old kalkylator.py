import os
import keyboard
import time

os.system('cls' if os.name == 'nt' else 'clear')

add_or_subtract = input('would you like to add or subtract?: ')

if add_or_subtract == 'add':
    first = input('Input first number: ')
    second = input('Input second number: ')
    sum = (float(first) + float(second))
    print(sum)
    
elif add_or_subtract == 'subtract' or add_or_subtract == 'sub' :
    first = input('Input first number: ')
    second = input('Input second number: ')
    sum = (float(first) - float(second))
    print(sum)

else:
    print('Error please answer with add or subtract')    