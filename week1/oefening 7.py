totaal_seconden = float (input("geef het aantal seconden"))

dagen = int (totaal_seconden/86400)
rest1= int(totaal_seconden% 86400)

uren = int (rest1/3600)
rest2= int (rest1% 3600)

minuten = int (rest2 /60)
rest3 = int (rest2%60)


print ("dagen: {0} uren: {1} mintuten: {2} seconden {3}".format(dagen, uren,minuten,rest3))