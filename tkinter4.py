from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("300x397") # width x height
root.title("This is my page")
# Important label options
# text - adds the text
#  bd - background
# fg - foreground
# font - sets the font font=("TimesNewRoman",19,"bold")
# padx - x padding
# pady - y padding
# relief - border stylling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''This module provides a \nportable way of using operating system dependent \nfunctionality. If you just want to read or write a \nfile see open(), if you want to manipulate paths, see \nthe os.path module, and if you want to read all the \nlines in all the files on the command line see the \nfileinput module. For creating temporary files and \ndirectories see the tempfile module, and for \nhigh-level file and directory handling see the shutil module.
\nNotes on the availability of these functions:''',  bg ="red", fg="white", padx=23, pady=34, font="comicsansms 19 bold", borderwidth=8, relief = GROOVE)
# Important pack options
# anchor - north west - nw
# side = top,bottom, left, right
# # title_label.pack(anchor="nw")
# title_label.pack(side=BOTTOM, anchor="sw", fill=x)
# fill =x , in  x direction color will expand
#padx
#pady
title_label.pack(side=LEFT, fill =Y, padx= 45, pady=90)
title_label.pack()
root.mainloop()