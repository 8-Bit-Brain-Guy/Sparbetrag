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
    # Get the value from the first entry and set it in the second entry
    value = entry1.get()
    entry2.delete(0, tk.END)  # Clear the second entry
    entry2.insert(0, value)   # Insert the value into the second entry

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
ZinsenEntry.insert(0, "5%")
EndbetragEntry.insert(0, "")

# Bind the first entry field to capture 'Tab' or 'Enter' key events
EndbetragEntry.bind("<Tab>", on_entry)
EndbetragEntry.bind("<Return>", on_entry)

# Bind the ESC key to close the window
root.bind("<Escape>", close_window)

# Create labels for the entry fields
label1 = tk.Label(root, text="Startbetrag:")
label2 = tk.Label(root, text="Sparbetrag (mtl):")


# Pack the labels and entry fields into the window
label1.pack(padx=10, pady=5)
StartbetragEntry.pack(padx=10, pady=10)
label2.pack(padx=10, pady=5)
Sparbetrag_mtlEntry.pack(padx=10, pady=10)
label3.pack(padx=10, pady=5)
LaufzeitEntry.pack(padx=10, pady=10)
label4.pack(padx=10, pady=5)
ZinsenEntry.pack(padx=10, pady=10)
label5.pack(padx=10, pady=5)
EndbetragEntry.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
