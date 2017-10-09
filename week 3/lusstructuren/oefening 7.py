startwaarde = int(input("Geef u beginwaarde: "))
stapgrootte = int(input("geef de positieve stapgrootte"))
aantal_getallen =int(input("hoeveel getallen zijn er"))

def print_lijst_getallen (startwaarde, stapgrootte, aantal_getallen):

    for i in range(startwaarde,aantal_getallen,stapgrootte):
        print("De lijst is: [{0}]".format(i))
print_lijst_getallen(startwaarde,stapgrootte,aantal_getallen)
