leeftijd_hond = int(input("geeft uw hond zijn leeftijd: "))

if (leeftijd_hond <= 0):
    print(" Dit zal niet kloppen")
elif ( leeftijd_hond == 1):
    print(" Je hond is 14 mensenjaren")
elif (leeftijd_hond == 2):
    print("Je hond is 22 in mensenjaren")
else:
    leeftijd_mens = 22 + (leeftijd_hond-2)*5
    print("uw hond is {0} in mensenjaren".format(leeftijd_mens))