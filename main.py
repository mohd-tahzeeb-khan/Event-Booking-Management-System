import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
import PIL
import datetime
from PIL import Image, ImageTk
from datetime import date



class Daata_Decorations():
    def on_enter(self,e):
        self.btn.config(background='red', foreground= "white")

    def on_leave(self,e):
        self.btn.config(background= 'SystemButtonFace', foreground= 'black')

    def add_booking(self):
        add_book=tk.Tk()
        add_book.geometry('1200x800')
        add_book.title('BOOKING')
        
        frame_main=Frame(add_book,width=1180, height=780, bg='black').place(x=10,y=10)
        frame_heading=Frame(add_book, width=1170, height=70, bg='white').place(x=15, y=15)
        heading_label=Label(add_book, text='BOOKING',font=('arail',35, 'bold'),fg='blue', bg='white').pack(side=TOP,pady=20)
        main_frame=Frame(add_book, height=690, width=1170, bg='white', relief=SUNKEN).place(x=15, y=95)


        add_btn=Button(add_book, text='ADD BOOKING', width=15,     font=('arail', 10, 'bold'),height=2, fg='white', bg='green').place(x=320,y=730)
        add_btn=Button(add_book, text='RESET', width=15, height=2, font=('arail', 10, 'bold'),fg='Black', bg='yellow').place(x=520,y=730)
        add_btn=Button(add_book, text='CLOSE', width=15, height=2, font=('arail', 10, 'bold'),fg='white', bg='red', command=add_book.destroy).place(x=720,y=730)


        party_billno_label=Label(add_book, text='Bill No:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=110)
        party_bill_no_entry=Entry(add_book, width=25,state=DISABLED,font=(15), relief=SUNKEN, bd=3).place(x=250, y=110)
        party_name_label=Label(add_book, text='Party Name:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=150)
        party_bill_no_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3).place(x=250, y=150)

        party__label=Label(add_book, text='Phone No:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=190)
        party_bill_no_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3).place(x=250, y=190)

        party_label=Label(add_book, text='Alternative Phone no:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=230)
        party_bill_no_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3).place(x=250, y=230)

        party_label=Label(add_book, text='Booking for Date:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=270)
        party_bill_no_entry=Entry(add_book, width=25, relief=SUNKEN, font=(15),bd=3).place(x=250, y=270)

        party_label=Label(add_book, text='Person:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=310)
        party_bill_no_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3).place(x=250, y=310)

        party_label=Label(add_book, text='Advance:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=350)
        party_bill_no_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3).place(x=250, y=350)



        lawn_label=Label(add_book, text='Lawn Rent:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=110)
        lawn_decoration_label=Label(add_book, text='Lawn Decoration:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=150)
        gate_label=Label(add_book, text='Gate+Stage:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=190)
        watchman_label=Label(add_book, text='Watchman:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=230)
        cleaning_name_label=Label(add_book, text='Cleaning Charges:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=270)
        water_label=Label(add_book, text='Water Charges:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=310)
        electric__label=Label(add_book, text='Electric Charges:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=350)
        #party_label=Label(add_book, text=':', bg='White', font=('arail', 12, 'bold')).place(x=50, y=140)

        #party_label=Label(add_book, text=':', bg='White', font=('arail', 12, 'bold')).place(x=50, y=140)



        #btn_frame=Frame(add_book, height=100, width=500, bg='black', relief=RAISED).pack(x=300, y=650)
        #btn_frame=Frame(add_book, height=90, width=500, bg='white', relief=RIDGE, bd=2).pack(side=BOTTOM)





        add_book.mainloop()
    def Cancel_booking(self):
        cancel_book=tk.Tk()
        cancel_book.geometry('800x800')
        cancel_book.title('CANCELLING')
        cancel_book.mainloop()
    def working_staff(self):
        working_staff=tk.Tk()
        working_staff.geometry('800x800')
        working_staff.title('STAFF')
        working_staff.mainloop()
    def credit(self):
        credit=tk.Tk()
        credit.geometry('800x800')
        credit.title('CREDIT')
        credit.mainloop()
    def setting(self):
        setting_win=tk.Tk()
        setting_win.geometry('800x800')
        setting_win.title('SETTING')
        setting_win.mainloop()
   
    def __init__(self):
        
        today= date.today()
        events={'2021-10-28':('London','Program'),\
                '2021-10-15':('Paris','Program'),\
                '2018-07-30':('New York','Program')}
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
        self.cal=Calendar(self.main_window, selectmode='none')
        
        self.cal.pack(side=LEFT,padx=20, pady=20, ipady=130)
        for k in events.keys():
            date1=datetime.datetime.strptime(k,"%Y-%m-%d").date()
            self.cal.calevent_create(date1, events[k][0], events[k][1])
        self.cal.tag_config('Program', background='green', foreground='white')
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
        self.button=Button(self.main_window, text='Working Stuff',bg='orange',fg='Black',height=2, width=15,font=('arial', 10, 'bold'),command= self.working_staff)
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