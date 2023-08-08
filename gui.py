#getting started with tkinter
from tkinter import *
top = Tk()

#top window title and dimension
top.title("Welcome To Bizmarrow")
top.geometry('500x500')

#Adding a menu Bar
menu = Menu(top)
item = Menu(menu)
item.add_command(label = 'New')
menu.add_cascade(label='File', menu=item)
top.config(menu=menu)

#Adding a label
label_0 = Label(top, text="Are you a python programmer?")
label_0.grid()

#Adding Entry Field
txt = Entry(top, width=10)
txt.grid(column=1, row=0)


#function to display text when
#button is clicked
def clicked():
    label_0.configure(text= "I just got clicked")
    res = "You wrote " + txt.get()
    label_0.configure(text = res)

#button widget with blue color text
#inside
button = Button(top, text= "Click Me", fg="blue", command=clicked)
button.grid(column=2, row=0)




top.mainloop()