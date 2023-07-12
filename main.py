import tkinter as tk

def create_grid():
    window = tk.Toplevel()

    scales = [
        {"name": "Dorian", "scale": [2, 1, 2, 2, 2, 1, 2]},
        {"name": "Phrygian", "scale": [1, 2, 2, 2, 1, 2, 2]},
        {"name": "Lydian", "scale": [2, 2, 2, 1, 2, 2, 1]},
        {"name": "Mixolydian", "scale": [2, 2, 1, 2, 2, 1, 2]},
        {"name": "Aeolian", "scale": [2, 1, 2, 2, 1, 2, 2]},
        {"name": "Locrian", "scale": [1, 2, 2, 1, 2, 2, 2]}
    ]

    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    for i in range(13):
        for j in range(8):
            scale = scales[j % 6]
            note = notes[i]
            mode_name = note + " " + scale["name"]
            mode_scale = [note]
            current_note = note
            for step in scale["scale"]:
                index = notes.index(current_note)
                next_index = (index + step) % len(notes)
                next_note = notes[next_index]
                mode_scale.append(next_note)
                current_note = next_note
            mode_scale_text = " ".join(mode_scale)
            label = tk.Label(window, text=mode_name + "\n" + mode_scale_text, borderwidth=1, relief="solid", justify=tk.CENTER)
            label.grid(row=i, column=j)

root = tk.Tk()
root.title("mode scales")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 500) // 2
y = (screen_height - 500) // 2

# Set the window size and position
root.geometry(f'500x500+{x}+{y}')

button = tk.Button(root, text="click to see every single scale in every single mode", command=create_grid)
button.pack()

root.mainloop()

# all the patterns
#
# Major Scale: W, W, H, W, W, W, H
# Natural Minor Scale: W, H, W, W, H, W, W
# Dorian Mode is: W, H, W, W, W, H, W
# Mixolydian Mode is: W, W, H, W, W, H, W
