import tkinter as tk

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
root.title("Eingabe Weitergabe")

# Create labels for the entry fields
label1 = tk.Label(root, text="Eingabefeld 1:")
label2 = tk.Label(root, text="Eingabefeld 2:")

# Create two entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Insert default values into the entry fields
entry1.insert(0, "Startwert 1")
entry2.insert(0, "Startwert 2")

# Bind the first entry field to capture 'Tab' or 'Enter' key events
entry1.bind("<Tab>", on_entry)
entry1.bind("<Return>", on_entry)

# Bind the ESC key to close the window
root.bind("<Escape>", close_window)

# Pack the labels and entry fields into the window
label1.pack(padx=10, pady=5)
entry1.pack(padx=10, pady=5)
label2.pack(padx=10, pady=5)
entry2.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
