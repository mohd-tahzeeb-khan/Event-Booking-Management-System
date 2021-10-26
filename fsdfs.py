import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkcalendar
from tkcalendar import Calendar, DateEntry
import datetime
from datetime import date
  
  
# Returns the current local date
today= date.today()

root = tk.Tk()

events={'2021-10-28':('London',' meeting'),\
    '2021-10-15':('Paris','meeting'),\
    '2018-07-30':('New York','meeting')}

cal = Calendar(root, selectmode='none',year=today.year, month=today.month,day=today.day)

for k in events.keys():
    date=datetime.datetime.strptime(k,"%Y-%m-%d").date()
    cal.calevent_create(date, events[k][0], events[k][1])

#cal.tag_config('ggg', background='red', foreground='white')
cal.tag_config('meeting', background='green', foreground='white')
cal.pack(fill="both", expand=True)

root.mainloop()