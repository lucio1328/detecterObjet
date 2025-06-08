import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def load_image():
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    img = img.resize((224, 224))
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

root = tk.Tk()
panel = tk.Label(root)
panel.pack()

load_button = tk.Button(root, text="Charger une image", command=load_image)
load_button.pack()

root.mainloop()
