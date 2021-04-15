from tkinter import *

root = Tk()
root.title("Python Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def btn_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def btn_clear():
    e.delete(0, END)

def btn_add():
    num_one = e.get()
    global num_1
    global math
    math = "addition"
    num_1 = int(num_one)
    e.delete(0, END)

def btn_subtract():
    num_one = e.get()
    global num_1
    global math
    math = "subtraction"
    num_1 = int(num_one)
    e.delete(0, END)

def btn_multiply():
    num_one = e.get()
    global num_1
    global math
    math = "multiplication"
    num_1 = int(num_one)
    e.delete(0, END)

def btn_divide():
    num_one = e.get()
    global num_1
    global math
    math = "division"
    num_1 = int(num_one)
    e.delete(0, END)

def btn_equal():
    num_two = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, num_1 + int(num_two))
    if math == "subtraction":
        e.insert(0, num_1 - int(num_two))
    if math == "multiplication":
        e.insert(0, num_1 * int(num_two))
    if math == "division":
        e.insert(0, num_1 / int(num_two))

def btn_decimal():
    # Code here
    return


# Define buttons on calculator
btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))

btn_add = Button(root, text="+", padx=40, pady=20, command=btn_add)
btn_subtract = Button(root, text="-", padx=40, pady=20, command=btn_subtract)
btn_multiply = Button(root, text="*", padx=40, pady=20, command=btn_multiply)
btn_divide = Button(root, text="/", padx=40, pady=20, command=btn_divide)
btn_decimal = Button(root, text=".", padx=40, pady=20, command=btn_click("."))
btn_equal = Button(root, text="=", padx=40, pady=20, command=btn_equal)
btn_clear = Button(root, text="C", padx=40, pady=20, command=btn_clear)


# Display buttons on GUI
btn1.grid(row=5, column=0)
btn2.grid(row=5, column=1)
btn3.grid(row=5, column=2)

btn4.grid(row=4, column=0)
btn5.grid(row=4, column=1)
btn6.grid(row=4, column=2)

btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)

btn0.grid(row=6, column=1)

btn_add.grid(row=5, column=3)
btn_subtract.grid(row=4, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=2, column=3)

btn_decimal.grid(row=6, column=2)
btn_equal.grid(row=6, column=3)
btn_clear.grid(row=1, column=3)


root.mainloop()