import tkinter as tk

def on_entry(event):
    # Get the value from the first entry and set it in the second entry
    value = entry1.get()
    entry2.delete(0, tk.END)  # Clear the second entry
    entry2.insert(0, value)   # Insert the value into the second entry

# Create the main window
root = tk.Tk()
root.title("Eingabe Weitergabe")

# Create two entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Bind the first entry field to capture 'Tab' or 'Enter' key events
entry1.bind("<Tab>", on_entry)
entry1.bind("<Return>", on_entry)

# Pack the entries into the window
entry1.pack(padx=10, pady=10)
entry2.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
