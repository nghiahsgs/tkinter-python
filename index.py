from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import messagebox


window = Tk()
window.title("Test form nghiahsgs")
# window.geometry("500x500")

# Thêm label
lbl = tkinter.Label(window, text="Hello ban",fg="red",font=('Arial',50))
lbl.grid(column=0,row=0)

# Thêm textbox
txt = Entry(window,width=20)
txt.grid(column=0,row=1)

# Thêm combobox
txt = Entry(window,width=20)
txt.grid(column=0,row=1)

# Thêm button
def handleClick():
    lbl.configure(text="Xin chao %s"%(txt.get()))
btnHello = Button(window,text="say hello",command=handleClick)
btnHello.grid(column=0,row=2)


# them combo
combo = Combobox(window)
combo['values'] = ('ban 1','ban 2','ban 3')
combo.current(1)
combo.grid(column=0,row=3)

# Thêm button
def handleClick2():
    # lbl.configure(text="hello %s"%(combo.get()))
    messagebox.showinfo(title="hi",message="hello %s"%(combo.get()))
    
btnHello2 = Button(window,text="say hello 2",command=handleClick2)
btnHello2.grid(column=0,row=4)


window.mainloop()

