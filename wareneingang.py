
lagerbestand = 50 
def wareneingang(menge): 
  bestand = lagerbestand + menge
return bestand 


def warenausgang(menge): 
 neue_bestand = lagerbestand - menge
return neue_bestand 

print(wareneingang(menge))
print(warenausgang(menge))
