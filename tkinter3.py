from tkinter import *
from PIL import Image, ImageTk
image_root = Tk()

image_root.geometry("600x787")
# photo = PhotoImage(file="logo512.png")
# for jpg files
photo1 = Image.open("rajasthani arts.jpg")
image1 = ImageTk.PhotoImage(photo1)
vanshika_label = Label(image=image1)
vanshika_label.pack()
image_root.mainloop()
