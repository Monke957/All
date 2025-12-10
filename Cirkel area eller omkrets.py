import os

pi = 3.14
rund = 360.0
j = True
h = True

def Area():
    print("skriv radie = ", end=" ")
    radie = input("")
    radie = float(radie)
    area = radie*radie*pi
    print("\n")
    print("Arean =", area, menh)

def båge():
    print("skriv vinkeln på 'cirkel biten': ", end="")
    vinkeln = input("")
    vinkeln = float(vinkeln)
    print("vad är diametern?: ", end="")
    diametern = input("")
    diametern = float(diametern)
    bågen = diametern*pi*vinkeln/rund
    print("\n")
    print("bågen = ",bågen, menh)
         
def sektor():
    print("skriv vinkeln på 'cirkel biten': ", end="")
    vinkeln = input("")
    vinkeln = float(vinkeln)
    print("vad är radien?: ", end="")
    radien = input("")
    radien = float(radien)
    sektorn = (radien*radien)*pi*vinkeln/rund
    print("\n")
    print("sektorn = ",sektorn, menh)
    
def Omkrets():
        print("skriv diametern = ", end=" ")
        diameter = input("")
        diameter = float(diameter)
        omkrets = diameter*pi
        print("\n")
        print("Omkretsen =", omkrets, menh)

def Volym():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Vad är höjden?: ", end="")
    höjd = input("")
    höjd = float(höjd)

    print("Vad är bredden?: ", end="")
    bredd = input("")
    bredd = float(bredd)

    print("Vad är djupet?: ", end="")
    djup = input("")
    djup = float(djup)

    svar = höjd*bredd*djup
    print(f"Volymen = {svar}{menh}")



def vb():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Vad vill du räkna? Volym, begränsingsarea. V/B: ", end="")
    VB = input("")

    if VB == "V" or vad == "v":
        Volym()
        print(" ")
        print("Press enter to continue...", end="")
        input("")
    #elif VB == "B" or VB == "b":

    


def cirkel():
    i = True
    while i == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        

        print("Vill du räkna area, omkrets, cirkel-båge, cirkel-sektor? A/O/CB/CS... = ", end="")


        AeO = input("")

        if AeO == "A" or AeO == "a":
            os.system('cls' if os.name == 'nt' else 'clear')
            Area()
            print(" ")
            print(" ")
            print("vill du räkna ett till tal? J/N... = ", end="")
            a = input("")

            if a == "J" or a == "j":
                continue
            elif a == "N" or a == "n":
                i = False
                
            else:
                print("ERROR: Svara med J för Ja eller N för Nej")
        elif AeO == "O" or AeO == "o":
            os.system('cls' if os.name == 'nt' else 'clear')
            Omkrets()
            print(" ")
            print(" ")
            print("vill du räkna ett till tal? J/N... = ", end="")
            a = input("")

            if a == "J" or a == "j":
                continue
            elif a == "N" or a == "n":
                i = False
            else:
                print("ERROR: Svara med J för Ja eller N för Nej")
    
        elif AeO == "CB" or AeO == "cb" or AeO == "Cb" or AeO == "cB":
            os.system('cls' if os.name == 'nt' else 'clear')
            båge()
            print(" ")
            print(" ")
            print("vill du räkna ett till tal? J/N... = ", end="")
            a = input("")

            if a == "J" or a == "j":
                continue
            elif a == "N" or a == "n":
                i = False
            else:
                print("ERROR: Svara med J för Ja eller N för Nej")

        elif AeO == "CS" or AeO == "cs" or AeO == "Cs" or AeO == "cS":
            os.system('cls' if os.name == 'nt' else 'clear')
            sektor()
            print(" ")
            print(" ")
            print("vill du räkna ett till tal? J/N... = ", end="")
            a = input("")

            if a == "J" or a == "j":
                continue
            elif a == "N" or a == "n":
                i = False
            else:
                print("ERROR: Svara med J för Ja eller N för Nej")
        
        else:
            print("ERROR: svara A för area eller O för omkrets...")

while j == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Vill du avsluta? J/N: ", end="")
    
    print("Vilken mått enhet? = ", end="")
    global menh
    menh = input("")
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Vad vill du räkna?: Algebra eller Rätblock. A/R: ", end="")
    vad = input("")
    

    if vad == "A" or vad == "a":
        cirkel()
    elif vad == "R" or vad == "r":
        vb()

    



    



    

        

