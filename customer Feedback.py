from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
frame_header = ttk.Frame(root)
frame_header.pack()
logo = PhotoImage(file='truck.jpg').subsample(2, 2)
logolabel = ttk.Label(frame_header, text='logo', image=logo)
logolabel.grid(row=0, column=0, rowspan=2)
headerlabel = ttk.Label(frame_header, text='CUSTOMER FEEDBACK', foreground='orange',
                        font=('Arial black', 24))
headerlabel.grid(row=0, column=1)
messagelabel = ttk.Label(frame_header,
                         text='PLEASE TELL US WHAT YOU THINK?',
                         foreground='purple', font=('Arial black', 10))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()

myvar = StringVar()
var = StringVar()

namelabel = ttk.Label(frame_content, text='           Name' )
namelabel.grid(row=0, column=3, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=3)

emaillabel = ttk.Label(frame_content, text='  Email' )
emaillabel.grid(row=0, column=2, sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
entry_email.grid(row=1, column=2)


var1 = StringVar()
l1 = Checkbutton(root, text='Exellent', variable=var1, font=('Arial',10))
l1.deselect()
l1.place(x=77, y=205)

var2 = IntVar()
l2 = Checkbutton(root, text='V.good', variable=var2, font=('Arial',10))
l2.place(x=77, y=225)

var3 = IntVar()
l3 = Checkbutton(root, text='Neutral', variable=var3, font=('Arial', 10))
l3.place(x=77, y=245)

var4 = IntVar()
l4 = Checkbutton(root, text='Bad',variable=var4, font=('Arial', 10))
l4.place(x=77, y=265)

commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial black', 10))
commentlabel.grid (row= 4, column=3, sticky='sw')
textcomment = Text(frame_content, width=50, height=3)
textcomment.grid(row=5, column=3, columnspan=2)


textcomment.config(wrap ='word')

def clear():
    global entry_name
    global entry_email
    global Checkbutton
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    l1.deselect
    l2.deselect
    l3.deselect
    l4.deselect
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global Checkbutton
    global textcomment
    print('Name:{}'.format(myvar.get()))
    print('Email:{}'.format(var.get()))
    print('check:{}'.format(var.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    l1.deselect
    l2.deselect
    l3.deselect
    l4.deselect
    textcomment.delete(1.0, END)


submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=10, column=3, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=10, column=4, sticky='w')


mainloop()

