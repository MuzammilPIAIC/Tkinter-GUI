import tkinter as tk
import keyboard
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
from csv import writer
import csv
import datetime
import os

if not os.path.exists('History.csv'):
    print("File created")
    df11=pd.DataFrame(columns=["Date","Time"])
    df11.to_csv("History.csv", index=False)

if not os.path.exists('User_data.csv'):
    print("File created")
    df22=pd.DataFrame(columns=["Names","Fingerprints"])
    df22.to_csv("User_data.csv", index=False)
    
    

root=tk.Tk()
root.geometry("650x360")
root.resizable(width=0, height=0)
root.title('Security Management Software')

frame=tk.Frame(root,bg='lightblue')
frame.place(relheight=1,relwidth=1)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def Login_page():
    for item in frame.place_slaves():
        item.place_forget()
    label=tk.Label(frame,text='Place your finger on fingerprint scanner to login',font=("Helvatical bold", 20),bg='lightblue')
    label.place(relx=0.5,rely=0.3,anchor="center")
    login_check= tk.Button(frame, text="Login", width=15, height=2, command=welcome)
    login_check.place(relx=0.5,rely=0.6, anchor="center")
    
def show_history():
    for item in frame.place_slaves():
        item.place_forget()
    frame2=tk.Frame(frame,bg='lightblue')
    frame2.place(relheight=.6,relwidth=.6,relx=0.2,rely=0.2)
    
    label=tk.Label(frame,text='Login History of '+str(user_name),font=("Helvatical bold", 15),bg='lightblue')
    label.place(relx=0.5,rely=0.1,anchor="center")
        
    scrollbary = Scrollbar(frame2, orient=VERTICAL)
    tree = ttk.Treeview(frame2, columns=("Date", "Time"), height=200, selectmode="extended",
                    yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Time', text="Time", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.pack()
    with open("History/"+str(user_name)+".csv") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            date = row['Date']
            time = row['Time']
            tree.insert("", 0, values=(date, time))
    
    back_buttom= tk.Button(frame, text="Back", width=15, height=2, command=welcome_for_back_button)
    back_buttom.place(relx=0.5,rely=0.9, anchor="center")
    
    
def show_user_data():
    for item in frame.place_slaves():
        item.place_forget()
    frame2=tk.Frame(frame,bg='lightblue')
    frame2.place(relheight=.6,relwidth=.6,relx=0.2,rely=0.2)
    
    label=tk.Label(frame,text='Users Data',font=("Helvatical bold", 15),bg='lightblue')
    label.place(relx=0.5,rely=0.1,anchor="center")
        
    scrollbary = Scrollbar(frame2, orient=VERTICAL)
    global tree
    tree = ttk.Treeview(frame2, columns=("Names", "Fingerprints"), height=200, selectmode="extended",
                    yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree.heading('Names', text="Names", anchor=W)
    tree.heading('Fingerprints', text="Fingerprints", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.pack()
    
    file = "User_data.csv"
    f = open(file, 'r')
    global csvreader_list
    csvreader = csv.reader(f)
    csvreader_list = list(csvreader)
    f.close()
    print(csvreader_list)
    for (i, n) in csvreader_list:
        tree.insert('', 'end', values=(i,n))
    
    back_buttom= tk.Button(frame, text="Back", width=15, height=2, command=Home)
    back_buttom.place(relx=0.3,rely=0.85)
    
    delete_buttom= tk.Button(frame, text="Delete", width=15, height=2, command=delete)
    delete_buttom.place(relx=0.6,rely=0.85)


def delete():
    
    # Get selected item to Delete
    selected_item = tree.selection()[0]
    values = tuple(tree.item(selected_item)['values'])
    new_l = []
    for i in values:
        k = str(i)
        new_l.append(k)
    index = csvreader_list.index(new_l)
    df = pd.read_csv("User_data.csv")
    rows = df.index[index-1]
    df.drop(rows, inplace=True)
    df.to_csv("User_data.csv", index=False)
    tree.delete(selected_item)

 
def welcome_for_back_button():
    
    for item in frame.place_slaves():
        item.place_forget()
    
    label=tk.Label(frame,text='Welcome '+str(user_name),font=("Helvatical bold", 15),bg='lightblue')
    label.place(relx=0.5,rely=0.15, anchor="center")
    logout= tk.Button(frame, text="Logout", width=15, height=2, command=Home)
    logout.place(relx=0.3,rely=0.5)
    
    view_history= tk.Button(frame, text="View History", width=15, height=2, command=show_history)
    view_history.place(relx=0.6,rely=0.5)



def welcome():
    data = pd.read_csv("User_data.csv")
    fingerprints = data["Fingerprints"].values
    user = False
    check = 3
    index = -1
    for i in fingerprints:
        index += 1
        if i == check:
            user = True
            break
    global user_name
    user_name = data.loc[index, 'Names']
    if user == True:
        if not os.path.exists("History/"+str(user_name)+".csv"):
            print(user_name,"history file created")
            df111=pd.DataFrame(columns=["Date","Time"])
            df111.to_csv("History/"+str(user_name)+".csv", index=False)
        x = datetime.datetime.now()
        current_date = x.strftime("%d-%m-%Y")
        current_time = x.strftime("%I:%M %p")
        row_contents = [current_date,current_time]
        append_list_as_row("History/"+str(user_name)+".csv", row_contents)
        for item in frame.place_slaves():
            item.place_forget()
        
        label=tk.Label(frame,text='Welcome '+str(user_name),font=("Helvatical bold", 15),bg='lightblue')
        label.place(relx=0.5,rely=0.15, anchor="center")
        logout= tk.Button(frame, text="Logout", width=15, height=2, command=Home)
        logout.place(relx=0.3,rely=0.5)
        
        view_history= tk.Button(frame, text="View History", width=15, height=2, command=show_history)
        view_history.place(relx=0.6,rely=0.5)
        
            
    else:
        for item in frame.place_slaves():
            item.place_forget()
        label1=tk.Label(frame,text='Fignerprint not match! you need to Add yourself first',font=("Helvatical bold", 15),bg='lightblue')
        label1.place(relx=0.5,rely=0.2, anchor="center")
        back_to_home= tk.Button(frame, text="Back to Home", width=15, height=2, command=Home)
        back_to_home.place(relx=0.5,rely=0.5, anchor="center")
    
def add_user_button():
    user_name = mystring.get()
    row_contents = [user_name,4]
    append_list_as_row('User_data.csv', row_contents)
    welcome()
    
    
    

def add_user_page():
    for item in frame.place_slaves():
        item.place_forget()
    global mystring
    mystring = StringVar()
    text1=tk.Label(frame,text='Enter Your Name',font=("Helvatical bold", 15),bg='lightblue')
    text1.place(relx=0.5,rely=0.35, anchor="center")
    
    entry_feild = tk.Entry(frame, textvariable = mystring, font=("Helvatical bold", 20)) #entry textbox  
    entry_feild.place(relx=0.5,rely=0.5, anchor="center", width=250,height=40)
    
    user_submit= tk.Button(frame, text="Submit", width=15, height=2, command=add_user_button)
    user_submit.place(relx=0.5,rely=0.7, anchor="center")
    
def Add_Modify_users():
    for item in frame.place_slaves():
        item.place_forget()
    heading=tk.Label(frame,text='Add and Modify Users',font=("Helvatical bold", 15),bg='lightblue')
    heading.place(relx=0.5,rely=0.1, anchor="center")
    
    add_user= tk.Button(frame, text="Add new user", width=15, height=2, command=add_user_page)
    add_user.place(relx=0.6,rely=0.5)

    modify_user= tk.Button(frame, text="Modify Users", width=15, height=2, command=show_user_data)
    modify_user.place(relx=0.3,rely=0.5)

    changeOnHover(add_user, "lightgreen", "white")
    changeOnHover(modify_user, "lightgreen", "white")
    

def Home():
    for item in frame.place_slaves():
        item.place_forget()
    heading=tk.Label(frame,text='Welcome to the security management tool',font=("Helvatical bold", 15),bg='lightblue')
    heading.place(relx=0.5,rely=0.1, anchor="center")


    login_button= tk.Button(frame, text="Login", width=15, height=2, command=Login_page)
    login_button.place(relx=0.6,rely=0.5)

    add_modify_button= tk.Button(frame, text="Add/Modify Users", width=15, height=2, command=Add_Modify_users)
    add_modify_button.place(relx=0.3,rely=0.5)

    changeOnHover(login_button, "lightgreen", "white")
    changeOnHover(add_modify_button, "lightgreen", "white")
  


#mystring = StringVar()

####define the function that the signup button will do
#def add_user_button():
##    print(mystring.get())


    

heading=tk.Label(frame,text='Welcome to the security management tool',font=("Helvatical bold", 15),bg='lightblue')
heading.place(relx=0.5,rely=0.1, anchor="center")

#bt=tk.Button(root,text='page1',command=page1)
#bt.grid(column=5,row=5)

login_button= tk.Button(frame, text="Login", width=15, height=2, command=Login_page)
login_button.place(relx=0.6,rely=0.5)

add_modify_button= tk.Button(frame, text="Add/Modify Users", width=15, height=2, command=Add_Modify_users)
add_modify_button.place(relx=0.3,rely=0.5)

changeOnHover(login_button, "lightgreen", "white")
changeOnHover(add_modify_button, "lightgreen", "white")




root.mainloop()