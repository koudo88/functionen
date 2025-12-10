def berechne_brutto(netto_preis, steuersatz = 0.19):
  brutto_preis = netto_preis * steuersatz
  return brutto_preis


print(berechne_brutto(4000))
berechne_brutto((4000, 0.07))
