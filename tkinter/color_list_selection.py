import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("bg color changer")
win.geometry("300x300")
colors=["red","blue","yellow"]

def color_changer(event):
    bg_color=combox.get()
    win.configure(bg=bg_color)

combox=ttk.Combobox(win, values=colors)
combox.pack(pady=100)
combox.set("choose a color")
combox.bind("<<ComboboxSelected>>", color_changer)

win.mainloop()