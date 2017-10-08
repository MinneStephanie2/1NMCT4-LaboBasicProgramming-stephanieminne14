keuze = input("Welke eeneheid gebruikt u? (c: celsius, f: fahrenheit)")
f = 1
F = 1
c= 2
C =2

if (keuze == 1):
    fahrenheid = int(input("geef je tempertatuur in fahreneheid: "))
    def geef_celsius (fahrenheid):
        berekening_fahrenheid = (fahrenheid-32)*5/9
        print("je temperatuur in graden celsius is {0}".format(berekening_fahrenheid))
    print(geef_celsius(fahrenheid))
elif (keuze == 2):
    celsius = int (input("geef je temperatuur in graden celsius: "))
    def geef_fahrenheit (celsius):
        berekening_celsius = (celsius*9/5)+32
        print("je temperatuur in fahrenheid {0}".format(berekening_celsius))
    print(geef_fahrenheit(celsius))
else:
    print("Dit is geen geldige waarde")

