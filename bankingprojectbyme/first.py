import tkinter as tk
from tkinter import messagebox
from time import gmtime,strftime

#window for creating account button
def Create():
    crwn=tk.Tk()
    crwn.geometry("600x300")
    crwn.title("Create Account")
    crwn.configure(bg='#0F1123')
    l_title=tk.Message(crwn,text="Online Banking System",relief='raised',width=2000,padx=600,pady=0,fg='white',bg='#0F1123',justify='center',font=("Arial","50","bold"))
    l_title.pack(side='top')
    l1=tk.Label(crwn,text="Enter name:",relief="raised")
    l1.place(x=710,y=100)
    e1=tk.Entry(crwn)
    e1.place(x=680,y=130)
    l2=tk.Label(crwn,text="Enter Opening Credit:",relief="raised")
    l2.place(x=680,y=160)
    e2=tk.Entry(crwn)
    e2.place(x=680,y=190)
    l3=tk.Label(crwn,text="Enter desired PIN:",relief="raised")
    l3.place(x=690,y=220)
    e3=tk.Entry(crwn,show="*")
    e3.place(x=680,y=250)
    b=tk.Button(crwn,text="submit",command=lambda:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.place(x=725,y=280)
    crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    return


#for logout
def logout(master):
    messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()


#for checking the login credentials
def check_log_in(master,name,acc_num,pin):
    if(check_acc_nmb(acc_num)==0):
        master.destroy()
        Main_Menu()
        return

    if( (is_number(name))  or (is_number(pin)==0) ):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()
    else:
        master.destroy()
        logged_in_menu(acc_num,name)

#window for logging in
def log_in(master):
    master.destroy()
    loginwn=tk.Tk()
    loginwn.geometry("600x300")
    loginwn.title("Log in")
    loginwn.configure(bg="#0F1123")
    fr1=tk.Frame(loginwn,bg="blue")
    l_title=tk.Message(loginwn,text="Online Banking system",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#0F1123",justify="center",font=("Arial","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(loginwn,text="Enter Name:",relief="raised")
    l1.place(x=710,y=100)
    e1=tk.Entry(loginwn)
    e1.place(x=680,y=130)
    l2=tk.Label(loginwn,text="Enter account number:",relief="raised")
    l2.place(x=680,y=160)
    e2=tk.Entry(loginwn)
    e2.place(x=680,y=190)
    l3=tk.Label(loginwn,text="Enter your PIN:",relief="raised")
    l3.place(x=705,y=220)
    e3=tk.Entry(loginwn,show="*")
    e3.place(x=680,y=250)
    b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.place(x=725,y=280)
    b1=tk.Button(text="HOME",relief="raised",bg="black",fg="white",command=lambda: home_return(loginwn))
    b1.place(x=725,y=310)
    loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))

#window for logging in menuu
def logged_in_menu(accnt,name):
    rootwn=tk.Tk()
    rootwn.geometry("1200x1000")
    rootwn.title("Online banking System")
    rootwn.configure(background='#0F1123')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title=tk.Message(rootwn,text="Online Banking System",relief='raised',width=2000,padx=600,pady=0,fg='white',bg='#0F1123',justify='center',font=("Arial","50","bold"))
    l_title.pack(side='top')
    label1=tk.Label(text="Logged in as: "+name,relief="raised",bg='#0F1123',fg='white',anchor='center',justify='center')
    label1.pack(side="top")
    img1=tk.PhotoImage(file="credit1.png")
    img11=img1.subsample(2,2)
    img2=tk.PhotoImage(file="debit1.png")
    img22=img2.subsample(2,2)
    img3=tk.PhotoImage(file="checkbalance.png")
    img33=img3.subsample(2,2)
    img4=tk.PhotoImage(file="transactions1.png")
    img44=img4.subsample(2,2)
    img5=tk.PhotoImage(file="logout1.png")
    img55=img5.subsample(2,2)
    b1=tk.Button(image=img11,command=lambda: Cr_Amt(accnt,name))
    b1.image=img11
    b2=tk.Button(image=img22,command=lambda: De_Amt(accnt,name))
    b2.image=img22
    b3=tk.Button(image=img33,command=lambda: disp_bal(accnt))
    b3.image=img33
    b4=tk.Button(image=img44,command=lambda: disp_tr_hist(accnt))
    b4.image=img44
    b5=tk.Button(image=img55,command=lambda: logout(rootwn))
    b5.image=img55

    b1.place(x=200,y=200)
    b2.place(x=200,y=350)
    b3.place(x=1000,y=200)
    b4.place(x=1000,y=350)
    b5.place(x=650,y=600)

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
    try:
        fpin=open(num+".txt",'r')
    except FileNotFoundError:
        messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return 

def home_return(master):
    master.destroy()
    Main_Menu()

