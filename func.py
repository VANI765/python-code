from tkinter import *
from tkinter import messagebox
t1=Tk()
t1.title('MyLabel Widget')
obj1=Label(t1,text='Name')
obj1.grid(column=0,row=0)
obj2=Entry(t1)
obj2.grid(column=1,row=0)
obj3=Label(t1,text='Password')
obj3.grid(column=0,row=1)
obj4=Entry(t1,show="*")
obj4.grid(column=1,row=1)
def action():
    x=obj2.get()
    y=obj4.get()
    if x=='admin' and y=='123':
        messagebox.showinfo('Login','Login success')
    else:
        messagebox.showinfo('Login',"Login Fail")
btn=Button(t1,text='Submit',command=action,bg='orange',fg='red')
btn.grid(column=1,row=2)
mainloop()