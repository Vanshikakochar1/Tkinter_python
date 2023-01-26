from tkinter import *

label_root = Tk()
# width * height
label_root.geometry("444x567")
# width , height
# label_root.minsize(200, 100)  # minimum size lock
# width , height
# label_root.maxsize(1200, 800)  # lock maximize

label = Label(text="this is a GUI")
label.pack()
label_root.mainloop()  # provides basic gui window - blank window