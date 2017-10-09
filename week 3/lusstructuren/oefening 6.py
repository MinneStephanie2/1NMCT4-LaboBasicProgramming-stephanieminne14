def print_getallen ():
    getal =0
    for getal in range (200,309):
        #enkel getalen deelbaar door zeven
        if (getal %7) == 0:
            #controle of alles juist is en dan nog kijken hoe het deelbaar is door 5
            if (getal %5) != 0:
                print (getal)
print_getallen()