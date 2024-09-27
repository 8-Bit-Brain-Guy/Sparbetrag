from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

#### Diese Flag kann aktiviert werden um das Debugging zu vereinfachen:
DEBUG = False

#### GUI Parameter
padxLabel = 5
padyLabel = 5
padxEntry = 5
padyEntry = 5
padxTextfeld = 5
padyTextfeld = 5
padxCanvas = 5
padyCanvas = 5

#### Startwerte
Endbetrag = 0
Startbetrag = 0
Sparbetrag_mtl = 250.0
Laufzeit = 120
Zinsen = 0.05
Zinsen_mtl = (Zinsen / 12)


#### Callback Funktionen
def on_entry(event):
    #### Die Werte aus den Edit-Feldern einlesen
    if DEBUG:
        print("Die Callback-Funktion \"on entry\" wurde aufgerufen.")
        print((StartbetragEntry.get()))
        print((Sparbetrag_mtlEntry.get()))
        print((LaufzeitEntry.get()))
        print((ZinsenEntry.get()))

    try:
        StartbetragValue = (float)(StartbetragEntry.get())
        Sparbetrag_mtlValue = (float)(Sparbetrag_mtlEntry.get())
        LaufzeitValue = (int)(LaufzeitEntry.get())
        ZinsenValue = (float)(ZinsenEntry.get())
        Zinsen_mtlValue = (float)(ZinsenValue / 12)
        if DEBUG:
            print("Startbetrag    Sparbetrag (mtl.)    Laufzeit    Zinsen (jähl.)")
            print("%f    %f    %f    %f" %(StartbetragValue, Sparbetrag_mtlValue, LaufzeitValue, ZinsenValue))

        #### Berechnen der Gesamtsumme zu Laufzeitende:
        # Zinseszinsformel mit monatlicher Einzahlung E = r * q * (q^n-1) / (q-1)
        # r = monatl. rate
        # n = Einzahlungsdauer in Monaten
        # q = Montatszinsfaktor == (1 + Zinsen/12)
        q = 1 + Zinsen_mtlValue
        EndbetragValue = StartbetragValue + Sparbetrag_mtlValue * q * (pow(q, LaufzeitValue) - 1) / (q - 1)

        #### Clear the second entry
        EndbetragEntry.delete(0, tk.END)
        ### Insert the value into the second entry
        EndbetragEntry.insert(0, round(EndbetragValue, 2))

        #### Textfeld mit Verlauf der Gesamtsumme füllen
        Textfeld.delete(1.0, tk.END)
        #Textfeld.delete(0, tk.END)
        Textfeld.insert(END, "Monat     Wert\n")
        # Zwischenwert = Startbetrag + (Startbetrag*Zinsen_mtlValue)
        Zwischenwert = StartbetragValue + Sparbetrag_mtlValue
        Monatsbetraege = []
        for i in range(1, LaufzeitValue+1):
            Zwischenwert = Zwischenwert + (Zwischenwert * Zinsen_mtlValue)
            Monatsbetraege.append(Zwischenwert)
            #if ((i % 12 == 0) or (i in range(1, 12)) ):
            Textfeld.insert(END, "%s         %s\n" % (i, round(Zwischenwert, 2)))

            Zwischenwert = Zwischenwert + Sparbetrag_mtlValue

        #### Plotten der Daten
        x = range(1, LaufzeitValue+1)
        y = Monatsbetraege
        ax.plot(x, y, 'o', markersize=5)
        canvas.draw()  # Rendern des Diagramms

    except:
        EndbetragEntry.delete(0, tk.END)
        EndbetragEntry.insert(0, "Fehler")
        print("Fehler")


def close_window(event):
    #### Close the window when ESC is pressed
    root.destroy()



#### Create the main window
root = tk.Tk()
#root.geometry("850x450")
root.title("Sparbetrag")


