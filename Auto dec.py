import random
import os
import time

rand = random.randint(1,4)

os.system('cls' if os.name == 'nt' else 'clear')

def First():
    global choice2
    global choice3
    choice2 = input('What is your first choice?: ')
    choice3 = input('What is your second choice?: ')

def Second():
    global choice4
    global choice5
    global choice6
    choice4 = input('What is your first choice?: ')
    choice5 = input('What is your second choice?: ')
    choice6 = input('What is your third choice?: ')

def Third():
    global choice7
    global choice8
    global choice9
    global choice10
    choice7 = input('What is your first choice?: ')
    choice8 = input('What is your second choice?: ')
    choice9 = input('What is your third choice?: ')
    choice10 = input('What is your fourth choice?: ')

def Fourth():
        global choice11
        global choice12
        global choice13
        global choice14
        global choice15
        choice11 = input('What is your first choice?: ')
        choice12 = input('What is your second choice?: ')
        choice13 = input('What is your third choice?: ')
        choice14 = input('What is your fourth choice?: ')
        choice15 = input('What is your fifth choice?: ')

def Proccecing(rand):
    for x in (range(1,rand)):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Deciding')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Deciding.')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Deciding..')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Deciding...')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('-------------------------------')
    choices = input('how many choices do you have?: ')

    if not choices.strip():
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    
    if choices == 'break':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
        
    if choices == '2':
        First()
        os.system('cls' if os.name == 'nt' else 'clear')
        rand1 = random.randint(1,2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if rand1 == 1:
            Proccecing(rand)
            print('The choice was',choice2)
        if rand1 == 2:
                Proccecing(rand)
                print('The choice was',choice3)
        continue
        
    if choices == '3':
        Second()

        os.system('cls' if os.name == 'nt' else 'clear')
        rand2 = random.randint(1,3)
        if rand2 == 1:
            Proccecing(rand)
            print('The choice was',choice4)
        if rand2 == 2:
            Proccecing(rand)
            print('The choice was',choice5)
        if rand2 == 3:
            Proccecing(rand)
            print('The choice was',choice6)
        continue

    if choices == '4':
        Third()
        os.system('cls' if os.name == 'nt' else 'clear')
        rand3 = random.randint(1,4)
        if rand3 == 1:
            Proccecing(rand)
            print('The choice was',choice7)
        if rand3 == 2:
            Proccecing(rand)
            print('The choice was',choice8)
        if rand3 == 3:
            Proccecing(rand)
            print('The choice was',choice9)
        if rand3 == 4:
            Proccecing(rand)
            print(' choice was',choice10)
        continue

    if choices == '5':
        Fourth()
        os.system('cls' if os.name == 'nt' else 'clear')
        rand4 = random.randint(1,5)
        if rand4 == 1:
            Proccecing(rand)
            print('The choice was',choice11)
        if rand4 == 2:
            Proccecing(rand)
            print('The choice was',choice12)
        if rand4 == 3:
            Proccecing(rand)
            print('The choice was',choice13)
        if rand4 == 4:
            Proccecing(rand)
            print('The choice was',choice14)
        if rand4 == 5:
            Proccecing(rand)
            print('The choice was',choice15)
        continue

    else:
        print('Error, Please select a number from 2-5')
        