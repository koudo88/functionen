
lagerbestand = 50 
def wareneingang(): 
global lagerbestand 
lagerbestand += 10 
print(f"Neuer Bestand: {lagerbestand}") 


def warenausgang(): 
global lagerbestand 
lagerbestand -= 5 
print(f"Neuer Bestand: {lagerbestand}") 
wareneingang() 
warenausgang()
