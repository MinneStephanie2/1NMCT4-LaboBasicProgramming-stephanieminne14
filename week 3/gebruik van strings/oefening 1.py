woord1 = input("Geef een woord op: ")
woord2 = input("geef een tweede woord op: ")

def swap ():
   stuk1 = (woord1[:2])
   stuk2 =(woord1[2:])
   stuk3 = (woord2[:2])
   stuk4 = woord2[2:]

   nieuw_woord = ("{0}{1} {2}{3}".format(stuk3,stuk2,stuk1,stuk4))
   print (nieuw_woord)


swap()