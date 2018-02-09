import Tkinter
from Tkinter import*
import tkMessageBox
def supervisor():
        top.destroy()
        import supervisor
def stud():
        top.destroy()
        import student
top=Tkinter.Tk()
top.title("Supervisor Allotment System")
top.geometry('1000x650')
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="Options", menu=filemenu)
w = Label(top, text="Capstone Supervisor", font=("Monotype Corsiva", 40))
w.place(x=330,y=20)
w1 = Label(top, text="Allocation", font=("Monotype Corsiva", 40))
w1.place(x=420,y=80)
B=Tkinter.Button(top,text="Supervisor",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = supervisor)
B.place(x=530,y=220)
B1=Tkinter.Button(top,text="Student",font=("Monotype Corsiva",20),height=1,width=10,activebackground="powderblue",command = stud)
B1.place(x=280,y=220)
top.config(menu=menubar)
top.mainloop()
