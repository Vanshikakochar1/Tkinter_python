# from tkinter import *
# root = Tk()
# root.geometry("500x250")
# root.title("Submit Form")
#
# def sub():
#     print("Values Submitted")
#
# def cancel():
#     print("Values Cancelled")
#
# Label(root, text ="Kindly click the submit button!!", font="comicsans 13 bold", pady=15).grid(padx = 100)
# username = Label(root, text="username")
# password= Label(root, text="password")

# username.grid(pady = 10)
# password.grid(row=1 , pady=10)
#
# uservalue = StringVar()
# passwordvalue =StringVar()

# userentry = Entry(root, textvariable=uservalue).grid(row=0, column=1)
# passwordentry = Entry(root, textvariable=passwordvalue).grid(row=1, column=1)

# submit button
# submit = Button(root, text="Submit", command = sub).grid(row=1, column=0, pady =10)
# cancel = Button(root, text="Cancel", command = cancel).grid(row=1, column=1, pady=10)
# root.mainloop()


import tkinter as tk
root = tk.Tk()
root.geometry("200x150")
root.title("Submit form")
s = tk.Label(root, text="Submit the form", font="comicsans 13 bold")
s.pack(pady =20)
frame = tk.Frame(root)
frame.pack()
def submit_response():
    print("Response Submitted!")
def cancel():
    print("Response not recieved")
button = tk.Button(frame,
                   text="SUBMIT",
                   fg="green",
                   command=submit_response)
button.pack(side=tk.LEFT, padx=10, pady=10)
button2= tk.Button(frame,
                   text="CANCEL",
                   command=cancel)
button2.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()