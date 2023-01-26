from tkinter import *
root = Tk()
root.geometry("565x345")
root.title("Widgets and Grid")

def getvals():
    print("The value of user is:", uservalue.get())
    print("The value of password is:", passvalue.get())
    # gloabl variables not a good practice
# excel in row 0 and column 0 start
user = Label(root, text = "Username")
password = Label(root, text = "Password")
# pack krne k liye .grid
user.grid()
password.grid(row =1) # column autoamtically 0

# Entry widget = values input, <input> <text area>
# make 2 strings
'''Variable classes in tkinter
BooleanVar, DoubleVar, IntVar, StringVar'''
uservalue= StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column =1)
passentry.grid(row =1 , column=1)

Button (text="submit", command = getvals).grid()

root.mainloop()