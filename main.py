
import tkinter as tk
from tkinter import messagebox

def button_click():
    selected_note = note_var.get()
    message = "Notes: "
    for p in pattern:
        message += selected_note + " "
        note_index = notes.index(selected_note)
        note_index = (note_index + p) % len(notes)
        selected_note = notes[note_index]
    messagebox.showinfo("Scale", message)

window = tk.Tk()

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
pattern = [0, 2, 2, 1, 2, 2, 2, 1]

note_var = tk.StringVar(window)
note_var.set(notes[0])

dropdown_note = tk.OptionMenu(window, note_var, *notes)
dropdown_note.pack()

button = tk.Button(window, text="Get Scale", command=button_click)
button.pack()

window.mainloop()
