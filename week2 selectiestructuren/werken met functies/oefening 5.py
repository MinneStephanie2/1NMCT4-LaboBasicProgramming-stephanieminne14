maandnummer = int (input("geef een maandnummer"))
list = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "novermber", "december"]
maand = list [maandnummer]
def juisteMaandnummer (maandnummer):
    if (maandnummer> 12)or (maandnummer <0):
        print("ongeldig maandnummer!")
    else:
        print ("Dit maandnummer komt overeen met {0}".format(maand)
#list gebruiken
 print(juisteMaandnummer(maandnummer))
