#oefening 6
#bereken eht aantal uren, minuten, seconden
dagen = float (input("geef het aantal dagen"))
uren = float(input("geef het aantal uren"))
minuten= float(input("geeft het aantal minuten"))
seconden = float(input("geef het aantal seconden"))
totaal_seconden= seconden + minuten*60 + uren*60*60 + dagen *24*60*60
print ( "de totale seconden is:{0}". format(totaal_seconden))