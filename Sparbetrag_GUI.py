import tkinter as tk
import os

### Parameter
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

        
        # Zinseszinsformel mit monatlicher Einzahlung E = r * q * (q^n-1) / (q-1)
        # r = monatl. rate
        # n = Einzahlungsdauer in Monaten
        # q = Montatszinsfaktor == Zinsen/12
        
        EndbetragValue = Startbetrag + Sparbetrag_mtl * Zinsen_mtl * (pow(Zinsen_mtl, Laufzeit) - 1) / (Zinsen_mtl - 1)
        
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
root.title("Sparbetrag")

# Eingabefelder erzeugen
StartbetragEntry = tk.Entry(root)
Sparbetrag_mtlEntry = tk.Entry(root)
LaufzeitEntry = tk.Entry(root)
ZinsenEntry = tk.Entry(root)
EndbetragEntry = tk.Entry(root)

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

# Create labels for the entry fields
label1 = tk.Label(root, text="Startbetrag")
label2 = tk.Label(root, text="Sparbetrag (mtl)")
label3 = tk.Label(root, text="Laufzeit (Monate)")
label4 = tk.Label(root, text="Zinsen (jährl) (5% = 0.05)")
label5 = tk.Label(root, text="Endbetrag")


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

# Start the Tkinter event loop
os.system('cls')
root.mainloop()

