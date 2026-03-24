# using tkinter 
# framework 

import tkinter
from tkinter import*
from tkinter import messagebox
win=Tk()
win.configure(background="blue")
win.geometry('700x500')
def signup () :
    messagebox.showinfo("Dear user ", " Personal detials needed")
 

lab=Label(win, text='Sign up ',fg='White',font=('arial',16,'bold'),bg='blue').place(relx=0.5,rely=0.2,anchor=CENTER)
username_lab=Label(win,text="Username")
username_entry=Entry(win,width=25).place(relx=0.5,rely=0.4,anchor=CENTER)

username_entry2=Entry(win,width=25).place(relx=0.5,rely=0.5,anchor=CENTER)

username_entry3=Entry(win,width=25).place(relx=0.5,rely=0.6,anchor=CENTER)



btn=Button(win,text='Register',bg='black',fg='white',width=25,height=2,border=0,command=signup).place(relx=0.5,rely=0.7,anchor=CENTER)


lab=Label(win, text='Username:',fg='White',font=('arial',16,'bold'),bg='blue').place(relx=0.3,rely=0.4,anchor=CENTER)

lab=Label(win, text='Email: ',fg='White',font=('arial',16,'bold'),bg='blue').place(relx=0.3,rely=0.5,anchor=CENTER)

lab=Label(win, text='Password:',fg='White',font=('arial',16,'bold'),bg='blue').place(relx=0.3,rely=0.6,anchor=CENTER)








































win.mainloop()