from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

### Diese Flag kann aktiviert werden um das Debugging zu vereinfachen:
DEBUG = False

### Startparameter
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
        ax.plot(x, y)
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

#### Zwei Frames benutzen: Links Eingabefelder und Ausgabe für Endbetrag; Rechts detailierte Übersicht des Anwachsens des Entbetrages.
FrameLinks = tk.Frame(root)
FrameMitte = tk.Frame(root)
FrameRechts = tk.Frame(root)

#### Eingabefelder erzeugen
StartbetragEntry = tk.Entry(FrameLinks)
Sparbetrag_mtlEntry = tk.Entry(FrameLinks)
LaufzeitEntry = tk.Entry(FrameLinks)
ZinsenEntry = tk.Entry(FrameLinks)
EndbetragEntry = tk.Entry(FrameLinks)

#### Textfeld und Scrollbar erzeugen:
Textfeld = scrolledtext.ScrolledText(master=FrameMitte, width=30, height=20, wrap='word')

#### Erstelle ein Figure-Objekt und Canvas Objektes zum Plotten der berechneten Werte
fig = Figure(figsize=(5, 4), dpi=100)
#### Füge eine Subplot-Achse hinzu
ax = fig.add_subplot(111)
#### Einfügen der Figure in das Tkinter-Fenster
canvas = FigureCanvasTkAgg(fig, master=FrameRechts)
#### Rendern des Diagramms
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)


#### Labels für die Eingabefelder erzeugen
label1 = tk.Label(FrameLinks, text="Startbetrag", anchor="e")
label2 = tk.Label(FrameLinks, text="Sparbetrag (mtl)")
label3 = tk.Label(FrameLinks, text="Laufzeit (Monate)")
label4 = tk.Label(FrameLinks, text="Zinsen (jährl) (5% = 0.05)")
label5 = tk.Label(FrameLinks, text="Endbetrag")
label6 = tk.Label(FrameMitte, text="Details")
label7 = tk.Label(FrameRechts, text="Verlauf")

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

#### Pack the labels and entry fields into the window
#### Alles packen
FrameLinks.pack(side = tk.LEFT)
FrameMitte.pack(side = tk.LEFT)
FrameRechts.pack(side = tk.RIGHT)

label1.pack(padx=10, pady=5)
StartbetragEntry.pack(padx=10, pady=5)

label2.pack(padx=10, pady=5)
Sparbetrag_mtlEntry.pack(padx=10, pady=5)

label3.pack(padx=10, pady=5)
LaufzeitEntry.pack(padx=10, pady=5)

label4.pack(padx=10, pady=5)
ZinsenEntry.pack(padx=10, pady=5)

label5.pack(padx=10, pady=5)
EndbetragEntry.pack(padx=10, pady=5)

label6.pack(side = tk.TOP, padx=10, pady=5)
Textfeld.pack(side = tk.TOP, padx=5, pady=5)

label7.pack(side = tk.TOP, padx=10, pady=5)


#### Start the Tkinter event loop
os.system('cls')
root.mainloop()