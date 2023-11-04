import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root=Tk()
root.title("Register Form")
root.geometry("500x450")
root.config(bg="#ffcc00")
root.resizable(0,0)

name=StringVar()
email=StringVar()
password=StringVar()
gender=StringVar()
year=StringVar()
id=StringVar()
phone=StringVar()

#connect datatbase
con=sqlite3.connect("userdata.db")
cur=con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS student(
                name text,
                email text,
                password text,
                gender text,
                year text,
                mkpt int,
                phno int
                )
            ''')

con.commit()
def register():
    msg = f'Name :{name.get()} \n Email: {email.get()} \n Password : {password.get()}\n Gender :{gender.get()}\n Year :{year.get()}\n MKPT :{id.get()}\n ContactNO :{phone.get()}'
    showinfo(
        title='Information',
        message=msg
    )
def insert_record():
    check_counter = 0
    if en.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if ee.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if epass.get() == "":
        warn = "Password can't be empty"

    else:
        check_counter += 1

    if gender.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if year.get() == "":
        warn = "Select Year"
    else:
        check_counter += 1

    if id.get() == "":
        warn = "MKPT can't be empty"
    else:
        check_counter += 1
    if phno.get() == "":
        warn = "fill the contact"
    else:
        check_counter += 1
#insertdata
    if check_counter==7:
        try:
            con=sqlite3.connect("userdata.db")
            cur=con.cursor()
            cur.execute("INSERT INTO student VALUES (:name, :email, :password, :gender, :year, :mkpt, :phno)",{
                        'name':en.get(),
                        'email':ee.get(),
                        'password':epass.get(),
                        'gender':gender.get(),
                        'year':year.get(),
                        'mkpt':mkpt.get(),
                        'phno':phno.get()

            })
            con.commit()
            messagebox.showinfo("Confirmation","Record Saved")
        except Exception as ep:
            messagebox.showerror("",ep)
    else:
        messagebox.showerror("Error", warn)

def clear():
    messagebox.askokcancel("Ask Ok Cancel", "Are you sure to delete!")



'''top=Label(root,text="Register here",font=("arial",16),bg="#ffcc00")
top.grid(column=0,row=0,pady=10,padx=10,sticky=N)'''

ln=Label(root,text="Name",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
ln.grid(column=0,row=1,pady=10,padx=10,sticky=W)

le=Label(root,text="Email",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
le.grid(column=0,row=2,pady=10,padx=10,sticky=W)

lpass=Label(root,text="Password",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
lpass.grid(column=0,row=3,pady=10,padx=10,sticky=W)

lgender=Label(root,text="Gender",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
lgender.grid(column=0,row=4,sticky=W,padx=10,pady=10)

lyear=Label(root,text="Year",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
lyear.grid(column=0,row=5,sticky=W,padx=10,pady=10)

lid=Label(root,text="MKPT",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
lid.grid(column=0,row=6,sticky=W,padx=10,pady=10)

lph=Label(root,text="Phno",bg="#f2f2f2",font=("Arial Rounded MT Bold",10))
lph.grid(column=0,row=7,sticky=W,padx=10,pady=10)




en=ttk.Entry(root,textvariable=name)
en.grid(column=1,row=1,pady=10,padx=10,sticky=E)

ee=ttk.Entry(root,textvariable=email)
ee.grid(column=1,row=2,pady=10,padx=10,sticky=E)

epass=ttk.Entry(root,show="*",textvariable=password)
epass.grid(column=1,row=3,pady=10,padx=10,sticky=E)

male=ttk.Radiobutton(root,text="Male",variable=gender,value="Male").grid(column=1,row=4,sticky=NW,pady=20,padx=10)
female=ttk.Radiobutton(root,text="Female",variable=gender,value="Female").grid(column=2,row=4,sticky=E,pady=20,padx=10)

year=ttk.Combobox(root,width=19,textvariable=year)
year['values']=('first year','second year','third year','forth year','fifth year')
year.current(0)
year.grid(column=1,row=5,sticky=E)

mkpt=ttk.Entry(root,textvariable=id)
mkpt.grid(column=1,row=6,pady=10,padx=10,sticky=E)

phno=ttk.Entry(root,textvariable=phone)
phno.grid(column=1,row=7,pady=10,padx=10,sticky=E)


btnre=Button(root,text="Register",bg="#003399",fg="white",relief=RAISED,command=insert_record())
btnre.grid(column=0,row=10,sticky=E,padx=10,pady=20,ipady=15,ipadx=10)
btnclear=Button(root,text="Clear",bg="#ad423f",fg="white",relief=RAISED,command=clear)
btnclear.grid(column=2,row=10,sticky=E,padx=10,pady=20,ipady=15,ipadx=10)
root.mainloop()