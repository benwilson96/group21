import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql

LARGE_FONT=("Verdana", 12)



def verify_details(Page,UN,PW):
    db = pymysql.connect(host="csmysql.cs.cf.ac.uk", user="c1531722", passwd="pE9zby3j", db="c1531722")
    cursor = db.cursor()
    cursor.execute("SELECT Username, Password, Admin FROM Accounts")

    InputUN = UN.get()
    InputPW = PW.get()
    for UN, PW, ADM in cursor:
        if UN == InputUN and PW == InputPW:
            app.show_frame(LoggedIn)

            break
    if not(UN == InputUN and PW == InputPW):
        Page.unsuccessful_login()

    db.close()

def insert_account(UN,PW,Admin):
    db = pymysql.connect(host="csmysql.cs.cf.ac.uk", user="c1531722", passwd="pE9zby3j", db="c1531722")
    cursor = db.cursor()
    cursor.execute("SELECT ID FROM Accounts ORDER BY ID DESC")
    ID = cursor.fetchone()
    InputUN = UN.get()
    InputPW = PW.get()
    cursor.execute('''INSERT INTO `c1531722`.`Accounts` (`ID`, `Username`, `Password`, `Admin`) VALUES (%s, %s, %s, %s);''',(ID[0]+1,InputUN,InputPW,Admin))
    db.commit()
    db.close()

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Program")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, Register, LoggedIn):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l1 = ttk.Label(self, text="Login", font=LARGE_FONT)
        l1.pack(pady=10,padx=10)

        l2 = ttk.Label(self, text="User Name")
        l2.pack(side=LEFT)

        l3 = ttk.Label(self, text="Password ")
        l3.pack(side=LEFT)

        UserN_input = ttk.Entry(self, width=20)
        UserN_input.pack(side=RIGHT)

        PW_input = ttk.Entry(self, width=20)
        PW_input.pack(side=RIGHT)

        LoginBtn = ttk.Button(self, text="Login", command= lambda: verify_details(self, UserN_input, PW_input))
        LoginBtn.pack(side = BOTTOM)

        RegBtn = ttk.Button(self, text="Register", command= lambda: controller.show_frame(Register))
        RegBtn.pack(side = BOTTOM)

    def unsuccessful_login():
        l4 = ttk.Label(self, text="Inccorect login credentials")
        l4.pack(side=BOTTOM)


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self, text="Register", font=LARGE_FONT)
        l1.pack(pady=10,padx=10)

        l2 = ttk.Label(self, text="User Name")
        l2.pack(side=LEFT)

        l3 = ttk.Label(self, text="Password ")
        l3.pack(side=LEFT)

        UserN_input = ttk.Entry(self, width=20)
        UserN_input.pack(side=RIGHT)

        PW_input = ttk.Entry(self, width=20)
        PW_input.pack(side=RIGHT)

        RegBtn = ttk.Button(self, text="Register", command= lambda: insert_account(UserN_input,PW_input,1))
        RegBtn.pack(side = BOTTOM)

class LoggedIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Login Successful", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

app = SeaofBTCapp()
app.mainloop()
