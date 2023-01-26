from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
root.geometry("600x300")
image = Image.open("rajasthani arts.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()
dirs = os.listdir()
label2 = Label(text=dirs)
label2.pack()
root.mainloop()