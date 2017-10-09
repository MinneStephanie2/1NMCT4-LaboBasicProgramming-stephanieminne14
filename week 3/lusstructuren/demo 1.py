# # #oneindige lus
# # def oneinige_lus():
# #     i=6
# #
# # while (i > 0):
# #     i+=1
# #     print(i)
#
#
# #print 10 veelvouden van een getal
# def print_tien_veelvouden_van(getal):
#     for i in range (0,11):
#         print (i*getal)
#
# print_tien_veelvouden_van(6)
#
# #returne
# #oppervlakete cirkel
import math
def berken_oppervlakte_cirkle (diameter):
    opp = ((diameter/2)**2) * math.pi
    return opp
#de variable oppervlakte wordt het resultaat van de return waarde van mijn functie
oppervlakte = berken_oppervlakte_cirkle(2)
print(oppervlakte)