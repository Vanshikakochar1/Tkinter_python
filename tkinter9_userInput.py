from tkinter import *

root = Tk()
root.geometry("800x567")
root.title("Travel Form")
def getvals():
    print("Submitting form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get() ,paymentmodevalue.get(), agevalue.get(), foodservicevalue.get()}")

    with open ("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get() ,paymentmodevalue.get(), agevalue.get(), foodservicevalue.get()}\n")

# Use for making grid layout
# how to use checkbox and take user
# heading
Label(root, text ="Welcome to Travel India ", font="comicsans 13 bold", pady=15).grid()
# text for our form
name = Label(root, text="Name")
phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
emergency= Label(root, text="Emergency Contact")
paymentmode= Label(root, text="Payment Mode")
age= Label(root, text="Age")

# pack all the text with help of grid
name.grid(row=1, column=2, pady=13)
phone.grid(row=2, column=2, pady=13)
gender.grid(row=3, column=2, pady=13)
emergency.grid(row=4, column=2, pady=13)
paymentmode.grid(row=5, column=2, pady=13)
age.grid(row=6, column=2, pady=13)

# make tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
agevalue = StringVar()
foodservicevalue = IntVar(
)

# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)
ageentry = Entry(root, textvariable=agevalue)

# packing the entries
nameentry.grid(row=1, column =3)
phoneentry.grid(row=2, column =3)
genderentry.grid(row=3, column =3)
emergencyentry.grid(row=4, column =3)
paymentmodeentry.grid(row=5, column =3)
ageentry.grid(row=6, column =3)

#checkbox - use checkbutton
foodservice = Checkbutton(text="Want to prebook your meal?", variable=foodservicevalue)
foodservice.grid(row=7, column=3, pady=13)

# button and packing and assigning it a command
Button(text="Submit to travels india", command=getvals).grid(row =8, column=3, pady=13)

root.mainloop()