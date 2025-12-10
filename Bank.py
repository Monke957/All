import os
import time

balance = 0

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('-----------------------------------')
    print('1. Show your balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Store')
    print('5. Exit')
    choice = input('Choose 1-5: ')

    if choice == '5':
        break

    if choice == '1':
        print('-----------------------------------')
        print(f'Your balance is {balance}:gc') 

    
    if choice == '2':
        deposit = int(input('How much would you like to deposit: '))
        
        if deposit >= 1000000:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('5')
            time.sleep(1)
            print('4')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Error you dont have this much money ')
        
        else:
            balance += deposit
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-----------------------------------')
            print(f'Your new balance is {balance}:gc')

    if choice == '3':
        Withdraw = int(input('How much would you like to withdraw: '))
        

        
        if Withdraw >= balance:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Error you dont have this much money ')
            print('5')
            time.sleep(1)
            print('4')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
            balance -= Withdraw
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-----------------------------------')
            print(f'Your new balance is {balance}')

    if choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-----------------------------------')
        print(f'Your current balance is {balance}')
        print('-----------------------------------')
        print('1. Banana. Cost 5:gc')
        print('2. Cola. Cost 7:gc')
        print('3. Pizza. Cost 23:gc')
        #print('')
        #print('')
        storech = input('What would you like to buy?: ')
        if storech == '1':
            if balance <= 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Error you dont have the money')
                continue
            balance -= 5
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-----------------------------------')
            print(f'Your new balance is {balance}')
        
        if storech == '2':
            if balance <= 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Error you dont have the money')
                continue
            balance -= 7
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-----------------------------------')
            print(f'Your new balance is {balance}')
        
        if storech == '3':
            if balance <= 23:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Error you dont have the money')
                continue
            balance -= 23
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-----------------------------------')
            print(f'Your new balance is {balance}')


    