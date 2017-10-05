a = int (input("geef een getal: "))
b = int (input("geef een getal: "))
c = int( input("geef een getal: "))
d = int( input("geef een getal: "))

def berekenSom (a,b,c=0,d=0):
    berekening = a-b+c-d
    print("de uitkomst is {0}".format(berekening))
berekenSom(a,b,c,d)
berekenSom(a,b,c,d)

berekenSom(a,b)


