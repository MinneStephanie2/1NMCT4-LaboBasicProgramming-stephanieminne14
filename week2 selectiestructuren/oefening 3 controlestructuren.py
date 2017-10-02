 #Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een
#gepaste melding af.

geboortejaar = int(input("Geef je geboortejaar"))

import datetime
jaar = datetime.datetime.now().year

leeftijd = jaar - geboortejaar

if(leeftijd <= 18):
  print("U bent nog geen 18! \n Kom volgend jaar terug...")
else:
  print("Ok, u mag alcohol drinken")