import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
import PIL
from PIL import Image, ImageTk
from datetime import date



class Daata_Decorations():
    def on_enter(self,e):
        self.btn.config(background='red3', foreground= "white")

    def on_leave(self,e):
        self.btn.config(background= 'SystemButtonFace', foreground= 'black')

    def add_booking(self):
        add_book=tk.Tk()
        add_book.geometry('800x800')
        add_book.mainloop()
    def Cancel_booking(self):
        cancel_book=tk.Tk()
        cancel_book.geometry('800x800')
        cancel_book.mainloop()
    def working_stuff(self):
        working_stuff=tk.Tk()
        working_stuff.geometry('800x800')
        working_stuff.mainloop()
    def credit(self):
        credit=tk.Tk()
        credit.geometry('800x800')
        credit.mainloop()
    def setting(self):
        setting_win=tk.Tk()
        setting_win.geometry('800x800')
        setting_win.mainloop()
   
    def __init__(self):
        

        self.main_window=Tk()
        self.dd=StringVar()
        self.mm=StringVar()
        self.yy=StringVar()
        self.show_result=StringVar()

        #self.main_window.overrideredirect(True)
       
        #main_window.wm_state('iconic')

        width1= self.main_window.winfo_screenwidth()#responsive window
        height1=self.main_window.winfo_screenheight()
        self.main_window.geometry('%dx%d'%(width1, height1))
        self.main_window.title('Daata Decorations & Bichayat')
        self.main_window.iconbitmap('food.ico')
        frame1=Frame(self.main_window, width=width1, height=100, bg='blue').place(x=1,y=10)
        #LBS=Label(self.main_window, text='Developed by: Mohd Tahzeeb Khan, on-date:01/11/2021').place(x=100, y=0)
        lbs=Label(self.main_window, text='DAWAT LAWN & GARDEN', font=('courier', 60, 'bold'), bg='blue', fg='White').place(x=300, y=10)
        #photo=PhotoImage(file='close.png')
        #image1 = Image.open("close.png")
        #resize_image=image1.resize((20,22), Image.ANTIALIAS)
        #test=ImageTk.PhotoImage(resize_image)
        #self.btn=Button(self.main_window, text='Exit',image=test,bg='White',fg='red', font=50,command=self.main_window.destroy)
        #self.btn.place(x=1500,y=0)
        #self.btn.bind('<Enter>', self.on_enter)
        #self.btn.bind('<Leave>', self.on_leave)
        inquiry_frame=Frame(self.main_window, width=490, height=640, bg='white',bd=8, relief= RIDGE).place(x=2, y=130)
        inquirylbl_frame=Frame(self.main_window, width=450, height=56, bg='yellow', relief=RIDGE, bd=3).place(x=20, y=140)
        inquiry_label=Label(self. main_window, text='BOOKING CALENDAR',font=('arail', 25, 'bold'), bg='Yellow').place(x=60, y=145)
        self.cal=Calendar(self.main_window, selectmode='day')
        
        self.cal.pack(side=LEFT,padx=20, pady=20, ipady=130)
        lbs=Label(self.main_window, text='Date:', bg='White', font=('arial', 15, 'bold')).place(x=20, y=660)
        self.dd_entry=Entry(self.main_window, width=3,textvariable=self.dd,bg='grey', font=('arial', 15, 'bold'))
        self.dd_entry.place(x=80, y=665)
        lbs=Label(self.main_window, text='/', bg='White', font=('arial', 20, 'bold')).place(x=125, y=660)
        self.mm_entry=Entry(self.main_window,width=3, textvariable=self.mm,bg='grey', font=('arial', 15, 'bold'))
        self.mm_entry.place(x=150, y=665)
        lbs=Label(self.main_window, text='/', bg='White', font=('arial', 20, 'bold')).place(x=195, y=660)
        self.yy_entry=Entry(self.main_window, textvariable=self.yy, width=7, bg='grey', font=('arial', 15, 'bold'))
        self.yy_entry.place(x=220, y=665)
        self.result_entry=Entry(self.main_window, textvariable=self.show_result, width=12, bg='White',relief=RAISED, font=('arial', 15, 'bold'))
        self.result_entry.place(x=330, y=665)
        self.ddbutton=Button(self.main_window, text='SEARCH',bg='green',fg='white',font=('arial', 10, 'bold'))
        self.ddbutton.place(x=50, y=715)
        self.ddbutton=Button(self.main_window, text='CLEAR',bg='yellow',fg='black',font=('arial', 10, 'bold'))
        self.ddbutton.place(x=200, y=715)
        button_frame=Frame(self.main_window, width=710, height=70, bg='white',bd=8, relief= RIDGE).place(x=500, y=130)
        self.button=Button(self.main_window, text='Add Booking',bg='orange',fg='black',height=2, width=15,font=('arial', 10, 'bold'),command=self.add_booking)
        self.button.place(x=510, y=142)
        self.button=Button(self.main_window, text='Cancel Booking',bg='orange',height=2, width=15,fg='black',font=('arial', 10, 'bold'),command=self.Cancel_booking)
        self.button.place(x=650, y=142)
        self.button=Button(self.main_window, text='Working Stuff',bg='orange',fg='Black',height=2, width=15,font=('arial', 10, 'bold'),command= self.working_stuff)
        self.button.place(x=790, y=142)
        self.button=Button(self.main_window, text='Credit',bg='orange',height=2, width=15,fg='black',font=('arial', 10, 'bold'),command=self.credit)
        self.button.place(x=930, y=142)
        self.button=Button(self.main_window, text='Setting',bg='orange',fg='black',height=2, width=15,font=('arial', 10, 'bold'),command= self.setting)
        self.button.place(x=1070, y=142)
        about_frame=Frame(self.main_window, width=300, height=70, bg='white',bd=8, relief= RIDGE).place(x=1220, y=130)
        self.button=Button(self.main_window, text='Developer',bg='orange',fg='black',height=2, width=16,font=('arial', 10, 'bold'))
        self.button.place(x=1230, y=142)
        self.button=Button(self.main_window, text='Exit',bg='red',fg='white',height=2, width=15,command=self.main_window.destroy,font=('arial', 10, 'bold'))
        self.button.place(x=1380, y=142)

        treeview_frame=Frame(self.main_window, width=1020, height=570, bg='white',bd=8, relief= RIDGE).place(x=500, y=200)
        #frame2=Frame(self.maipn_window, width=500, height=100, bg='blue').place(x=1,y=30)
        lbs1=Label(self.main_window, text='DAATA BICHAYAT & DECORATION WORKS', font=('courier', 25, 'bold'), bg='blue', fg='White').place(x=450, y=780)
        self.main_window.resizable(0,0)
        self.main_window.mainloop()

if __name__ == "__main__":
    dawat_Lawn=Daata_Decorations()