#importing all tkinter module
from tkinter import *

root = Tk()

root.geometry('500x500')

root.title("Registeration Form")

label_0 = Label(root, text="Registeration Form", width=20, font=("bold", 20))
label_0.place(x=90, y=60)

#creating the label widget and the entry widget
label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_0 = Entry(root)
entry_0.place(x = 240, y= 130);

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_0 = Entry(root)
entry_0.place(x = 240, y= 180)

#creating the label and the radio button
label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

var = IntVar()
radio_0 = Radiobutton(root, text="Male", variable=var, value=1).place(x=235, y=230)
radio_1 = Radiobutton(root, text="Female", variable=var, value=2).place(x=290, y=230)

#label widget and dropdown widget
label_4 = Label(root, text="Countries", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

countryList = ["Nigeria", "Ghana", "South Africa", "Canada"]
c = StringVar()
countries = OptionMenu(root, c, *countryList)
countries.config(width=15)
c.set("Choose A Country")
countries.place(x=240, y=280)

#label and checkbutton widget
label_4 = Label(root, text="Languanges", width=20, font=("bold", 10))
label_4.place(x=75, y=330)

var1 = IntVar()
Checkbutton(root, text="English", variable=var1).place(x=230, y=330)

var2 = IntVar()
Checkbutton(root, text="English", variable=var2).place(x=290, y=330)

#sumit widget
Button(root, text="submit", width=20, fg="black", bg="white").place(x=180, y=380)









root.mainloop()