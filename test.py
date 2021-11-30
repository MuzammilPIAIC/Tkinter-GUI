# from tkinter import *
# import tkinter as tk
# from tkinter import ttk
# import csv
 
 
# app = tk.Tk()
# app.title('Test')
# app.geometry('800x500')
# x=StringVar()
# y=StringVar()
# z=StringVar()
 
# file = "User_data.csv"
 
# f = open(file, 'r')
# csvreader = csv.reader(f)
# csvreader_list = list(csvreader)
 
# # print(csvreader_list)


# label1=tk.Label(app,text="By Date:",font="Helvetica 12",fg="white",bg="#460B05")
# label1.place(x=10,y=10)
# search1=tk.Entry(app,textvariable=x)
# search1.place(x=80,y=10,height=23,width=200)

# label2=tk.Label(app,text="By Time:",font="Helvetica 12",fg="white",bg="#460B05")
# label2.place(x=300,y=10)
# search2=tk.Entry(app,textvariable=y)
# search2.place(x=370,y=10,height=23,width=200)





 
 
# tv = ttk.Treeview(app, columns=('col_1', 'col_2'), show='headings')
# tv.column('col_1', minwidth=0, width=400)
# tv.column('col_2', minwidth=0, width=100)

 
# tv.heading('col_1', text='Date')
# tv.heading('col_2', text='Time')

 
# tv.place(x=100,y=200)
 
# def search():
    # k = -1
    # tv.delete(*tv.get_children())
    # word=x.get().title()
    # word1=y.get()
    # if x.get():
        # for (i, n) in csvreader_list:
            # k = k + 1
            # if word in i:
                # tv.insert('', 'end', values=(i,n))
    # elif y.get():
        # for (i, n) in csvreader_list:
            # if word1 in n:
                # tv.insert('', 'end', values=(i,n))
    # else:
        # for (i,n) in csvreader_list:
            # tv.insert('', 'end', values=(i,n))
    # search1.delete(0, 'end')
    # search2.delete(0, 'end')
    # print(k)

        
# print(csvreader_list)
# searchbutton=tk.Button(app,text="Search",fg="black",command=search,anchor="center",justify=CENTER)
# searchbutton.place(x=1,y=50,width=898)
# app.mainloop()


# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an instance of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Company")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('1', 'Honda'))
tree.insert('', 'end', text="2", values=('2', 'Hyundai'))
tree.insert('', 'end', text="3", values=('3', 'Tesla'))
tree.insert('', 'end', text="4", values=('4', 'Wolkswagon'))
tree.insert('', 'end', text="5", values=('5', 'Tata Motors'))
tree.insert('', 'end', text="6", values=('muzammil', '2'))

tree.pack()

def edit():
   # Get selected item to Edit
   selected_item = tree.selection()[0]
   tree.item(selected_item, text="blub", values=("foo", "bar"))

def delete():
    
    # Get selected item to Delete
    selected_item = tree.selection()[0]
    values = tuple(tree.item(selected_item)['values'])
    new_l = []
    for i in values:
        k = str(i)
        new_l.append(k)
    print("values ",new_l)
    l = [['ashan','1'],['muzammil','2'],['osama','3']]
    print(l)
    index = l.index(new_l)
    print("index ",index)
    l.remove(new_l)
    print(l)
    tree.delete(selected_item)

# Add Buttons to Edit and Delete the Treeview items
edit_btn = ttk.Button(win, text="Edit", command=edit)
edit_btn.pack()
del_btn = ttk.Button(win, text="Delete", command=delete)
del_btn.pack()

win.mainloop()