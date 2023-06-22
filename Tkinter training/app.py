from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

e.insert(0,"Entrer")



myLabel1 = Label(root, text="Hello World")  # .grid(row=0, column=0)

#myLabel1.grid(row=0, column=0)
myLabel1.pack()


def myClick():
    myLabel2 = Label(root, text=e.get())  # .grid(row=1, column=1)
    myLabel2.pack()


myButton = Button(root, text="Ajouter", padx=50, pady=50, command=myClick)  # state=DISABLED pour désactiver

#myButton.grid(row=3, column=0)
myButton.pack()

root.mainloop()
