import Tkinter
from Tkinter import*
import tkMessageBox
import sqlite3


def bak():
   top.destroy()
   import Index

def chckdata():
   con = sqlite3.connect('main.db')
   cur = con.cursor()
   user=username.get()
   code=password.get()
   cur.execute('SELECT * FROM reg_stud WHERE regno = ? AND password = ?', (user, code))
   if cur.fetchall():
      tkMessageBox.showinfo("Alert","Login Successfull!")
      f=open("user.txt","w")
      f.write(user);
      f.close();
      top.destroy()
      import studprof
   else:
      tkMessageBox.showinfo("Alert","Invalid data or User doesn't exist!")
    
   


top=Tkinter.Tk()
top.title("Student Login")
top.geometry('1000x650')




menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)







canvas = Canvas(width = 250, height = 150)
    
canvas.pack(expand = YES, fill = BOTH)
   
gif1 = PhotoImage(file = 'login.gif')
    
canvas.create_image(350, 100, image = gif1, anchor = NW)

w = Label(top, text=" Student Login", font=("Monotype Corsiva", 40))
w.place(x=500,y=150)

w1 = Label(top, text="------------------------------------------------------------------------", font=("Monotype Corsiva", 30))
w1.place(x=100,y=250)


L2 = Label(top, text="Reg No", font=("Cambria", 14))
L2.place(x=330,y=320)
username=StringVar()

E2 =Entry(top, bd =5 ,width=35, textvariable=username)
E2.place(x=440,y=320)


L3 = Label(top, text="Password", font=("Cambria", 14))
L3.place(x=335,y=380)
password=StringVar()

E3 = Entry(top, bd =5 ,width=35, show="*", textvariable=password)
E3.place(x=440,y=380)


B=Tkinter.Button(top,text="Login",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command =  chckdata)
B.place(x=480,y=440)

B1=Tkinter.Button(top,text="Back",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = bak)
B1.place(x=300,y=440)



top.config(menu=menubar)
top.mainloop()
