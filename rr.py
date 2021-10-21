from tkcalendar import Calendar

from tkinter import ttk
import tkinter as tk

def create_calcular(top, datess):
    cal=Calendar(top, selectmode='none')
    date=cal.datetime.today()+cal.timedelta(int(datess))
    cal.calevent_create(date, 'hello', 'message')
    cal.calevent_create(date, 'reminder 2', 'remainder')
    cal.calevent_create(date+cal.timedelta(days=0), 'reminder 1', 'reminder')
    cal.calevent_create(date+cal.timedelta(days=0),'Message', 'message')
    cal.tag_config('reminder', background='red', foreground='yellow')
    cal.pack(fill='both', expand='True')
    ttk.Label(top, text="Hover over the events.").pack()
root=tk.Tk()
size='500x300'
root.geometry(size)
create_calcular(root, '23')
root.mainloop()