def write(master,name,oc,pin):
	
    if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 

    f1=open("Accnt_Record.txt",'r')
    accnt_no=int(f1.readline())
    accnt_no+=1
    f1.close()

    f1=open("Accnt_Record.txt",'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no)+".txt","w")
    fdet.write(pin+"\n")
    fdet.write(oc+"\n")
    fdet.write(str(accnt_no)+"\n")
    fdet.write(name+"\n")
    fdet.close()

    frec=open(str(accnt_no)+"-rec.txt",'w')
    frec.write("Date                             Credit            Debit             Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"         "+oc+"              "+oc+"\n")
    frec.close()
    
    messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
    master.destroy()
    return

def crdt_write(master,amt,accnt,name):
    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 

    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    amti=int(amt)
    cb=amti+camt
    fdet=open(accnt+".txt",'w')
    fdet.write(pin)
    fdet.write(str(cb)+"\n")
    fdet.write(accnt+"\n")
    fdet.write(name+"\n")
    fdet.close()
    frec=open(str(accnt)+"-rec.txt",'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
    master.destroy()
    return

def debit_write(master,amt,accnt,name):

    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 
                
    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    fdet.close()
    if(int(amt)>camt):
        messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
    else:
        amti=int(amt)
        cb=camt-amti
        fdet=open(accnt+".txt",'w')
        fdet.write(pin)
        fdet.write(str(cb)+"\n")
        fdet.write(accnt+"\n")
        fdet.write(name+"\n")
        fdet.close()
        frec=open(str(accnt)+"-rec.txt",'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
        master.destroy()
        return

def Cr_Amt(accnt,name):
    creditwn=tk.Tk()
    creditwn.geometry("600x300")
    creditwn.title("Credit Amount")
    creditwn.configure(bg="#0F1123")
    fr1=tk.Frame(creditwn,bg="blue")
    l_title=tk.Message(creditwn,text="Online Banking System",relief='raised',width=2000,padx=600,pady=0,fg='white',bg='#0F1123',justify='center',font=("Arial","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
    e1=tk.Entry(creditwn,relief="raised")
    l1.pack(side="top")
    e1.pack(side="top")
    b=tk.Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
    b.pack(side="top")
    creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
    debitwn=tk.Tk()
    debitwn.geometry("600x300")
    debitwn.title("Debit Amount")	
    debitwn.configure(bg="#0F1123")
    fr1=tk.Frame(debitwn,bg="blue")
    l_title=tk.Message(debitwn,text="Online Banking System",relief='raised',width=2000,padx=600,pady=0,fg='white',bg='#0F1123',justify='center',font=("Arial","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(debitwn,relief="raised",text="Enter Amount to be debited: ")
    e1=tk.Entry(debitwn,relief="raised")
    l1.pack(side="top")
    e1.pack(side="top")
    b=tk.Button(debitwn,text="Debit",relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
    b.pack(side="top")
    debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




def disp_bal(accnt):
    fdet=open(accnt+".txt",'r')
    fdet.readline()
    bal=fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance",bal)




def disp_tr_hist(accnt):
    disp_wn=tk.Tk()
    disp_wn.geometry("900x600")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="#0F1123")
    fr1=tk.Frame(disp_wn,bg="blue")
    l_title=tk.Message(disp_wn,text="Online Banking System",relief='raised',width=2000,padx=600,pady=0,fg='white',bg='#0F1123',justify='center',font=("Arial","50","bold"))
    l_title.pack(side="top")
    fr1=tk.Frame(disp_wn)
    fr1.pack(side="top")
    l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="#0F1123",relief="raised")
    l1.pack(side="top")
    fr2=tk.Frame(disp_wn)
    fr2.pack(side="top")
    frec=open(accnt+"-rec.txt",'r')
    for line in frec:
        l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
        l.pack(side="top")
    b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
    b.pack(side="top")
    frec.close()
    

#main window
def Main_Menu():
    rootwn=tk.Tk()
    rootwn.geometry("1200x1000")
    rootwn.title("Online banking System")
    photo =tk.PhotoImage(file = "icon.png")
    rootwn.iconphoto(False, photo)
    rootwn.configure(background='#0F1123')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image=tk.PhotoImage(file='banking1.png')
    x=tk.Label(image=bg_image)
    x.place(y=-100)
    l_title=tk.Message(rootwn,text="Online Banking System",relief='raised',width=2000,padx=600,pady=0,fg='white',bg='#0F1123',justify='center',font=("Arial","50","bold"))
    l_title.pack(side='top')
    img1=tk.PhotoImage(file='createnew.png')
    img2=tk.PhotoImage(file='login1.png')
    img3=tk.PhotoImage(file='exit.png')
    img11=img1.subsample(2,2)
    img22=img2.subsample(2,2)
    img33=img3.subsample(2,2)

    b1=tk.Button(image=img11,command=Create)
    b1.image=img11
    b2=tk.Button(image=img22,command=lambda: log_in(rootwn))
    b2.image=img22
    b3=tk.Button(image=img33,command=rootwn.destroy)
    b3.image=img33
    b1.place(x=700,y=300)
    b2.place(x=730,y=400)
    b3.place(x=700,y=600)
    rootwn.mainloop()

    
Main_Menu()

