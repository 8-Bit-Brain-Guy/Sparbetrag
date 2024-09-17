# Parameter
Endbetrag = 0
Startbetrag = 0
Sparbetrag_mtl = 250.0
Laufzeit = 120
zinsen = 0.05
zinsen_mtl = (zinsen / 12)

Endbetrag = Startbetrag
for i in range(Laufzeit+0):
    Endbetrag = Endbetrag + (Endbetrag * zinsen_mtl) + Sparbetrag_mtl
    if (i % 12 == 0):
        print("Betrag aktuell: %f" %Endbetrag)

print("Endbetrag: %f" %Endbetrag)


