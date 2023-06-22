import tkinter as tk
from tkinter import END

root = tk.Tk()

root.title("Calculatrice")
root.resizable(width=False, height=False)

num_view = tk.Entry(root, width=35, borderwidth=5)
num_view.grid(row=0, column=0, columnspan=3, padx=5, pady=10)


def choice_number(number):
    current = num_view.get()
    num_view.delete(0, END)
    num_view.insert(1, str(current) + str(number))

def clear_number():
    num_view.delete(0, END)

def add_button():
    first_number = num_view.get()
    global f_num
    global signe
    f_num = int(first_number)
    num_view.delete(0, END)
    signe = "addition"

def sub_button():
    first_number = num_view.get()
    global f_num
    global signe
    f_num = int(first_number)
    num_view.delete(0, END)
    signe = "soustraction"


def mult_button():
    first_number = num_view.get()
    global f_num
    global signe
    f_num = int(first_number)
    num_view.delete(0, END)
    signe = "multiplication"


def devide_button():
    first_number = num_view.get()
    global f_num
    global signe
    f_num = int(first_number)
    num_view.delete(0, END)
    signe = "division"

def equal_button():
    second_number = num_view.get()
    num_view.delete(0,END)
    match signe :
        case "addition":
            num_view.insert(0,f_num + int(second_number))
        case "soustraction":
            num_view.insert(0, f_num - int(second_number))
        case "multiplication":
            num_view.insert(0, f_num * int(second_number))
        case "division":
            num_view.insert(0, f_num / int(second_number))


num_0_button = tk.Button(root, text="0", width=9, height=5,command=lambda : choice_number(0))
num_1_button = tk.Button(root, text="1", width=9, height=5,command=lambda : choice_number(1))
num_2_button = tk.Button(root, text="2", width=9, height=5,command=lambda : choice_number(2))
num_3_button = tk.Button(root, text="3", width=9, height=5,command=lambda : choice_number(3))
num_4_button = tk.Button(root, text="4", width=9, height=5,command=lambda : choice_number(4))
num_5_button = tk.Button(root, text="5", width=9, height=5,command=lambda : choice_number(5))
num_6_button = tk.Button(root, text="6", width=9, height=5,command=lambda : choice_number(6))
num_7_button = tk.Button(root, text="7", width=9, height=5,command=lambda : choice_number(7))
num_8_button = tk.Button(root, text="8", width=9, height=5,command=lambda : choice_number(8))
num_9_button = tk.Button(root, text="9", width=9, height=5,command=lambda : choice_number(9))

button_add = tk.Button(root, text="+", width=9, height=5,command= lambda : add_button())
button_sub = tk.Button(root, text="-", width=9, height=5,command= lambda : sub_button())
button_mult = tk.Button(root, text="*", width=9, height=5,command= lambda : mult_button())
button_divide = tk.Button(root, text="/", width=9, height=5,command= lambda : devide_button())
button_equal = tk.Button(root, text="=", width=9, height=5,command= lambda : equal_button())
button_reset = tk.Button(root, text="C", width=9, height=5,command= lambda : clear_number())

num_0_button.grid(row=4, column=0)
num_1_button.grid(row=3, column=0)
num_2_button.grid(row=3, column=1)
num_3_button.grid(row=3, column=2)
num_4_button.grid(row=2, column=0)
num_5_button.grid(row=2, column=1)
num_6_button.grid(row=2, column=2)
num_7_button.grid(row=1, column=0)
num_8_button.grid(row=1, column=1)
num_9_button.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_reset.grid(row=4, column=1)




root.mainloop()
