import requests,json
from tkinter import *
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
import sys

import numpy as np
root=Tk()
root.title("Currancy Converter APP")
root.geometry('500x300')

var1=StringVar(root)
var2=StringVar(root)

var1.set('currancy')
var2.set('currancy')

def RealtimeCurrancyConversion():
    converted_amount.config(state='normal')
    my_api_key = '949Q765OQ6UQ9BGB'
    from_curr = var1.get()
    to_curr = var2.get()
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency=" + from_curr + "&to_currency=" + to_curr + "&apikey=" + my_api_key
    response = requests.get(main_url)
    result = response.json()
    try:
        converted_amount.delete(0,END)
        re = result['Realtime Currency Exchange Rate']
        exchange_rate = re['5. Exchange Rate']
        amount = amount_entry.get()
        try:
            Tot_amount = round(float(amount) * float(exchange_rate), 3)
        except UnboundLocalError:
            messagebox.showwarning('Warning', 'Plz fill all respective Entries entries')
    except KeyError:
        messagebox.showwarning('Warning', 'Plz fill all respective Entries entries')
    except ValueError:
        messagebox.showwarning('Warning', 'Dont Enter alphabets/Special Symbol/Alpha-Numeric values')
    else:
        converted_amount.insert(0, str(Tot_amount))


def clear():
    amount_entry.delete(0,END)
    converted_amount.delete(0,END)
    converted_amount.config(state='disable')

def Exit():
    messagebox.showwarning('Warning', 'Thank You For Using This App')
    sys.exit()

book=ttk.Notebook(root)
book.pack(pady=5)

curr_frame=Frame(book,width=480,height=480,bg='light blue')
curr_frame.pack(fill='both',expand=1)
book.add(curr_frame,text='Welcome to Real Time Currancy Conversion')


label1=Label(curr_frame, text='From Currancy',font=('Helvettica',18),bg='light green')
label1.grid(row=1,column=0,pady=5)

label2=Label(curr_frame, text='To Currancy',font=('Helvettica',18),bg='light green')
label2.grid(row=2,column=0,pady=5)

label3=Label(curr_frame, text='Amount',font=('Helvettica',18),bg='light green')
label3.grid(row=3,column=0,pady=5)

label4=Label(curr_frame, text='Converted Amount',font=('Helvettica',18),bg='light green')
label4.grid(row=4,column=0,pady=5)

amount_entry=Entry(curr_frame,font=('Helvettica',18),bg='light blue')
amount_entry.grid(row=3,column=1,pady=5)

converted_amount=Entry(curr_frame,font=('Helvettica',18),bg='light green')
converted_amount.grid(row=4,column=1,pady=5)

#df=pd.read_csv('physical_currency_list.csv')
lst=['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH', 'CNY', 'COP', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'ICP', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RUR', 'RWF', 'SAR', 'SBDf', 'SCR', 'SDG', 'SDR', 'SEK', 'SGD', 'SHIB', 'SHP', 'SLL', 'SOS', 'SRD', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VND', 'VUV', 'WBTC', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']

#for i,j in df.iterrows():
  #  lst.append(j[0])

from_currancy_option=OptionMenu(curr_frame,var1,*lst)
to_currancy_option=OptionMenu(curr_frame,var2,*lst)

from_currancy_option.config(width=10,font=('Helvettica',14))
to_currancy_option.config(width=10,font=('Helvettica',14))

from_currancy_option.grid(row=1,column=1)
to_currancy_option.grid(row=2,column=1)


converted_amount.config(state='disable')


butt1=Button(curr_frame,text='Convert',width=20,relief='groove',command=RealtimeCurrancyConversion)
butt1.grid(row=5,column=0,padx=5,pady=10)

butt2=Button(curr_frame,text='Clear',width=20,relief='groove',command=clear)
butt2.grid(row=5,column=1,padx=5,pady=10)


butt4=Button(curr_frame,width=20,text='exit',command=Exit)
butt4.grid(row=6,column=0)

root.mainloop()