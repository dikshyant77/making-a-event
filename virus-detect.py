from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("200x200")

def msg():
    messagebox.showwarning("alert!","stop virus found")
button=Button(window,text="scan for virus", command=msg)
button.place(x=40, y=20)

def msg1():
    messagebox.showerror("alert!","stop virus found")
button1=Button(window,text="show error", command=msg1)
button1.place(x=40, y=60)

def msg2():
    messagebox.askquestion("question box","Do you want to continue?")
button3=Button(window,text="ask question", command=msg2)
button3.place(x=40, y=100)

def msg4():
    messagebox.showerror("conform ","Do you want to preciate")
button4=Button(window,text="click me", command=msg4)
button4.place(x=40, y=140)

window.mainloop()
