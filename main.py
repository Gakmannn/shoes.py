import tkinter as tk
from tkinter import * 
from tkinter import messagebox

window = Tk() 
window.title("Обувной магазин")
window.geometry("500x250")

btn = tk.Button(text="Click Me", command=click_button)
btn.pack()

window.mainloop()