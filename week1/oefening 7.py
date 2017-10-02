totaal_seconden = float (input("geef het aantal seconden"))

dagen = int (totaal_seconden/86400)     #het aantal volledige dagen
rest1= int(totaal_seconden% 86400)      # de rest van de tijd in seconden

uren = int (rest1/3600)
rest2= int (rest1% 3600)

minuten = int (rest2 /60)
rest3 = int (rest2%60)


print ("dagen: {0} uren: {1} mintuten: {2} seconden {3}".format(dagen, uren,minuten,rest3))


#optie 2

#tijd = int ("geef aantal seconden: ")
# dagen = tijd // (3600*24)
#rest1 = tijd % (3600*24)

#uren = rest1//3600
#rest2 = rest1 % 3600

#mintuten = rest2 // 60
#seconden = rest2 %60

#print ("dagen: {0} uren: {1} mintuten: {2} seconden: {3}". format (dagen, uren, minuten, seconden))