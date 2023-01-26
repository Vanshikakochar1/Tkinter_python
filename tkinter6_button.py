from tkinter import *
root = Tk()
root.geometry("675x333")

def hello1():
    print("harr pal teriyan yaadan te yaadan vich hai tu")

def hello2():
    print("Do you know m tenu kinaa pyaar krda do you know")

def hello3():
    print("Slow motion mei doob jau teri aankho k hoshan m ")

def hello4():
    print("Lemonade ")


frame = Frame(root, borderwidth=8, bg="grey", relief = SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print1" , command = hello1)
b1.pack(side=LEFT, padx = 13 ,pady=20)

b2 = Button(frame, fg="red", text="Print2", command = hello2)
b2.pack(side=LEFT, padx = 13 ,pady=20)

b3= Button(frame, fg="red", text="Print3", command = hello3)
b3.pack(side=LEFT , padx = 13,pady=20)

b4= Button(frame, fg="red", text="Print4", command = hello4)
b4.pack(side=LEFT, padx = 13,pady=20)
root.mainloop()
# if use () this after the hello1 command then it will automatically print the buttons values
# otherwise it will print after clicking the button