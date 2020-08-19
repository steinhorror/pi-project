import whatispi as pi

first = True
de = True

def searchInPi():
    print("-" *27)
    print("\n Wie viele Nachkommastellen sollen berechnet werden? \n")
    pinum = pi.getPi(int(input("Eingabe: ")))
    print("-" *27)
    print("\n " + str(pinum) + "\n")
    input("<< Menü")

def searchInPisDecimals():
    print("-" *27)
    print("\n Nach welcher Zahl möchtest du in Pi suchen? \n")
    pisearch = input("Eingabe: ")
    schleife = True 
    numb = 10
    while(schleife == True):
        pinumb = pi.getPi(int(numb))
        pinumb = str(pinumb)
        pinumb = pinumb.split(".")[1]
        pinumb = pinumb.find(pisearch)
        if(pinumb == -1):
            if(numb == 10000):
                print("Möchten sie wirklich weiter suchen? Es könnte den PC sehr langsam machen\n")
                weiter = True
                if(weiter == True):
                    numb += 10
                else:
                    schleife = False
            numb += 10
            
    if(pinumb == -1):
        print("Die gewünschte Zahl wurde nicht gefunden falls sie die Zahl trotzdem suchen möchten drücken sie die 1 um zum Menü zu kommen einfach Enter drücken")
    else:
        print("die gewünschte Zahl efindet sich an der " + str(pi) + ". Nachkommastelle von Pi")
    

def menude():
    print("\n Drücke die folgenden Zahlen um das jeweilige Programm auszuführen.")
    print("\n 1. Pi mit einer ausgewählten Zahl an Nachkommastellen berechnen")
    print(" 2. Nach einer Zahl in Pis Nachkommastellen suchen")
    print(" 3. Sprache ändern\n")
    programState = input("Auswahl: ")
    if(programState == "1"):
        searchInPi()
    if(programState == "2"):
        searchInPisDecimals()
    if(programState == "3"):
        languages()

while de:
    if(first == True):
        print("\nPPPPPPPPPPPPPPPPP      iiii  \nP::::::::::::::::P    i::::i \nP::::::PPPPPP:::::P    iiii  \nPP:::::P     P:::::P         \n  P::::P     P:::::P iiiiiiii \n  P::::P     P:::::P i::::::i \n  P::::PPPPPP:::::P   i::::i \n  P:::::::::::::PP    i::::i \n  P::::PPPPPPPPP      i::::i \n  P::::P              i::::i \n  P::::P              i::::i \n  P::::P              i::::i \nPP::::::PP           i::::::i\nP::::::::P           i::::::i\nP::::::::P           i::::::i\nPPPPPPPPPP           iiiiiiii")
        first = False
    if(first == False):
        print("-" *27)
    menude()
