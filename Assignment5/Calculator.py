from tkinter import *
import tkinter as tk

val = ""


def click(number):
    global val
    val = val + str(number)
    data.set(val)


def calculate():
    global val
    val = str(eval(val))
    data.set(val)


def clear():
    global val
    val = ""
    data.set(val)


root = tk.Tk()
root.title("🔢 Calculator")
root.configure(background="white")
root.iconbitmap('icon.ico')
root.geometry("300x500")
root.resizable(False, False)


data = tk.StringVar()
screen = Label(root, text="Label", anchor=SE, font=("Verdana", 20), textvariable=data, background="#F5F5F5",
               fg="#000000")
screen.pack(expand=True, fill="both")

f = Frame(root)

b = Button(f, text="Clear", bg="#EEE9BF", font=("Verdana", 22), width=10, border=0, command=clear)
b.pack(side=LEFT, expand=True, fill="both")


b = Button(f, text="/", bg="#FFFFFF", fg="GREEN", font=("Verdana", 22), width=2, border=0, command=lambda: click("/"))
b.pack(side=LEFT, expand=True, fill="both")

f.pack(expand=True, fill="both", padx=5, pady=5)

f = Frame(root)

b = Button(f, text="7", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(7))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="8", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(8))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="9", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(9))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="*", bg="#FFFFFF", fg="GREEN", font=("Verdana", 22), width=2, border=0, command=lambda: click('*'))
b.pack(side=LEFT, expand=True, fill="both")

f.pack(expand=True, fill="both", padx=5, pady=5)

f = Frame(root)

b = Button(f, text="4", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(4))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="5", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(5))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="6", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(6))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="-", bg="#FFFFFF", fg="GREEN", font=("Verdana", 22), width=2, border=0, command=lambda: click('-'))
b.pack(side=LEFT, expand=True, fill="both")

f.pack(expand=True, fill="both", padx=5, pady=5)

f = Frame(root)

b = Button(f, text="1", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(1))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="2", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(2))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="3", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(3))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="+", bg="#FFFFFF", fg="GREEN", font=("Verdana", 22), width=2, border=0, command=lambda: click('+'))
b.pack(side=LEFT, expand=True, fill="both")

f.pack(expand=True, fill="both", padx=5, pady=5)

f = Frame(root)

b = Button(f, text="%", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click('%'))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="0", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click(0))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text=".", bg="#FFFFFF", font=("Verdana", 22), width=2, border=0, command=lambda: click('.'))
b.pack(side=LEFT, expand=True, fill="both")

b = Button(f, text="=", bg="#54AEFF", font=("Verdana", 22), width=2, border=0, command=calculate)
b.pack(side=LEFT, expand=True, fill="both")

f.pack(expand=True, fill="both", padx=5, pady=5)

root.mainloop()