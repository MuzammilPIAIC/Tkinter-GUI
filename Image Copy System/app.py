import tkinter as tk

from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import mysql.connector
from tkinter import messagebox  
import os


root=tk.Tk()
root.geometry("800x600")
root.resizable(width=0, height=0)
root.title('Welcome')

frame=tk.Frame(root,bg='lightblue')
frame.place(relheight=1,relwidth=1)

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def submit_button():
    source_path = mystring.get()
    target_path = mystring_2.get()

    if not source_path or not target_path:
        messagebox.showerror('Path Error', "Error: Please Check both Directory's path!")
    else:
        main_page()
        

def main_page():
    source_path = mystring.get()
    target_path = mystring_2.get()

    for item in frame.place_slaves():
        item.place_forget()
    list_1  = os.listdir(str(source_path))

    number = 0
    
    source_path=source_path.replace('\\','/')
    image = tk.PhotoImage(file=str(source_path)+"/"+str(list_1[number]))
    label = tk.Label(image=image)
    label.pack()


def Home():
    for item in frame.place_slaves():
        item.place_forget()
    heading=tk.Label(frame,text='Enter source directory path',font=("Helvatical bold", 15),bg='lightblue')
    heading.place(relx=0.5,rely=0.1, anchor="center")

    global mystring, mystring_2
    mystring = StringVar()
    mystring_2 = StringVar()
    # text1=tk.Label(frame,text='Enter Your Database Name',font=("Helvatical bold", 15),bg='lightblue')
    # text1.place(relx=0.5,rely=0.35, anchor="center")

    entry_feild = tk.Entry(frame, textvariable = mystring, font=("Helvatical bold", 20)) #entry textbox  
    entry_feild.place(relx=0.52,rely=0.2, anchor="center", width=650,height=40)

    heading1=tk.Label(frame,text='Enter save directory path',font=("Helvatical bold", 15),bg='lightblue')
    heading1.place(relx=0.5,rely=0.4, anchor="center")


    entry_feild_2 = tk.Entry(frame, textvariable = mystring_2, font=("Helvatical bold", 20)) #entry textbox  
    entry_feild_2.place(relx=0.52,rely=0.5, anchor="center", width=650,height=40)

    #bt=tk.Button(root,text='page1',command=page1)
    #bt.grid(column=5,row=5)

    submit_button= tk.Button(frame, text="Submit", width=15, height=2, command=submit_button) #command=add_new_db
    submit_button.place(relx=0.5,rely=0.7, anchor="center")


# heading=tk.Label(frame,text='Welcome to the Database management tool',font=("Helvatical bold", 15),bg='lightblue')
# heading.place(relx=0.5,rely=0.1, anchor="center")

heading=tk.Label(frame,text='Enter source directory path',font=("Helvatical bold", 15),bg='lightblue')
heading.place(relx=0.5,rely=0.1, anchor="center")

global mystring, mystring_2
mystring = StringVar()
mystring_2 = StringVar()
# text1=tk.Label(frame,text='Enter Your Database Name',font=("Helvatical bold", 15),bg='lightblue')
# text1.place(relx=0.5,rely=0.35, anchor="center")

entry_feild = tk.Entry(frame, textvariable = mystring, font=("Helvatical bold", 20)) #entry textbox  
entry_feild.place(relx=0.52,rely=0.2, anchor="center", width=650,height=40)

heading1=tk.Label(frame,text='Enter save directory path',font=("Helvatical bold", 15),bg='lightblue')
heading1.place(relx=0.5,rely=0.4, anchor="center")


entry_feild_2 = tk.Entry(frame, textvariable = mystring_2, font=("Helvatical bold", 20)) #entry textbox  
entry_feild_2.place(relx=0.52,rely=0.5, anchor="center", width=650,height=40)

#bt=tk.Button(root,text='page1',command=page1)
#bt.grid(column=5,row=5)

submit_button= tk.Button(frame, text="Submit", width=15, height=2, command=submit_button) #command=add_new_db
submit_button.place(relx=0.5,rely=0.7, anchor="center")


# add_modify_button= tk.Button(frame, text="Existed Database", width=15, height=2)
# add_modify_button.place(relx=0.3,rely=0.5)

changeOnHover(submit_button, "lightgreen", "white")

# changeOnHover(add_modify_button, "lightgreen", "white")



root.mainloop()