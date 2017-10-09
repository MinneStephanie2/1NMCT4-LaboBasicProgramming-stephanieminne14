import random
gok =0
getal = random.randrange(0,21,1)


def nummer_raden ():
    gok = int(input("doen een gokje"))

    if (gok > getal):
        print ("kleiner!")
    elif(gok < getal):
        print("grooter!")
    else:
        print(getal)
        print("Goed geraden!")

while gok != getal:
    nummer_raden()
    if (gok == getal): break;





