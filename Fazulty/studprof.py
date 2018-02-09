import Tkinter
from Tkinter import*
import tkMessageBox
import sqlite3



def out():
   top.destroy()
   import Index

def sup():
    f=open("user.txt","r")
    name=f.readline()
    f.close()
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cursor=cur.execute('SELECT * FROM reg_stud WHERE regno = ?',(name,))
    for row in cursor:
        specialization=row[4]
        supervisor=row[7]
    if supervisor=='':
       try:
          cur.execute('INSERT INTO allot (fname,sname,specialization) VALUES (?,?,?)', ("abc",name,specialization))
       except sqlite3.IntegrityError:
          tkMessageBox.showinfo("Alert","Already Requested!")
       else:
          con.commit()
          tkMessageBox.showinfo("Alert","Your request has been added!")
          
          
    else:
         tkMessageBox.showinfo("Alert","Your Supervisor is already alloted!")
         f=StringVar()
         f.set(supervisor)
         w2=Label(top,text=" UID of Supervisor : ",font=("Monotype Corsiva", 14))
         w2.place(x=410,y=360)

         w3=Label(top,textvariable=f,font=("Monotype Corsiva", 14))
         w3.place(x=570,y=360)
    
         
        
   



top=Tkinter.Tk()
top.title("Student :: Profile")
top.geometry('1000x650')

#Menu Start

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)



#Menu end


f=open("user.txt","r")
name=f.readline()
f.close()

con = sqlite3.connect('main.db')
cur = con.cursor()


   
cursor=cur.execute('SELECT * FROM reg_stud WHERE regno = ?',(name,))
for row in cursor:
    user=row[1]
    specialization=row[4]
    phone=row[5]
    mail=row[6]
    supervisor=row[7]
    






a=StringVar()
a.set(user)

b=StringVar()
b.set(specialization)

c=StringVar()
c.set(phone)

d=StringVar()
d.set(supervisor)

e=StringVar()
e.set(mail)







canvas = Canvas(width = 250, height = 10)
    
canvas.pack(expand = YES, fill = BOTH)
   
gif1 = PhotoImage(file = 'profile.gif')
    
canvas.create_image(300, 20, image = gif1, anchor = NW)


w1=Label(top,textvariable=a,font=("Monotype Corsiva", 34))
w1.place(x=482,y=50)

w2=Label(top,text="E-Mail : ",font=("Monotype Corsiva", 14))
w2.place(x=482,y=100)

w3=Label(top,textvariable=e,font=("Monotype Corsiva", 14))
w3.place(x=545,y=100)

w4=Label(top,text="Phone : ",font=("Monotype Corsiva", 14))
w4.place(x=482,y=125)

w5=Label(top,textvariable=c,font=("Monotype Corsiva", 14))
w5.place(x=545,y=125)

w4=Label(top,text="Specialization : ",font=("Monotype Corsiva", 14))
w4.place(x=482,y=150)

w5=Label(top,textvariable=b,font=("Monotype Corsiva", 14))
w5.place(x=600,y=150)




B1=Tkinter.Button(top,text="Request Supervisor",font=("Monotype Corsiva",20),height=1,width=16,activebackground="powderblue",command = sup)
B1.place(x=400,y=290)






B=Tkinter.Button(top,text="Logout",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = out)
B.place(x=800,y=5)




top.config(menu=menubar)
top.mainloop()
