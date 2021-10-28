import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import PIL
import datetime
from PIL import Image, ImageTk
from datetime import date
import requests
import time
from tkinter.scrolledtext import ScrolledText
 



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
        today= date.today()
        cancel_book.geometry('800x800')
        cancel_book.title('CANCELLING')
        back_frame=Frame(cancel_book, width=780, height=780, bg='black').place(x=10,y=10)
        main_frame=Frame(cancel_book, width=760, height=760, bg='grey').place(x=20,y=20)
        heading_frame=Frame(cancel_book, width=350, height=80, bg='White', relief=RAISED, bd=5).place(x=25,y=25)
        search_frame=Frame(cancel_book, width=395, height=80, bg='White', relief=RAISED, bd=5).place(x=380,y=25)
        bill_label=Label(cancel_book, text='Bill No:', bg='white', font=(20)).place(x=400,y=35)
        bill_entry=Entry(cancel_book, width=16,font=(25)).place(x=500, y=35)

        date_label=Label(cancel_book, text='Date:', bg='white', font=(20)).place(x=400,y=70)
        cal=DateEntry(cancel_book,selectmode='day',year=today.year,date_pattern='dd/MM/yyyy',weekendbackground='white', month=today.month,showweeknumbers=False, weekendforeground='black', day=today.day,width=14, font=(15))
        cal.place(x=500, y=70)

        #down_frame=Frame(cancel_book, width=460, height=150, bg='White', relief=RAISED, bd=5).place(x=20,y=20)
        label_heading=Label(cancel_book, text='Cancellation', bg='white',font=('arial', 30, 'bold')).place(x=70, y=40)
        down_frame=Frame(cancel_book, width=750, height=600, bg='White', relief=RAISED, bd=5).place(x=25,y=110)
        down_frame=Frame(cancel_book, width=750, height=60, bg='White', relief=RAISED, bd=5).place(x=25,y=710)

        reset_btn=Button(cancel_book, width=15, text='Cancel', font=(8)).place(x=35, y=720)
        reset_btn=Button(cancel_book, width=15, text='Exit',bg='red', font=(8),command=cancel_book.destroy).place(x=590, y=720)
        cancel_book.mainloop()


    def working_staff(self):
        working_staff=tk.Tk()
        working_staff.geometry('800x800')
        working_staff.title('STAFF')
        back_frame=Frame(working_staff, width=780, height=780, bg='Black').place(x=10, y=10)
        front_frame=Frame(working_staff, width=750, height=750).place(x=25, y=25)
        heading_frame=Frame(working_staff, width=730, height=100, bg='white', relief=RIDGE, bd=5).place(x=35, y=40)
        heading_label=Label(working_staff, text='WORKING STAFF', bg='white',font=('arail', 40, 'bold')).place(x=170, y=60)
        main_frame=Frame(working_staff, width=730, height=520, bg='white', relief=RIDGE, bd=5).place(x=35, y=145)
        btn_frame=Frame(working_staff, width=730, height=100, bg='white', relief=RIDGE, bd=5).place(x=35, y=670)
        add_btn=Button(working_staff, width=15, text='Add', font=(8)).place(x=50, y=700)
        delete_btn=Button(working_staff, width=15, text='Delete', font=(8)).place(x=330, y=700)
        #modify_btn=Button(working_staff, width=15, text='Modify', font=(8)).place(x=450, y=700)
        exit_btn=Button(working_staff, width=15, text='Exit',bg='red', font=(8),command=working_staff.destroy).place(x=570, y=700)
        working_staff.mainloop()
    def credit(self):
        credit=tk.Tk()
        credit.geometry('800x800')
        credit.title('CREDIT')
        credit.mainloop()
    def setting(self):
        setting_win=tk.Tk()
        setting_win.geometry('800x680')
        setting_win.title('SETTING')
        setting_win['bg']='black'
        lawn=StringVar(setting_win)
        decoration=StringVar(setting_win)
        gate=StringVar(setting_win)
        watchme=StringVar(setting_win)
        no=StringVar(setting_win)
        cleaning=StringVar(setting_win)
        electric=StringVar(setting_win)
        water=StringVar(setting_win)
        whatsapp=StringVar(setting_win)
        emialid=StringVar(setting_win)
        password=StringVar(setting_win)

        tc = ttk.Notebook(setting_win)
        t1 = ttk.Frame(tc)
        tc.add(t1, text ='Booking Amount Setting')
        tc.pack(expand = 1, fill ="both")
        frame_main=Frame(t1, width=780, height=650, bg='black').place(x=10, y=10)
        btn_frame=Frame(t1, width=760, height=520, bg='white', relief=SUNKEN, bd=5).place(x=20, y=30)
        lbl=Label(t1, text="Lawn rent:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=50)
        lawn__charges_spin = Spinbox(t1,textvariable=lawn, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=55)
        lbl=Label(t1, text="Lawn Decoration:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=100)
        lawn__charges_spin = Spinbox(t1,textvariable=decoration, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=105)
        lbl=Label(t1, text="Gate + Stage:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=150)
        lawn__charges_spin = Spinbox(t1,textvariable=gate, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=155)
        lbl=Label(t1, text="Watchman:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=200)
        lawn__charges_spin = Spinbox(t1,textvariable=watchme, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=205)
        lbl=Label(t1, text="No.:", font=('Arail', 15, 'bold'), bg='white').place(x=350, y=200)
        lawn__charges_spin = Spinbox(t1,textvariable=no, from_ = 0, to =9999, increment=1, width=5,font=(15))
        lawn__charges_spin.place(x=450, y=205)
        lbl=Label(t1, text="Cleaning Charges:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=250)
        lawn__charges_spin = Spinbox(t1,textvariable=cleaning, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=255)
        lbl=Label(t1, text="Electric Charges:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=300)
        lawn__charges_spin = Spinbox(t1,textvariable=electric, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=305)
        lbl=Label(t1, text="Water Charges:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=350)
        lawn__charges_spin = Spinbox(t1,textvariable=water, from_ = 0, to =9999, increment=50, width=5,font=(15))
        lawn__charges_spin.place(x=250, y=355)
        lbl=Label(t1, text="Whatsapp Number:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=400)
        whatsno_entry=Entry(t1,textvariable=whatsapp,font=('Arail', 15, 'bold'), width=25)
        whatsno_entry.place(x=250, y=400)
        lbl=Label(t1, text="Email ID:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=450)
        Email_entry=Entry(t1,textvariable=emialid,font=('Arail', 15, 'bold'), width=25)
        Email_entry.place(x=250, y=450)
        lbl=Label(t1, text="Password:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=500)
        passs_entry=Entry(t1,textvariable=password, font=('Arail', 15, 'bold'),width=25)
        passs_entry.place(x=250, y=500)
        


        btn_frame=Frame(t1, width=760, height=70, bg='white', relief=SUNKEN, bd=5).place(x=20, y=560)
        Exit_button=Button(t1, text='Exit',bg='Red',fg='White',height=2, width=15,font=('arial', 10, 'bold'),command=setting_win.destroy)
        Exit_button.place(x=620, y=575)
        Update_button=Button(t1, text='Update',bg='Green',fg='White',height=2, width=15,font=('arial', 10, 'bold'))
        Update_button.place(x=470, y=575)

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
        url = "https://www.geeksforgeeks.org"
        timeout = 1
        try:
            request=requests.get(url, timeout=timeout)
            image1 = Image.open("wifi.png")
            resize_image=image1.resize((50,40), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize_image)

            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=1450,y=780)

        # catching exception
        except (requests.ConnectionError, requests.Timeout) as exception:
            image1 = Image.open("no_wifi.png")
            resize_image=image1.resize((50,40), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=1450,y=780)
            

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

        self.treeview_frame=Frame(self.main_window, width=1020, height=570, bg='white',bd=8, relief= RIDGE).place(x=500, y=200)
        self.column_notice=('#1','#2','#3','#4','#5', '#6', '#7', '#8')
        self.tree_note=ttk.Treeview(self.main_window, columns=self.column_notice, show='headings', height=23)
        self.tree_note.column('#1',anchor=CENTER, width=70)
        self.tree_note.column('#2',anchor=CENTER, width=285)
        self.tree_note.column('#3',anchor=CENTER, width=120)
        self.tree_note.column('#4',anchor=CENTER, width=100)
        self.tree_note.column('#5',anchor=CENTER, width=150)
        self.tree_note.column('#6',anchor=CENTER, width=70)
        self.tree_note.column('#7',anchor=CENTER, width=100)
        self.tree_note.column('#8',anchor=CENTER, width=100)
        
        self.tree_note.heading('#1', text='Bill No')
        self.tree_note.heading('#2', text='Party Name')
        self.tree_note.heading('#3', text='Booking Date')
        self.tree_note.heading('#4', text='Phone No')
        self.tree_note.heading('#5', text='Occasion')
        self.tree_note.heading('#6', text='Person')
        self.tree_note.heading('#7', text='Advance')
        self.tree_note.heading('#8', text='Pending')
        

        self.tree_note.bind('<<TreeviewSelect>>')
        self.tree_note.place(x=510, y=212)
        #frame2=Frame(self.maipn_window, width=500, height=100, bg='blue').place(x=1,y=30)
        lbs1=Label(self.main_window, text='DAATA BICHAYAT & DECORATION WORKS', font=('courier', 25, 'bold'), bg='blue', fg='White').place(x=450, y=780)
        self.main_window.resizable(0,0)
        '''if request==1:
            image1 = Image.open("wifi.png")
            resize_image=image1.resize((50,40), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize_image)

            label1 = tk.Label(image=test)
            label1.image = test
            

            # Position image
            label1.place(x=40,y=40)
        else:
            image1 = Image.open("no_wifi.png")
            resize_image=image1.resize((50,40), Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resize_image)

            label1 = tk.Label(image=test)
            label1.image = test

            # Position image
            label1.place(x=40,y=40)'''
      
       
        

        self.main_window.mainloop()

if __name__ == "__main__":
    dawat_Lawn=Daata_Decorations()
    