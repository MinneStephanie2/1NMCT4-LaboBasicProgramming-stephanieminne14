maand = (int (input("Geef je maandnummer: ")))

def juisteMaandnummer (maand):
   maand = maand - 1
   maanden = ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober",
              "November", "December"]
   if (maand<= 12 and maand >=0):
         print("de maand is {0:s}".format(maanden[maand]))
   else:
        print ("Dit is een ongeldig getal")

print(juisteMaandnummer(maand))
