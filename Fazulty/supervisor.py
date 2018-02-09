import Tkinter
from Tkinter import*
import tkMessageBox



def logfac():
        top.destroy()
        import logfac

def regfac():
        top.destroy()
        import regfac
        

   
top=Tkinter.Tk()
top.title("Supervisor Allotment System")
top.geometry('1000x650')


#Menu Start

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)



#Menu end




w = Label(top, text="Supervisor Page", font=("Monotype Corsiva", 40))
w.place(x=360,y=20)




B=Tkinter.Button(top,text="Login",font=("Monotype Corsiva",20),height=1,width=12,activebackground="powderblue",command = logfac)
B.place(x=530,y=220)




B1=Tkinter.Button(top,text="New User",font=("Monotype Corsiva",20),height=1,width=10,activebackground="powderblue",command = regfac)
B1.place(x=280,y=220)










top.config(menu=menubar)
top.mainloop()
