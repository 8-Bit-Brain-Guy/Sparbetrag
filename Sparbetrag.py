import os

### Parameter
Endbetrag = 0
Startbetrag = 0
Sparbetrag_mtl = 250.0
Laufzeit = 120
Zinsen = 0.05
Zinsen_mtl = (Zinsen / 12)

### Berechnung
Endbetrag = Startbetrag
Monatsbetraege = []
for i in range(Laufzeit+1):    
    Endbetrag = Endbetrag + (Endbetrag * Zinsen_mtl) + Sparbetrag_mtl
    Monatsbetraege.append(Endbetrag)



### Analyse
os.system('cls')
print("########## Übersicht ##########")
print("Parameter: ")
print("Startbetrag:     %.2f" %Startbetrag)
print("Sparbetrag_mtl:  %.2f" %Sparbetrag_mtl)
print("Laufzeit:        %d" %Laufzeit)
print("Zinsen:          %.2f" %Zinsen)
print("\n")
print("Analyse:")
print("Monat        Betrag aktuell:")
for i in range(len(Monatsbetraege)):    
    if (i % 12 == 0):
        print("%d            %.2f" %(i, Monatsbetraege[i]))

print("-------------------------------")
print("Endbetrag:     %.2f\n" %Endbetrag)