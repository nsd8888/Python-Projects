from tkinter import *
from tkinter import ttk

from tkinter import messagebox

root=Tk()
root.title("Currancy Converter")
root.geometry('500x500')


def Lock():
    if not home_entry.get() or not conversion_entry.get() or not currancy_rate_entry.get():
        messagebox.showwarning('Warning', 'fill all entries')
    else:
        home_entry.config(state='disable')
        conversion_entry.config(state='disable')
        currancy_rate_entry.config(state='disable')
        book.tab(1, state='normal')

        home1.config(text="Amount of {} convert to {}".format(home_entry.get(),conversion_entry.get()))
        home2.config(text='Equals to as many {}'.format(conversion_entry.get()))

        home1_button1.config(text='Convert {} to {}'.format(home_entry.get(),conversion_entry.get()))

        home1_label1.config(text='Enter the {} Amount'.format(home_entry.get()))
        home2_label.config(text='Amount of {}'.format(conversion_entry.get()))

def Convert():
    home2_label_entry.delete(0,END)
    x=float(currancy_rate_entry.get())*float(home1_label_entry.get())
    home2_label_entry.insert(0,x)


def Unlock():
    home_entry.config(state='normal')
    conversion_entry.config(state='normal')
    currancy_rate_entry.config(state='normal')
    book.tab(1, state='disable')


def Clear():
    home1_label_entry.delete(0,END)
    home2_label_entry.delete(0,END)


book=ttk.Notebook(root)
book.pack(pady=5)

currancy_frame= Frame(book,width=480,height=480)
conversion_frame= Frame(book,width=480,height=480)
currancy_frame.pack(fill='both',expand=1)
conversion_frame.pack(fill='both',expand=1)

book.add(currancy_frame,text='currancies')
book.add(conversion_frame,text='conversions')

home= LabelFrame(currancy_frame,text='your Home Currancy')
home.pack(pady=10)
home_entry=Entry(home,font=('Helvettica',22))
home_entry.pack(pady=10,padx=10)

conversion= LabelFrame(currancy_frame,text='Conversion Currancy')
conversion.pack(pady=20)

conversion_label=Label(conversion,text="Home currancy to")
conversion_label.pack(pady=5)

conversion_entry=Entry(conversion,font=('Helvettica',22))
conversion_entry.pack(pady=10,padx=10)

currancy_rate_label=Label(conversion,text="currancy conversion rate")
currancy_rate_label.pack(pady=5)

currancy_rate_entry=Entry(conversion,font=('Helvettica',22))
currancy_rate_entry.pack(pady=10,padx=10)

button_frame=Frame(currancy_frame)
button_frame.pack(pady=10,padx=10)

butt1=Button(button_frame,text="lock",command=Lock)
butt1.grid(row=0,column=0,padx=20)

butt2=Button(button_frame,text="Unlock",command=Unlock)
butt2.grid(row=0,column=1,padx=20)


home1=LabelFrame(conversion_frame,text='Amount to convert')
home1.pack(pady=10)
home1_label1=Label(home1,text="Enter the amount for conversion")
home1_label1.pack(pady=10)

home1_label_entry=Entry(home1,font=('Helvettica',22))
home1_label_entry.pack(pady=10,padx=10)

home1_button=Label(conversion_frame)
home1_button.pack(pady=5)

home1_button1=Button(home1_button,text='Convert',command=Convert)
home1_button1.grid(row=0,column=0)

home2= LabelFrame(conversion_frame,text="The Total Amount")
home2.pack(pady=10)
home2_label=Label(home2,text='Total Amount')
home2_label.pack(pady=5)
home2_label_entry=Entry(home2,font=('Helvettica',22))
home2_label_entry.pack(pady=10,padx=10)

home2_button=Label(conversion_frame)
home2_button.pack(pady=5)
home2_button1=Button(home2_button,text='Clear',command=Clear)
home2_button1.grid(row=0,column=0)

#disable 2nd tab
book.tab(1,state='disable')

root.mainloop()