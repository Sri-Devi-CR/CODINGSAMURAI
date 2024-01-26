'''
-------------------------------------------------CODING SAMURAI TASK 1-------------------------------------------------------------
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
from tkinter import simpledialog
import sqlite3 as sql
import random

#REFERENCES OF SQLITE3
#https://docs.python.org/3/library/sqlite3.html

#REFERENCES FOR FONTS
#https://www.tutorialspoint.com/python/tk_fonts.htm
# from tkinter import font

FONT1 = ("Sitka Heading",13)
FONT2 = ("Sitka Heading",11)
BUTTONFONT = ("Sitka Heading",11)
BG = 'plum'#"#efb2ea"
BG2 = "beige"
BG3 = '#cfb997'
TEXTCOLOR = "black"
SELECT = "SELECT * FROM tasks"
SELECT2 = "SELECT * FROM completedTasks"
CREATE = "CREATE TABLE IF NOT EXISTS tasks(tID PRIMARY KEY, tName varchar(50), tDescription varchar(1000))"
CREATE2 = "CREATE TABLE IF NOT EXISTS completedTasks(tID PRIMARY KEY, tName varchar(50), tDescription varchar(1000))"

global comp_taskID, comp_task_title_di, comp_task_desc_di
global taskID,task_title_di,task_desc_di,result
task_title_di = {}
task_desc_di = {}
taskID = []
comp_task_title_di = {}
comp_task_desc_di = {}
comp_taskID = []


def addTask(): #TO DATABASE
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

def updateToLiAndDi(li,di1,di2,query):
    cur.execute(query)
    result = cur.fetchall()
    for ttuple in result:
        for j in range(len(ttuple)):
            if int(ttuple[0]) not in li:
                li.append(int(ttuple[0]))
                di1[int(ttuple[0])] = ttuple[1]
                di2[int(ttuple[0])] = ttuple[2]

def listUpdate():
    column_names = ["Task ID", "Task title", "Task Description"]

    TASK_X=20
    TASK_Y=210

    for i in range(3):
        if i==0:
            lab = Label(root, text=column_names[i], font=FONT2,bg=BG3,height=1, width=10, borderwidth = 1, relief = 'ridge')
        else:
            lab = Label(root, text=column_names[i],font=FONT2,bg=BG3,height=1, width=22, borderwidth = 1, relief = 'ridge')
            if i==2:
                TASK_X += 100

        lab.place(x=TASK_X,y=TASK_Y)
        TASK_X += 100    

    TASK_X = 20
    TASK_Y = 240

    for i in range(len(taskID)):
        lab1 = Label(root, font=FONT2,bg=BG2,height=1, width=10, borderwidth = 1, relief = 'ridge', text = taskID[i])
        lab2 = Label(root, font=FONT2,bg=BG2,height=1, width=22, borderwidth = 1, relief = 'ridge', text = task_title_di[taskID[i]])
        lab3 = Label(root, font=FONT2,bg=BG2,height=1, width=22, borderwidth = 1, relief = 'ridge', text = task_desc_di[taskID[i]])

        lab1.place(x=TASK_X,y=TASK_Y)
        lab2.place(x=TASK_X+100,y=TASK_Y)
        lab3.place(x=TASK_X+300,y=TASK_Y)

        TASK_Y+=30

def completeWindow():
    try:
        global task_ID_enter_tk
        task_ID_enter_tk = tk.Tk()
        task_ID_enter_tk.title("Completed Tasks")
        task_ID_enter_tk.configure(background=BG)
        task_ID_enter_tk.geometry("550x300+50+20")

        ID_to_del = int(tID_input)

        cur.execute('insert into completedTasks values (?,?,?)', (ID_to_del,task_title_di[ID_to_del],task_desc_di[ID_to_del]))
        cur.execute('delete from tasks where tID = ?',(ID_to_del,))
        con.commit()

        # appendCompTask()
        updateToLiAndDi(comp_taskID,comp_task_title_di,comp_task_desc_di,SELECT2)
        # appendTask()
        updateToLiAndDi(taskID,task_title_di,task_desc_di,SELECT)
        taskID.remove(ID_to_del)
        task_title_di.pop(ID_to_del)
        task_desc_di.pop(ID_to_del)

        listUpdate()

        cur.execute("SELECT * FROM completedTasks")
        res = cur.fetchall()

        column_names = ["Task ID", "Task title", "Task Description"]

        CTASK_X = 20
        CTASK_y = 10
        for j in range(3):
            if j!=0:
                lab = Label(task_ID_enter_tk, font=FONT2,bg=BG3,height=1, width=22, borderwidth = 1, relief = 'ridge')####
                if j==2:
                        lab.place(x=CTASK_X,y=CTASK_y)
                        CTASK_X += 100 
                
            else:
                lab = Label(task_ID_enter_tk, font=FONT2,bg=BG3,height=1, width=10, borderwidth = 1, relief = 'ridge')
            lab.config(text=column_names[j])
            lab.place(x=CTASK_X,y=CTASK_y)
            CTASK_X+=100

        CTASK_X = 20
        CTASK_y = 40
        for tasc in res:
            CTASK_X = 20
            for j in range(len(tasc)):
                if j!=0:
                    lab = Label(task_ID_enter_tk, font=FONT2,bg=BG2,height=1, width=22, borderwidth = 1, relief = 'ridge')####
                    if j==2:
                            lab.place(x=CTASK_X,y=CTASK_y)
                            CTASK_X += 100 
                
                else:
                    lab = Label(task_ID_enter_tk, font=FONT2,bg=BG2,height=1, width=10, borderwidth = 1, relief = 'ridge')

                lab.config(text=str(tasc[j]))
                lab.place(x=CTASK_X,y=CTASK_y)
                CTASK_X += 100
            CTASK_y += 30
            j=0
            # i+=1

        task_ID_enter_tk.mainloop()
    except:
        print()

def completeTask():
    # task_ID_enter_tk.withdraw()
    global tID_input
    tID_input = simpledialog.askstring(title="Yay",prompt="Enter task ID of the task that is completed:")
    if int(tID_input) in taskID:
        if len(comp_taskID)!=0:
            task_ID_enter_tk.destroy()
        completeWindow()
        
    else:
        messagebox.showerror("Error","Invalid Task ID")

def deleteTask():
    cur.execute("DROP TABLE completedTasks")
    cur.execute(CREATE2)
    con.commit()
    if len(comp_taskID)!=0:
        task_ID_enter_tk.destroy()
        completeWindow()

def saveTask(): # TO TEXT FILE
    tasks_txt = open("Tasks.txt",'w')
    tasks_txt.write("TASKS TO DO")
    tasks_txt.write("\n")
    for id in taskID:
        tasks_txt.write("Task ID: "+str(id))
        tasks_txt.write("\nTask Title: "+task_title_di[id])
        tasks_txt.write("\nTask Description: "+task_desc_di[id])
        tasks_txt.write("\n")

    tasks_txt.write("\n")
    tasks_txt.write("TASKS COMPLETED")
    tasks_txt.write("\n")
    for id in comp_taskID:
        tasks_txt.write("Task ID: "+str(id))
        tasks_txt.write("\nTask Title: "+comp_task_title_di[id])
        tasks_txt.write("\nTask Description: "+comp_task_desc_di[id])
        tasks_txt.write("\n")

    tasks_txt.close()
    messagebox.showinfo("Info","Check Tasks.txt to see the saved tasks")

con = sql.connect("Coding_Samurai.db")
cur = con.cursor()
# cur.execute("DROP TABLE tasks")
# cur.execute("DROP TABLE completedTasks")
cur.execute(CREATE)
cur.execute(CREATE2)

root = tk.Tk()
root.configure(background=BG)# #efb2ea
root.title("To Do List")
root.geometry("550x550+650+20")
root.resizable(True,True)
#main code

lab1 = Label(root, text="Task Title: ",background=BG, fg=TEXTCOLOR, font=FONT1)
lab1.place(x=20, y=20)

lab2 = Label(root, text="Task Description: ",background=BG, fg=TEXTCOLOR, font=FONT1)
lab2.place(x=20, y=57)

txt1 = Entry(root,width=35,font=FONT1)
txt1.place(x=200,y=20)

txt2 = Entry(root,width=35,font=FONT1)
txt2.place(x=200,y=57)

but1 = Button(root, text="Add Task", command=addTask,width=12, font=BUTTONFONT, background="#06ea00" , borderwidth = '3')
but1.place(x=20,y=130)

but2 = Button(root, text = "Save", command=saveTask,width=12, font=BUTTONFONT, background="cyan" , borderwidth = '3')
but2.place(x=150,y=130)

but2 = Button(root, text = "Complete", command=completeTask,width=12, font=BUTTONFONT, background="cyan" , borderwidth = '3')
but2.place(x=280,y=130)

but2 = Button(root, text = "Delete All", command=deleteTask,width=12, font=BUTTONFONT, background="cyan" , borderwidth = '3')
but2.place(x=410,y=130)

updateToLiAndDi(taskID,task_title_di,task_desc_di,SELECT)
listUpdate()

root.mainloop()
con.commit()
cur.close()

"""
Improvements needed in:
1. Tasks when completed have issues when printed onto to do tasks 
"""