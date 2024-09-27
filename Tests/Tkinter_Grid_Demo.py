import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Grid Layout Beispiel")

# Label und Eingabefeld erstellen
label1 = tk.Label(root, text="Name:")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="Alter:")
entry2 = tk.Entry(root)

# Button erstellen
button = tk.Button(root, text="Abschicken")

# Widgets mit Grid platzieren
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Event-Loop starten
root.mainloop()
