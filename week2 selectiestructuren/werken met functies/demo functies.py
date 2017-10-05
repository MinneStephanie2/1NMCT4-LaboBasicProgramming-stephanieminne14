# lengt = 4
# breedte = 6
# oppervlaketehoek= lengt*breedte
#
# lengt2= 3
# breedte2 = 8
# oppervlaketehoek2= lengt2*breedte2

# lengte = int (input("geef de lengte"))
# breedte = int( input("geef de breedte"))
# #functie schrijven
def berkenoppervlakteRechthoek (lengte =0, breedte=0): #eventueel kan je een default meegeven door bv:lengte =0
    #alle statements met de tab indent behoren tot deze functie
    if (lengte == 0) and (breedte ==0):
        lengte = int(input("geef de lengte: "))
        breedte = int(input("geef de breedte: "))
    oppervlakte = lengte*breedte
    print("de oppervlakte is {0}".format(oppervlakte))
    print ("de breedte is {0}".format(breedte))
berkenoppervlakteRechthoek(3,8)
berkenoppervlakteRechthoek(8,10)
berkenoppervlakteRechthoek(breedte=3, lengte=4)
berkenoppervlakteRechthoek()


# def wordt geskipt tot het laatste deel van de comandeno (vb: berkenoppervlakteRechthoek())
# eerst variablen, dan def en als laatste code

#tussen de haakjes kan je een parrameter meegeven
