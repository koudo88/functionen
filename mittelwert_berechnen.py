def mittelwer_berechnen(* args):
  mittel = sum(args)/ len(args)
return mittel

print(mittelwer_berechnen(1,2,3))
print(mittelwer_berechnen(10,20,30,40,50))

def berechne_mittelwert(*werte: int) -> int:
    """Berechnet den arithmetischen Mittelwert beliebig vieler Zahlen.

    Args:
        *werte: Eine beliebige Anzahl an Ganzzahlen,deren Durchschnitt ermittelt werden soll.

    Returns:
        float: Der Durchschnitt aller übergebenen Werte.

    Raises:
        ValueError: Wenn keine Werte übergeben wurden.
    """
    if not werte:
        raise ValueError("Es muss mindestens ein numerischer Wert übergeben werden.")
    

    return sum((wert) for wert in werte) / len(werte)
  
  print(berechne_mittelwert(1, 2, 3))              
  print(berechne_mittelwert(10, 20, 30, 40, 50))   



  
