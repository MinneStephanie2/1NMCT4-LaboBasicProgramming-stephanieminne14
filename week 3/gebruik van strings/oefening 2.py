naam = input("geef uw naam: ")
voornaam = input("geef uw voornaam: ")
geboortedatum = input("Geef uw geboortedatum (formaat: dd-mm-yyyy): ")

def paswoord ():
    deel1 = (naam [:3])
    deel1 = deel1.lower()
    deel2 = (voornaam [:2])
    deel2 = deel2.upper()
    deel2 = deel2.replace(" ","")
    deel3 = (geboortedatum[3:8])
    deel3 = deel3.replace("-","")

    paswoord= ("{0}{1}{2}".format(deel1,deel2,deel3))
    print ("jouw paswoord is {0}".format(paswoord))
paswoord()