'''
Project Title: To-Do List Application

Project Description: Create a simple command-line to-do list application in Python
    that allows users to manage their tasks. This project will help you practice
    working with data structures, user input, and basic file handling.

Key Features you can include:
    • Add tasks: Users should be able to add tasks to their to-do list with a title and a description.
    • List tasks: Users can view their existing tasks with details like title, description, and a unique task ID.
    • Mark tasks as complete: Users can mark tasks as complete or uncompleted.
    • Delete tasks: Users can remove tasks from their to-do list.
    • Save tasks: Implement file handling to save tasks to a text file, so users can retrieve them even after closing the program.
    • Load tasks: Allow users to load their saved tasks from the text file when they start the program.
    • User-friendly interface: Create a simple and intuitive command-line interface that guides users through the available actions.
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
import random

#REFERENCES OF SQLITE3
#https://docs.python.org/3/library/sqlite3.html

#REFERENCES FOR FONTS
#https://www.tutorialspoint.com/python/tk_fonts.htm
# from tkinter import font

FONT1 = ("Sitka Heading",13)
FONT2 = ("Segoe UI Symbol",13)
FONT3 = ("Segoe UI Symbol",10)
BUTTONFONT = ("Sitka Heading",11)
BG = "#efb2ea"
TEXTCOLOR = "black"

task_title_di = {}
task_desc_di = {}
taskID = []
liBox_elem = []

def addTask():
    task_title = txt1.get()
    task_desc = txt2.get()

    if len(task_title)==0:
        messagebox.showinfo('Empty Entry', 'Enter task title')
    else:
        flag = True
        while (flag):
            ID = random.randint(0,9999)
            if ID not in taskID:
                flag=False
        cur.execute('insert into tasks values (?,?,?)', (ID,task_title,task_desc))

        task_title_di[ID] = task_title
        task_desc_di[ID] = task_desc
        taskID.append(ID)

        txt1.delete(0,'end')
        txt2.delete(0,'end')
        
        listUpdate()

def listUpdate():
    libox.delete(0,'end')
    for i in taskID:
        item1 = f"Task ID: {i}"
        item2 = f"Task Title: {task_title_di[i]}"
        item3 = f"Task Description: {task_desc_di[i]} "
        final = " || ".join([item1,item2,item3])
        libox.insert('end', final)
        liBox_elem.append(final)

def deleteOne():
    try:
        toDelete = libox.get(libox.curselection())
        if toDelete in liBox_elem:
            liBox_elem.remove(toDelete)
            listUpdate()
            # ttitle = toDelete
            # for t in
            # toDeleteID
            # cur.execute("Delete from tasks where tID = ?",(toDeleteID,))
    except:
        messagebox.showinfo("Cannot Delete","No task selected")

con = sql.connect("Coding_Samurai.db")
cur = con.cursor()
#cur.execute("DROP TABLE tasks")
cur.execute("CREATE TABLE IF NOT EXISTS tasks(tID PRIMARY KEY, tName varchar(50), tDescription varchar(1000))")
#cur.execute("")

root = tk.Tk()
root.configure(background='#efb2ea')# #efb2ea
root.title("To Do List")
root.geometry("550x550+650+20")
root.resizable(True,True)
#main code

lab1 = Label(root, text="Task Title: ",background=BG, fg=TEXTCOLOR, font=FONT1)
lab1.place(x=20, y=20)

lab2 = Label(root, text="Task Description: ",background=BG, fg=TEXTCOLOR, font=FONT1)
lab2.place(x=20, y=57)

txt1 = Entry(root,width=35,font=FONT2)#height=1,
txt1.place(x=200,y=20)

txt2 = Entry(root,width=35,font=FONT2)#height=3,
txt2.place(x=200,y=57)

but1 = Button(root, text="Add Task", command=addTask,width=16, font=BUTTONFONT, background="#06ea00" , borderwidth = '3')
but1.place(x=20,y=150)

lab3 = Label(root, text="Added Tasks: ",background=BG, fg=TEXTCOLOR, font=FONT1)
lab3.place(x=20, y=210)

libox = Listbox(root,height=15,width=50,font=FONT3, selectmode="SINGLE", selectbackground="cyan",selectforeground="black")
libox.place(x=20,y=240)

but2 = Button(root, text = "Save", command=addTask,width=16, font=BUTTONFONT, background="cyan" , borderwidth = '3')
but2.place(x=400,y=240)

but2 = Button(root, text = "Complete", command=addTask,width=16, font=BUTTONFONT, background="cyan" , borderwidth = '3')
but2.place(x=400,y=290)
#https://stackoverflow.com/questions/25244454/python-create-strikethrough-strikeout-overstrike-string-type

but2 = Button(root, text = "Delete", command=deleteOne,width=16, font=BUTTONFONT, background="cyan" , borderwidth = '3')
but2.place(x=400,y=340)


# res = cur.execute("SELECT * FROM tasks")
# print('Fetched row: ',res.fetchall())


root.mainloop()

con.commit()
cur.close()

# fonts=list(font.families())
# fonts.sort()
# index = random.randint(0,len(fonts))
# FONT2 = (fonts[index],12)
# print(fonts[index])

# Segoe UI Symbol
# Sitka Heading Semibold

# def change_color(i=0):
#     if i < 4:
#         colors = ('beige', 'blue', 'green', 'black')
#         root.config(bg=colors[i])
#         root.after(500, change_color, (i+1)%4)

# change_color()
