
from tkinter import *
import math
import cmath

root=Tk()
root.title("this is your calculator")
root.geometry('300x300')
root.resizable(0,0)


#----------------------------------------------


menubar=Menu(root)
filebar=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=filebar)
filebar.add_command(label="Standard")
filebar.add_separator()
filebar.add_command(label="Scientific")
filebar.add_separator()
filebar.add_command(label="Exit")
root.config(menu=menubar)

#-----------------------------------------------

lb1=Label(root)
lb1.pack(expand=True, fill="both")

x= StringVar()
e=Entry(lb1,bg="lightgreen",font=("Times",14),textvariable=x)
e.pack(expand=True, fill='both')
ex=""
op=""
v1=0
op2="deg"
def numbers(var):
    global v
    global ex
    ex=ex+str(var)
    x.set(ex)
    v=0

def sci(var1):
    global v,v1,y1
    global ex
    global op,op2
    op = var1
    if op=="pow()":
        y1=ex
        y=var1[0:(len(var1)-1)]+ex
        x.set(y)
        ex=""
        v1=1
        v=1
    elif op=="π":
        y=(math.pi)
        x.set(y)
    else:
        op=var1
        var1=str(var1)
        y=var1[0:(len(var1)-1)]+ex+var1[len(var1)-1:]
        x.set(y)
        v=1

def conversion(var2):
    global op2
    op2=var2

def clear():
    global v
    global ex
    ex=""
    x.set(ex)
    v=0

def equal():
    global v,v1,y1
    global ex
    global op,op2
    if op2=="rad":
        if op == "sin()" and v == 1:
            y=(float(ex)*180)/math.pi
            result = str(math.sin(math.radians(y)))
        elif op == "cos()" and v == 1:
            y = (float(ex) * 180) / math.pi
            result = str(math.cos(math.radians(y)))
        elif op == "tan()" and v == 1:
            y = (float(ex) * 180) / math.pi
            result = str(math.tan(math.radians(y)))
        else:
            result = str(eval(ex))
    else:
        if op == "sin()" and v == 1:
            result = str(math.sin(math.radians(float(ex))))
        elif op == "cos()" and v == 1:
            result = str(math.cos(math.radians(float(ex))))
        elif op == "tan()" and v == 1:
            result = str(math.tan(math.radians(float(ex))))
        elif op == "exp()" and v == 1:
            result = str(math.exp(float(ex)))
        elif op == "log()" and v == 1:
            result = str(math.log(float(ex)))
        elif op == "Sqrt()" and v == 1:
            try:
                result = str(math.sqrt(float(ex)))
            except:
                result = str(cmath.sqrt(float(ex)))
        elif op == "inverse()" and v == 1:
            result = str(1 / (float(ex)))
        elif op == "pow()" or v1 == 1:
            result = str(math.pow(float(y1), float(ex)))
        else:
            result = str(eval(ex))


    x.set(result)
    ex=str(result)
    v=0
    op=""

#-------------------------------------------------
butframe1= Frame(root)
butframe1.pack(expand=True, fill='both')
butframe2= Frame(root)
butframe2.pack(expand=True, fill='both')
butframe3= Frame(root)
butframe3.pack(expand=True, fill='both')
butframe4= Frame(root)
butframe4.pack(expand=True, fill='both')





#------------------------------------------------------------------
butt1=Button(butframe1,text="7",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0,command=(lambda:numbers(7)))
butt1.pack(side=LEFT,expand=True,fill="both")

butt2=Button(butframe1,text="8",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(8)))
butt2.pack(side=LEFT,expand=True,fill='both')

butt3=Button(butframe1,text="9",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(9)))
butt3.pack(side=LEFT,expand=True,fill='both')

butt4=Button(butframe1,text="+",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers("+")))
butt4.pack(side=LEFT,expand=True,fill='both')

buttrad=Button(butframe1,text="rad",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:conversion("rad")))
buttrad.pack(side=LEFT,expand=True,fill='both')

butt5=Button(butframe1,text="sin() ",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("sin()")))
butt5.pack(side=LEFT,expand=True,fill='both')

butt6=Button(butframe1,text="log()",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("log()")))
butt6.pack(side=LEFT,expand=True,fill='both')

#-------------------------------------------------------------

butt1=Button(butframe2,text="4",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(4)))
butt1.pack(side=LEFT,expand=True,fill='both')

butt2=Button(butframe2,text="5",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(5)))
butt2.pack(side=LEFT,expand=True,fill='both')

butt3=Button(butframe2,text="6",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(6)))
butt3.pack(side=LEFT,expand=True,fill='both')

butt4=Button(butframe2,text="-",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers("-")))
butt4.pack(side=LEFT,expand=True,fill='both')

buttdeg=Button(butframe2,text="deg",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:conversion("deg")))
buttdeg.pack(side=LEFT,expand=True,fill='both')

butt5=Button(butframe2,text="cos()",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("cos()")))
butt5.pack(side=LEFT,expand=True,fill='both')

butt6=Button(butframe2,text="1/x",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("inverse()")))
butt6.pack(side=LEFT,expand=True,fill='both')

#-------------------------------------------------------------------
butt1=Button(butframe3,text="1",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(1)))
butt1.pack(side=LEFT,expand=True,fill='both')

butt2=Button(butframe3,text="2",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(2)))
butt2.pack(side=LEFT,expand=True,fill='both')

butt3=Button(butframe3,text="3",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(3)))
butt3.pack(side=LEFT,expand=True,fill='both')

butt4=Button(butframe3,text="/",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers("/")))
butt4.pack(side=LEFT,expand=True,fill='both')

buttno=Button(butframe3,text="π",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("π")))
buttno.pack(side=LEFT,expand=True,fill='both')

butt5=Button(butframe3,text="tan()",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("tan()")))
butt5.pack(side=LEFT,expand=True,fill='both')

butt6=Button(butframe3,text="x^y",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("pow()")))
butt6.pack(side=LEFT,expand=True,fill='both')


#---------------------------------------------------

butt1=Button(butframe4,text="0",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(0)))
butt1.pack(side=LEFT,expand=True,fill='both')

butt2=Button(butframe4,text="c",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0,command=clear)
butt2.pack(side=LEFT,expand=True,fill='both')

butt5=Button(butframe4,text=".",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers(".")))
butt5.pack(side=LEFT,expand=True,fill='both')

butt3=Button(butframe4,text="*",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:numbers("*")))
butt3.pack(side=LEFT,expand=True,fill='both')

butt4=Button(butframe4,text="=",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0,command=equal)
butt4.pack(side=LEFT,expand=True,fill='both')

buttYes=Button(butframe4,text="exp",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0,command=(lambda:sci("exp()")))
buttYes.pack(side=LEFT,expand=True,fill='both')



butt6=Button(butframe4,text="Sqrt()",font=("Times",12),activebackground="lightblue",relief=GROOVE,border=0, command=(lambda:sci("Sqrt()")))
butt6.pack(side=LEFT,expand=True,fill='both')

root.mainloop()

