'''
Um ein Bild in einem Frame mit Tkinter anzuzeigen, kannst du das Label-Widget verwenden und das Bild in das Label einfügen.
Dazu benötigst du die Bibliothek Pillow (Python Imaging Library), um das Bild zu laden und im Tkinter-Format darzustellen.
'''

import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Bild im Frame anzeigen")

# Create a frame to hold the image
frame = Frame(root, width=300, height=300)
frame.pack(padx=10, pady=10)

# Load an image using Pillow
image = Image.open("Verlauf_Demo.png")  # Pfad zu deinem Bild
image = image.resize((200, 200))  # Bildgröße anpassen
photo = ImageTk.PhotoImage(image)

# Create a label to display the image and add it to the frame
label = tk.Label(frame, image=photo)
label.pack()

# Start the Tkinter event loop
root.mainloop()