import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('MyTaskList')
root.geometry('500x650+500+100')  
root.resizable(False, False) 

myTaskList = []

def addTask():
    task = task_add_entry.get()
    task_add_entry.delete(0,END)
    
    if task:
        with open ("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        myTaskList.append(task)
        listbox.insert(END,task)
        

def deletTask():
    global  myTaskList
    task = str(listbox.get(ANCHOR))
    if task in myTaskList:
        myTaskList.remove(task)
        with open ("tasklist.txt", "w") as taskfile:
            for task in myTaskList:
                taskfile.write(task+"\n")
            
            listbox.delete( ANCHOR)
           
      

def TaskFileMange():
    try:
        global myTaskList
        with open ("tasklist.txt", "r") as taskfile:
           tasks = taskfile.readlines()
        for task in tasks:
           if task != '\n':
            myTaskList.append(task)
            listbox.insert(END,task)
    except:
         file=open("tasklist.txt", "w")
         file.close()

myIcon = tk.PhotoImage(file="public/logo.png")
root.iconphoto(False, myIcon)
root.configure(bg="#333333") 

new_width = 44  
new_height = 44 

myIcon = myIcon.subsample(int(myIcon.width() / new_width), int(myIcon.height() / new_height))
topBarImage = tk.PhotoImage(file="public/topbar.png")
Label(root, image=topBarImage).pack()
Label(root, image=myIcon , bg='#53545b').place(x=30,y=15)



PageTitle = Label(root, text='MyTasks', font="arial 50 bold", fg="white", bg="#53545b")
PageTitle.place(x=70,y=5)


addFrame= Frame(root, width=400 ,height=60, bg='#595959')
addFrame.place(x=50, y=130)


taskAdd=StringVar()

task_add_entry = Entry(addFrame, width=18, font="arial 34", highlightbackground="#595959", bg='#595959',  fg="white")
task_add_entry.place(x=3, y=4)
task_add_entry.focus()


button_image = tk.PhotoImage(file="public/add.png")


addButton = tk.Button(root, image=button_image, compound="left", font='arial 33', width=36,height=38, bg='#5a95ff', fg='#000', highlightbackground="white", command=addTask)
addButton.place(x=403, y=136)


frameList = tk.Frame(root, bd=3, width=100, height=400, bg='#53545b')
frameList.pack(pady=(160, 0))

listbox = tk.Listbox(frameList, font=('arial', 32), width=27, height=27, bg='#53545b', fg='white', cursor="hand2", selectbackground="#5a95ff")

listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
scrollbar_List = tk.Scrollbar(frameList)
scrollbar_List.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar_List.set)
scrollbar_List.config(command=listbox.yview)

delete_list_icon = tk.PhotoImage(file="public/delete.png")
new_width = 50
new_height = 50
delete_list_icon = delete_list_icon.subsample(int(delete_list_icon.width() / new_width), int(delete_list_icon.height() / new_height))

TaskFileMange()

delete_button = tk.Button(root, image=delete_list_icon, bg="#53545b" ,width=30, height=30,command=deletTask)
delete_button.place(x=220, y=580)  


root.mainloop()
