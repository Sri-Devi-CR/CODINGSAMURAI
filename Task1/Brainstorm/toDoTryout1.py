import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
#REFERENCES OF SQLITE3
#https://docs.python.org/3/library/sqlite3.html

#REFERENCES FOR FONTS
#https://www.tutorialspoint.com/python/tk_fonts.htm
import sqlite3 as sql
import random

FONT1 = ("Sitka Heading",13)
FONT2 = ("Segoe UI Symbol",13)
FONT3 = ("Segoe UI Symbol",10)
BUTTONFONT = ("Sitka Heading",11)
BG = "#efb2ea"
BG2 = "cyan"
TEXTCOLOR = "black"
TASK_X = 0
TASK_Y = 30
TASK_SPACE = 40

task_title_di = {}
task_desc_di = {}
taskID = []
#------------------------------- Functions--------------------------------
def addTask():
    task_title = txt1.get()
    task_desc = txt2.get()

    if len(task_title)==0:
        messagebox.showinfo('Empty Entry', 'Enter task title')
    else:
        ##SIMPLY INSERT TASK TITLE AND DESCRIPTION IN DB AND CALL SELECT * FROM EVERYTIME A TASK IS ADDED
        ##IF TASK IS DELETED, CALL SELECT QUERY AGAIN
        global TASK_Y
        dyn_lab = Label(parent_lab, text=task_title,background=BG,fg=TEXTCOLOR,font=FONT2)
        dyn_lab.pack(fill=tk.BOTH, expand=True)
        txt1.delete(0,tk.END)
        txt2.delete(0,tk.END)
        #dyn_lab.place(x=TASK_X,y=TASK_Y)
        TASK_Y += TASK_SPACE


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

parent_lab = Label(root, background=BG2, height=20, width=70, borderwidth='2')
parent_lab.place(x=20,y=210)

lab3 = Label(parent_lab, text="Added Tasks: ",background=BG2, fg=TEXTCOLOR, font=FONT1)
lab3.place(x=0, y=0)

# libox = Listbox(root,height=13,width=50,font=FONT3, selectmode="SINGLE", selectbackground="cyan",selectforeground="black")
# libox.place(x=20,y=240)

# but2 = Button(root, text = "Save", command=addTask,width=16, font=BUTTONFONT, background="cyan" , borderwidth = '3')
# but2.place(x=360,y=240)

# but2 = Button(root, text = "Complete", command=addTask,width=16, font=BUTTONFONT, background="cyan" , borderwidth = '3')
# but2.place(x=360,y=290)
# #https://stackoverflow.com/questions/25244454/python-create-strikethrough-strikeout-overstrike-string-type

# but2 = Button(root, text = "Delete", command=addTask,width=16, font=BUTTONFONT, background="cyan" , borderwidth = '3')
# but2.place(x=360,y=340)


# res = cur.execute("SELECT * FROM tasks")
# print('Fetched row: ',res.fetchall())


root.mainloop()

con.commit()
cur.close()
