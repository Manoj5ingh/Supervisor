import Tkinter
from Tkinter import*
import tkMessageBox
import sqlite3



def out():
   top.destroy()
   import Index

def select(option):
    tkMessageBox.showinfo("Alert","Successfully added!")
    f=open("user.txt","r")
    name=f.readline()
    f.close()
    con = sqlite3.connect('main.db')
    cur3 = con.cursor()
    cur3.execute('DELETE FROM allot where sname=?',(option,))
    cur3.execute('UPDATE reg_stud SET supervisor=? where regno=?',(name,option,))
    con.commit()
    
def time(t):
    f=open("user.txt","r")
    name=f.readline()
    f.close()
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cursor=cur.execute('UPDATE reg_fac SET hours = ? WHERE uid=?' ,(t,name,))
    con.commit()
    tkMessageBox.showinfo("Alert","Your open hours updated!")

def sel():
    f=open("user.txt","r")
    name=f.readline()
    f.close()
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cursor=cur.execute('SELECT * FROM reg_fac WHERE uid = ?',(name,))
    for row in cursor:
        specialization=row[4]

    students=[]    
    cursor=cur.execute('SELECT * FROM allot WHERE specialization = ?',(specialization,))
    for row in cursor:
        a=row[2]
        students.append(a)

    w1=Label(top,text="Students : ",font=("Monotype Corsiva", 18))
    w1.place(x=400,y=520)

    option = StringVar(top)
    option.set(students[0])

    w = apply(OptionMenu, (top, option) + tuple(students))
    w.place(x=500,y=520)

    B2=Tkinter.Button(top,text="Select",font=("Monotype Corsiva",16),height=1,width=12,activebackground="powderblue",command = lambda: select(option.get()))
    B2.place(x=450,y=560)

def sup():
    f=open("user.txt","r")
    name=f.readline()
    f.close()
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cursor=cur.execute('SELECT * FROM reg_fac WHERE uid = ?',(name,))
    for row in cursor:
        specialization=row[4]

    w1=Label(top,text="Open Hours : ",font=("Monotype Corsiva", 18))
    w1.place(x=350,y=400)
    t=StringVar()

    E3 = Entry(top, bd =5 ,width=35, textvariable=t)
    E3.place(x=480,y=400)

    B1=Tkinter.Button(top,text="Update",font=("Monotype Corsiva",16),height=1,width=12,activebackground="powderblue", command = lambda: time(t.get()))
    B1.place(x=430,y=440)

    
    
    
    
    
    
         
        
   



top=Tkinter.Tk()
top.title("Faculty :: Profile")
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


   
cursor=cur.execute('SELECT * FROM reg_fac WHERE uid= ?',(name,))
for row in cursor:
    user=row[1]
    specialization=row[4]
    phone=row[5]
    mail=row[6]
    hours=row[7]
    






a=StringVar()
a.set(user)

b=StringVar()
b.set(specialization)

c=StringVar()
c.set(phone)

d=StringVar()
d.set(hours)

e=StringVar()
e.set(mail)

h=StringVar()
h.set(hours)






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

w4=Label(top,text="Open hours : ",font=("Monotype Corsiva", 14))
w4.place(x=482,y=175)

w5=Label(top,textvariable=h,font=("Monotype Corsiva", 14))
w5.place(x=600,y=175)




B1=Tkinter.Button(top,text="Select Students",font=("Monotype Corsiva",20),height=1,width=16,activebackground="powderblue",command = sel)
B1.place(x=310,y=290)

B1=Tkinter.Button(top,text="Open Hours",font=("Monotype Corsiva",20),height=1,width=16,activebackground="powderblue",command = sup)
B1.place(x=550,y=290)






B=Tkinter.Button(top,text="Logout",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = out)
B.place(x=800,y=5)




top.config(menu=menubar)
top.mainloop()
