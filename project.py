#import tkinter
from tkinter import *
import tkinter.messagebox

#create to-do-list application window
top = Tk()
top.title("To do list")
top.geometry('500x500')

#frame widget to hold the listbox and scroll bar
frame_task = Frame(top)
frame_task.pack()


#To hold the list_box
list_box = Listbox(frame_task, bg="blue", fg="white", height=12, width=50, font="Helvetica")
list_box.pack(side=tkinter.LEFT)

#scrolldown in case the total list exceed d size of the given window
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
list_box.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=list_box.yview)

#entertask
def entertask():
    button.configure()

#The button widget
button = Button(top, text="Add Task", width=50, command=entertask)
button.pack(pady=3)

top.mainloop()