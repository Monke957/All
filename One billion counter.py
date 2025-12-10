import os
import keyboard

os.system('cls' if os.name == 'nt' else 'clear')


while True:
    print('1. Ip')
    print('2. Hardware')
    print('3. Weather')
    print('4. ')
    print('5.')
    info = input('what system info would you like to see. (1-5): ')

    if info == '1':
        os.system(command='ipconfig')

    if info == '2':
        os.system(command='systeminfo')

    if info == '3':
        Wea = input('Where would you like to see the forecast?: ')
        os.system(command=f'curl wttr.in/{Wea}')



