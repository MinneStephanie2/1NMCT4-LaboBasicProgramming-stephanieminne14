zin = ("dit is een string!")

print (zin)
print (zin [4:])
print (zin[4:6])
print (zin[:3]) #vanaf 0 beginnen en drie karakters

zin_uppercase = zin.upper()
print (zin_uppercase)

zin_filename = zin.replace(" ","_") #spaties vervangen door _
print(zin_filename)

pos = zin.index("i") #zoeken naar het eerste plaats van de i, als hij het niet vind krijg je foutmelding
print (pos)

zin.find("is") #als hij het niet vind krijg je een min 1 teruge

controle = zin.isalnum()
print(controle)