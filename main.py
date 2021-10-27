import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import PIL
import datetime
from PIL import Image, ImageTk
from datetime import date



class Daata_Decorations():
    
    def on_enter(self,e):
        self.btn.config(background='red', foreground= "white")

    def on_leave(self,e):
        self.btn.config(background= 'SystemButtonFace', foreground= 'black')
    def reset(self):
        party_person_entry.delete(0,END)
        party_name_entry.delete(0, END)
        party_phone_entry.delete(0, END)
        party_alterphone_entry.delete(0, END)
        Advance_entry.delete(0, END)
        Address_entry.delete(0, END)
        
    def total(self):
        a='24000'
        return a

    def add_booking(self):
        global party_person_entry, party_name_entry, party_phone_entry, party_alterphone_entry, Advance_entry,Address_entry
        today= date.today()
        add_book=tk.Tk()
        add_book.geometry('1200x800')
        add_book.title('BOOKING')
        self.guard=StringVar(add_book)
        self.no_guard=StringVar(add_book)
        self.cleaning_charges=StringVar(add_book)
        self.water__charges=StringVar(add_book)
        self.electric_charges=StringVar(add_book)
        self.lawn_rent=StringVar(add_book)
        self.stage=StringVar(add_book)
        self.decoration=StringVar(add_book)
        self.bill=StringVar(add_book)
        self.bill.set('DL975')
        self.grandtotal=StringVar(add_book)
       



        frame_main=Frame(add_book,width=1180, height=780, bg='black').place(x=10,y=10)
        frame_heading=Frame(add_book, width=1170, height=70, bg='white').place(x=15, y=15)
        heading_label=Label(add_book, text='BOOKING',font=('arail',35, 'bold'),fg='blue', bg='white').pack(side=TOP,pady=20)
        main_frame=Frame(add_book, height=690, width=1170, bg='white', relief=SUNKEN).place(x=15, y=95)


        


        party_billno_label=Label(add_book, text='Bill No:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=110)
        party_bill_no_entry=Entry(add_book, width=25,state=DISABLED,textvariable=self.bill,font=(15), relief=SUNKEN, bd=3)
        party_bill_no_entry.place(x=250, y=110)

        party_name_label=Label(add_book, text='Party Name:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=150)
        party_name_entry=Entry(add_book, width=25,justify='center', relief=SUNKEN,font=(15), bd=3)
        party_name_entry.place(x=250, y=150)

        party_phone_label=Label(add_book, text='Phone No:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=190)
        party_phone_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        party_phone_entry.place(x=250, y=190)

        party_alterphone_label=Label(add_book, text='Alternative Phone no:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=230)
        party_alterphone_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        party_alterphone_entry.place(x=250, y=230)

        party_label=Label(add_book, text='Occasion:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=270)
        event_choosen = ttk.Combobox(add_book,font=(12), width=23)
        event_choosen['values'] = ('MARRIAGE','HALDI & SANGEET','ENGAGEMENT', 'ANNIERSARY', 'BIRTHDAY', 'FAMILY GET-TOGETHER','OFFICE EVENT', 'FAREWELL', 'OTHER')
        event_choosen.place(x=250, y=270)
        event_choosen.current(0)

        party_label=Label(add_book, text='Person:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=310)
        party_person_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        party_person_entry.place(x=250, y=310)

        Advance_label=Label(add_book, text='Advance:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=350)
        Advance_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        Advance_entry.place(x=250, y=350)

        Date_of_booking_label=Label(add_book, text='Booking For Date:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=390)
        #Date_of_booking_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15),state=DISABLED, bd=3).place(x=250, y=390)
        #cal=Calendar(add_book, selectmode='day', weekendbackground='white', showweeknumbers=False, weekendforeground='black')
        cal=DateEntry(add_book,selectmode='day',year=today.year,date_pattern='dd/MM/yyyy',weekendbackground='white', month=today.month,showweeknumbers=False, weekendforeground='black', day=today.day,width=24, font=(15))
        cal.place(x=250, y=390)
        Address_label=Label(add_book, text='Address:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=430)
        Address_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        Address_entry.place(x=250, y=430)

        self.guard.set(300)
        self.no_guard.set(1)
        self.cleaning_charges.set(300)
        self.water__charges.set(100)
        self.electric_charges.set(600)
        self.lawn_rent.set(12000)
        self.decoration.set(5200)
        self.stage.set(1500)
        



        self.lawn_label=Label(add_book, text='Lawn Rent:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=110)
        self.lawn_rent_entry=Entry(add_book, textvariable=self.lawn_rent, width=25, relief=SUNKEN, font=(15), bd=3)
        self.lawn_rent_entry.place(x=800, y=110)
        self.lawn_decoration_label=Label(add_book, text='Lawn Decoration:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=150)
        self.decoration_entry=Entry(add_book, textvariable=self.decoration, width=25, relief=SUNKEN, font=(15), bd=3)
        self.decoration_entry.place(x=800, y=150)
        self.gate_label=Label(add_book, text='Gate+Stage:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=190)
        self.gate_entry=Entry(add_book, textvariable=self.stage,width=25, relief=SUNKEN, font=(15), bd=3)
        self.gate_entry.place(x=800, y=190)
        self.watchman_label=Label(add_book, text='Watchman:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=230)
        
        self.watchman__charges_spin = Spinbox(add_book, from_ = 0, to =1000, increment=50,textvariable=self.guard,  width=5,font=(15))
        self.watchman__charges_spin.place(x=800, y=230)
        self.watchman_no_charges_spin = Spinbox(add_book, from_ = 0, to =9, textvariable=self.no_guard,  width=2,font=(15))
        self.watchman_no_charges_spin.place(x=990, y=230)
        
        self.cleaning_name_label=Label(add_book, text='Per Guard,', bg='White', font=('arail', 12, 'bold')).place(x=890, y=230)
        self.cleaning_name_label=Label(add_book, text='Guard', bg='White', font=('arail', 12, 'bold')).place(x=1050, y=230)
        self.cleaning_name_label=Label(add_book, text='Cleaning Charges:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=270)
        self.cleaning__charges_spin = Spinbox(add_book,textvariable=self.cleaning_charges, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.cleaning__charges_spin.place(x=800, y=270)
        self.cleaning_name_label=Label(add_book, text='Per Event Charges', bg='White', font=('arail', 12, 'bold')).place(x=890, y=270)

        self.water_label=Label(add_book, text='Water Charges:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=310)
        self.water__charges_spin = Spinbox(add_book, from_ = 0,textvariable=self.water__charges, to =9999, increment=50, width=5, font=(15))
        self.water__charges_spin.place(x=800, y=310)
        self.cleaning_name_label=Label(add_book, text='Per Event Charges', bg='White', font=('arail', 12, 'bold')).place(x=890, y=310)
        self.electric__label=Label(add_book, text='Electric Charges:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=350)
        self.electric__charges_spin = Spinbox(add_book, from_ = 0, textvariable=self.electric_charges, to =9999, increment=50,  width=5,font=(15))
        self.cleaning_name_label=Label(add_book, text='Per Event Charges', bg='White', font=('arail', 12, 'bold')).place(x=890, y=350)
        self.electric__charges_spin.place(x=800, y=350)
        
        
        self.cal_total_label=Label(add_book, text='TOTAL:', bg='White', font=('arail', 16, 'bold')).place(x=600, y=500)
        self.grand_total_entry=Entry(add_book, width=15,textvariable=self.grandtotal, state=DISABLED,relief=SUNKEN,font=(16), bd=3)
        self.grand_total_entry.place(x=800, y=500)
    


        self.add_btn=Button(add_book, text='ADD BOOKING', width=15,     font=('arail', 10, 'bold'),height=2, fg='white', bg='green').place(x=320,y=730)
        self.add_btn=Button(add_book, text='RESET', width=15, height=2, font=('arail', 10, 'bold'),fg='Black', bg='yellow', command=self.reset).place(x=520,y=730)
        self.add_btn=Button(add_book, text='CLOSE', width=15, height=2, font=('arail', 10, 'bold'),fg='white', bg='red', command=add_book.destroy).place(x=720,y=730)
        self.cal_button=Button(add_book, text='Calculate', bg='Green', fg='White', font=(15), width=15, command=self.total).place(x=990, y=493)


        add_book.mainloop()
    def total(self):
        self.rent=int(self.lawn_rent_entry.get())
        self.decoration=int(self.decoration_entry.get())
        self.stage=int(self.gate_entry.get())
        self.watchmen=int(self.watchman__charges_spin.get())
        self.no_guard=int(self.watchman_no_charges_spin.get())
        self.clean=int(self.cleaning__charges_spin.get())
        self.water=int(self.water__charges_spin.get())
        self.electric=int(self.electric__charges_spin.get())
        self.a=int(self.watchmen)
        self.b=int(self.no_guard)
        self.c=self.a*self.b
        
        self.grandtotal.set(self.rent+self.decoration+self.stage+self.c+self.clean+self.water+self.electric)






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
        self.cal=Calendar(self.main_window, selectmode='none',showweeknumbers=False,weekendbackground='white', weekendforeground='black')
        
        self.cal.pack(side=LEFT,padx=20, ipadx=10,pady=20, ipady=130)
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