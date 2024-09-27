import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Funktion zur Erstellung eines einfachen Diagramms
def plot():
    # Erstelle ein Figure-Objekt
    fig = Figure(figsize=(5, 4), dpi=100)

    # Füge eine Subplot-Achse hinzu
    ax = fig.add_subplot(111)

    # Daten zum Plotten
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Erzeuge das Diagramm
    ax.plot(x, y)

    # Binde das Diagramm an das Tkinter-Fenster
    canvas = FigureCanvasTkAgg(fig, master=root)  # Einfügen der Figure in das Tkinter-Fenster
    canvas.draw()  # Rendern des Diagramms
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Matplotlib Diagramm in Tkinter")

# Erstelle einen Button, um das Diagramm anzuzeigen
button = tk.Button(root, text="Diagramm anzeigen", command=plot)
button.pack(padx=10, pady=10)

# Start des Tkinter-Event-Loops
root.mainloop()
