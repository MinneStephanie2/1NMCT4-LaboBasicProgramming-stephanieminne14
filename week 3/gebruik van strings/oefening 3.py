

def controle_mail (mailadres):
   pos = mailadres.find ("@student.howest.be")
   if pos == -1:
       return False
   voornaam_naam = mailadres[:pos]  #wegknippen achterste stukje

   voornaam_naam= voornaam_naam.replace(".","")
   controle_naam = voornaam_naam.isalnum()
   if (controle_naam == False):
       return False
   return True

mailadres = input("wat is je e-mail-adress van howest: ")
controle_mail(mailadres)
