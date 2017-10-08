keuze = int (input("Welke eeneheid gebruikt u? (1: celsius, 2: fahrenheit)"))


def geef_celsius(keuze):
    fahrenheid = (celsius - 32) * 5 / 9
    print("je temperatuur in graden fahrenheid is {0}".format(fahrenheid))
    print(geef_celsius(fahrenheid))


def geef_fahrenheit(keuze):
    celsius = (fahrenheid * 9 / 5) + 32
    print("je temperatuur in celsius {0}".format(celsius))
    print(geef_fahrenheit(celsius))

if (keuze == 2):
    fahrenheid = (int(input("geef je tempertatuur in fahreneheid: ")))
    geef_fahrenheit(keuze)

elif (keuze == 1):
    celsius = (int (input("geef je temperatuur in graden celsius: ")))
    geef_celsius(keuze)
else:
    print("Dit is geen geldige waarde")