#### Eingabefelder erzeugen
StartbetragEntry = tk.Entry(root)
Sparbetrag_mtlEntry = tk.Entry(root)
LaufzeitEntry = tk.Entry(root)
ZinsenEntry = tk.Entry(root)
EndbetragEntry = tk.Entry(root)

#### Textfeld und Scrollbar erzeugen:
Textfeld = scrolledtext.ScrolledText(master=root, width=30, height=20, wrap='word')

#### Erstelle ein Figure-Objekt und Canvas Objektes zum Plotten der berechneten Werte
fig = Figure(figsize=(5, 4), dpi=80)
#### Füge eine Subplot-Achse hinzu
ax = fig.add_subplot(111)
ax.set(xlabel='Monat', ylabel='Sparbetrag')
ax.grid()

#### Einfügen der Figure in das Tkinter-Fenster
canvas = FigureCanvasTkAgg(fig, master=root)
#### Rendern des Diagramms
canvas.draw()


#### Labels für die Eingabefelder erzeugen
label1 = tk.Label(root, text="Startbetrag", anchor="e")
label2 = tk.Label(root, text="Sparbetrag (mtl)")
label3 = tk.Label(root, text="Laufzeit (Monate)")
label4 = tk.Label(root, text="Zinsen (jährl) (5% = 0.05)")
label5 = tk.Label(root, text="Endbetrag")
label6 = tk.Label(root, text="Details")
label7 = tk.Label(root, text="Verlauf")

#### Default Werte in die Eingabefelder einfügen
StartbetragEntry.insert(0, "0.0")
Sparbetrag_mtlEntry.insert(0, "250.0")
LaufzeitEntry.insert(0, "120")
ZinsenEntry.insert(0, "0.05")
EndbetragEntry.insert(0, "")

#### Bind the first entry field to capture 'Tab' or 'Enter' key events
StartbetragEntry.bind("<Tab>", on_entry)
Sparbetrag_mtlEntry.bind("<Tab>", on_entry)
LaufzeitEntry.bind("<Tab>", on_entry)
ZinsenEntry.bind("<Tab>", on_entry)

StartbetragEntry.bind("<Return>", on_entry)
Sparbetrag_mtlEntry.bind("<Return>", on_entry)
LaufzeitEntry.bind("<Return>", on_entry)
ZinsenEntry.bind("<Return>", on_entry)

#### Bind the ESC key to close the window
root.bind("<Escape>", close_window)

#### Alles per Grid im Fenster anordnen. Die Fenstergröße passt sich automatisch an die belegte Fläche der Elemente an.
label1.grid(row=0, column=0, padx=padxLabel, pady=padyLabel)
StartbetragEntry.grid(row=1, column=0, padx=padxEntry, pady=padyEntry)
label2.grid(row=2, column=0, padx=padxLabel, pady=padyLabel)
Sparbetrag_mtlEntry.grid(row=3, column=0, padx=padxEntry, pady=padyEntry)
label3.grid(row=4, column=0, padx=padxLabel, pady=padyLabel)
LaufzeitEntry.grid(row=5, column=0, padx=padxEntry, pady=padyEntry)
label4.grid(row=6, column=0, padx=padxLabel, pady=padyLabel)
ZinsenEntry.grid(row=7, column=0, padx=padxEntry, pady=padyEntry)
label5.grid(row=8, column=0, padx=padxLabel, pady=padyLabel)
EndbetragEntry.grid(row=9, column=0, padx=padxEntry, pady=padyEntry)

label6.grid(row=0, column=1, padx=padxLabel, pady=padyLabel)
Textfeld.grid(row=1, column=1, rowspan=9, padx=padxTextfeld, pady=padyTextfeld)
label7.grid(row=0, column=2, padx=padxLabel, pady=padyLabel)
canvas.get_tk_widget().grid(row=1, column=2, rowspan=9, padx=padxCanvas, pady=padyCanvas)


######################################
#### Start the Tkinter event loop ####
######################################
os.system('cls')
root.mainloop()