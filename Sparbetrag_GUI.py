from tkinter import *
import tkinter as tk
import os

### Starting Parameters
Endbetrag = 0
Startbetrag = 0
Sparbetrag_mtl = 250.0
Laufzeit = 120
Zinsen = 0.05
Zinsen_mtl = (Zinsen / 12)




def on_entry(event):
    # Get the value from the entries and set it in the second entry
    try:
        StartbetragValue = (float)(StartbetragEntry.get())
        Sparbetrag_mtlValue = (float)(Sparbetrag_mtlEntry.get())
        LaufzeitValue = (int)(LaufzeitEntry.get())
        ZinsenValue = (float)(ZinsenEntry.get())
        print("StartbetragValue: %s" %StartbetragValue)
        print("Startbetrag_mtlValue: %s" %Startbetrag_mtlValue)
        print(Startbetrag_mtlValue)
        print(LaufzeitValue)
        print(ZinsenValue)
        # print("%f    %f    %n    %f" %(StartbetragValue, Sparbetrag_mtlValue, LaufzeitValue, ZinsenValue))
        
        # Zinseszinsformel mit monatlicher Einzahlung E = r * q * (q^n-1) / (q-1)
        # r = monatl. rate
        # n = Einzahlungsdauer in Monaten
        # q = Montatszinsfaktor == (1 + Zinsen/12)
        q = 1 + Zinsen_mtl
        
        EndbetragValue = Startbetrag + Sparbetrag_mtl * q * (pow(q, Laufzeit) - 1) / (q - 1)
        
        EndbetragEntry.delete(0, tk.END)  # Clear the second entry
        EndbetragEntry.insert(0, round(EndbetragValue, 2))   # Insert the value into the second entry
    except:
        EndbetragEntry.delete(0, tk.END)  # Clear the second entry
        EndbetragEntry.insert(0, "Fehler")   # Insert the value into the second entry



def close_window(event):
    # Close the window when ESC is pressed
    root.destroy()



# Create the main window
root = tk.Tk()
root.geometry("400x330")
root.title("Sparbetrag")

# Zwei Frames benutzen: Links Eingabefelder und Ausgabe für Endbetrag; Rechts detailierte Übersicht des Anwachsens des Entbetrages.
FrameLinks = tk.Frame(root)
FrameLinks.pack()
FrameLinks.pack(side = tk.LEFT)

FrameRechts = tk.Frame(root)
FrameRechts.pack()
FrameRechts.pack(side = tk.RIGHT)

# Eingabefelder erzeugen
StartbetragEntry = tk.Entry(FrameLinks)
Sparbetrag_mtlEntry = tk.Entry(FrameLinks)
LaufzeitEntry = tk.Entry(FrameLinks)
ZinsenEntry = tk.Entry(FrameLinks)
EndbetragEntry = tk.Entry(FrameLinks)


# Textfeld erzeugen:
Textfeld = tk.Text(master=FrameRechts, width=39, height=15, wrap='word')


# Create labels for the entry fields
label1 = tk.Label(FrameLinks, text="Startbetrag", anchor="e")
label2 = tk.Label(FrameLinks, text="Sparbetrag (mtl)")
label3 = tk.Label(FrameLinks, text="Laufzeit (Monate)")
label4 = tk.Label(FrameLinks, text="Zinsen (jährl) (5% = 0.05)")
label5 = tk.Label(FrameLinks, text="Endbetrag")
label6 = tk.Label(FrameRechts, text="Details")



# Insert default values into the entry fields
StartbetragEntry.insert(0, "0.0")
Sparbetrag_mtlEntry.insert(0, "250.0")
LaufzeitEntry.insert(0, "120")
ZinsenEntry.insert(0, "0.05")
EndbetragEntry.insert(0, "")

# Bind the first entry field to capture 'Tab' or 'Enter' key events
StartbetragEntry.bind("<Tab>", on_entry)
Sparbetrag_mtlEntry.bind("<Tab>", on_entry)
LaufzeitEntry.bind("<Tab>", on_entry)
ZinsenEntry.bind("<Tab>", on_entry)

StartbetragEntry.bind("<Return>", on_entry)
Sparbetrag_mtlEntry.bind("<Return>", on_entry)
LaufzeitEntry.bind("<Return>", on_entry)
ZinsenEntry.bind("<Return>", on_entry)




# Bind the ESC key to close the window
root.bind("<Escape>", close_window)




# Pack the labels and entry fields into the window
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
Textfeld.pack(side = tk.BOTTOM, padx=1, pady=5)

# Start the Tkinter event loop
os.system('cls')
root.mainloop()

