import Tkinter
from Tkinter import*
import tkMessageBox
import sqlite3



def bak():
   top.destroy()
   import Index


def savedata(name,regno,password,email,specialization,phone):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    try:
       cur.execute('INSERT INTO reg_stud (name,regno,password,specialization,mail,mobile,supervisor) VALUES (?,?,?,?,?,?,?)', (name,regno,password,specialization,email,phone,''))
    except sqlite3.IntegrityError:
       tkMessageBox.showinfo("Alert","User already exist!")
    else:
       con.commit()
       tkMessageBox.showinfo("Alert","Registration Successfull")
       top.destroy()
       import logstud
    


    
top=Tkinter.Tk()
top.title("Supervisor Allotment System:: Register")
top.geometry('1000x650')




#Menu Start

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)



#Menu end

canvas = Canvas(width = 250, height = 10)
    
canvas.pack(expand = YES, fill = BOTH)
   
gif1 = PhotoImage(file = 'nregister.gif')
    
canvas.create_image(380, 20, image = gif1, anchor = NW)

w = Label(top, text="Register", font=("Monotype Corsiva", 40))
w.place(x=500,y=20)

w = Label(top, text="------------------------------------------------------------------------", font=("Monotype Corsiva", 30))
w.place(x=100,y=120)




L1 = Label(top, text="Name", font=("Cambria", 14))
L1.place(x=370,y=190)
name=StringVar()
E1 =Entry(top, bd =5 ,width=35, textvariable=name)
E1.place(x=440,y=190)


L2 = Label(top, text="Reg No.", font=("Cambria", 14))
L2.place(x=330,y=230)
regno=StringVar()

E2 =Entry(top, bd =5 ,width=35, textvariable=regno)
E2.place(x=440,y=230)


L3 = Label(top, text="Password", font=("Cambria", 14))
L3.place(x=335,y=270)
password=StringVar()

E3 = Entry(top, bd =5 ,width=35, show="*", textvariable=password)
E3.place(x=440,y=270)


L5 = Label(top, text="Email", font=("Cambria", 14))
L5.place(x=365,y=310)
email=StringVar()

E5 = Entry(top, bd =5 ,width=35, textvariable=email)
E5.place(x=440,y=310)


L4 = Label(top, text="Specialization", font=("Cambria", 14))
L4.place(x=320,y=350)
specialization=StringVar()

E4 = Entry(top, bd =5 ,width=35, textvariable=specialization)
E4.place(x=440,y=350)



L6 = Label(top, text="Contact No.", font=("Cambria", 14))
L6.place(x=320,y=390)
phone=StringVar()

E6 = Entry(top, bd =5 ,width=35, textvariable=phone)
E6.place(x=440,y=390)


B=Tkinter.Button(top,text="Register",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = lambda: savedata(name.get(),regno.get(),password.get(),email.get(),specialization.get(),phone.get()))
B.place(x=480,y=450)

B1=Tkinter.Button(top,text="Back",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = bak)
B1.place(x=300,y=450)

top.config(menu=menubar)
top.mainloop()
