from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("Strip in Red")

s_label = Label(text="SUBMIT", bg="red", fg="white", borderwidth=10)
s_label.pack(side=BOTTOM, anchor="sw", fill=Y,padx=45, pady=45 )
c_label = Label(text="CANCEL", bg="grey", fg="white", borderwidth=10)

c_label.pack(side=BOTTOM, anchor="sw" )

root.mainloop()