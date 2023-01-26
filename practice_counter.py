# Using counter
import tkinter as tk

counter = 0


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


root = tk.Tk()
root.geometry("300x200")
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Submit', width=25, command=root.destroy)
button.pack()
root.mainloop()