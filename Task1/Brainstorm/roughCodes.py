import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)

#118-161
'''
    cur.execute(SELECT)
    global res
    res = cur.fetchall()
    print("Result in listupdate ",res)
    column_names = ["Task ID", "Task title", "Task Description"]

    TASK_X = 20
    TASK_Y = 210
    for j in range(3):
        if j!=0:
            lab = Label(root, font=FONT2,bg=BG3,height=1, width=22, borderwidth = 1, relief = 'ridge')####
            if j==2:
                    lab.place(x=TASK_X,y=TASK_Y)
                    TASK_X += 100 
            
        else:
            lab = Label(root, font=FONT2,bg=BG3,height=1, width=10, borderwidth = 1, relief = 'ridge')
        lab.config(text=column_names[j])
        lab.place(x=TASK_X,y=TASK_Y)
        TASK_X+=100

    TASK_X = 20
    TASK_Y = 240
    for tasc in res:
        TASK_X = 20
        for j in range(len(tasc)):
            if j!=0:
                lab = Label(root, font=FONT2,bg=BG2,height=1, width=22, borderwidth = 1, relief = 'ridge')####
                if j==2:
                        lab.place(x=TASK_X,y=TASK_Y)
                        TASK_X += 100 
            
            else:
                lab = Label(root, font=FONT2,bg=BG2,height=1, width=10, borderwidth = 1, relief = 'ridge')

            lab.config(text=str(tasc[j]))
            lab.place(x=TASK_X,y=TASK_Y)
            TASK_X += 100
        TASK_Y += 30
        flag=1
        j=0
        # i+=1
    '''