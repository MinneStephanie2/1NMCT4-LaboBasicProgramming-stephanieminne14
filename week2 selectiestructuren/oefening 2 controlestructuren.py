 #Vraag een niet decimaal getal aan de gebruiker op. Bepaal of het opgegeven getal even of
#oneven is. Print een gepaste boodschap af.

getal = float (input ("geef een decimaal getal"))

resultaat = getal/2
if (resultaat % 2)== 0:
    print("je heb een even getal")
else: print("je hebt een oneven getal")

