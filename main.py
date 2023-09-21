
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import PIL
import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date
import requests
import time
from tkinter.scrolledtext import ScrolledText
from database import Dawat_lawn_database
d1=Dawat_lawn_database()

class Daata_Decorations():
    
    def reset(self):
        self.party_person_entry.delete(0,END)
        self.party_name_entry.delete(0, END)
        self.party_phone_entry.delete(0, END)
        self.party_alterphone_entry.delete(0, END)
        self.Advance_entry.delete(0, END)
        self.Address_entry.delete(0, END)
        self.discount_entry.delete(0, END)
        self.grand_total_entry.delete(0,END)
        
    

    def add_booking(self):
        global party_person_entry,bilnum,a, party_name_entry, party_phone_entry, today_1, party_alterphone_entry, Advance_entry,Address_entry, counter
        today= date.today()
        bilnum=d1.bill_no_declaration()
        self.a=bilnum
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
        self.bill.set(bilnum)
        self.grandtotal=StringVar(add_book)
        self.discount=StringVar(add_book)
        for data in d1.fetch_settings():
            fetch_lawn_rent=data['Lawn Rent']
            fetch_lawn_decoration=data['Lawn Decorations']
            fetch_lawn_gate=data['Lawn Gate']
            fetch_lawn_watchman=data['Watchman']
            fetch_lawn_watchman_no=data['nos watchman']
            fetch_lawn_cleaning=data['cleaning charges']
            fetch_lawn_electric=data['electric charges']
            fetch_lawn_water=data['water charges']
        self.lawn_rent.set(fetch_lawn_rent)
        self.decoration.set(fetch_lawn_decoration)
        self.stage.set(fetch_lawn_gate)
        self.guard.set(fetch_lawn_watchman)
        self.no_guard.set(fetch_lawn_watchman_no)
        self.cleaning_charges.set(fetch_lawn_cleaning)
        self.electric_charges.set(fetch_lawn_electric)
        self.water__charges.set(fetch_lawn_water)
        self.discount.set(00)



        frame_main=Frame(add_book,width=1180, height=780, bg='black').place(x=10,y=10)
        frame_heading=Frame(add_book, width=1170, height=70, bg='white').place(x=15, y=15)
        heading_label=Label(add_book, text='BOOKING',font=('arail',35, 'bold'),fg='blue', bg='white').pack(side=TOP,pady=20)
        main_frame=Frame(add_book, height=690, width=1170, bg='white', relief=SUNKEN).place(x=15, y=95)





        self.party_billno_label=Label(add_book, text='Bill No:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=110)
        self.party_bill_no_entry=Entry(add_book, width=25,state=DISABLED,textvariable=self.bill,font=(15), relief=SUNKEN, bd=3)
        self.party_bill_no_entry.place(x=250, y=110)
        self.party_name_label=Label(add_book, text='Party Name:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=150)
        self.party_name_entry=Entry(add_book, width=25,justify='center', relief=SUNKEN,font=(15), bd=3)
        self.party_name_entry.place(x=250, y=150)
        self.party_phone_label=Label(add_book, text='Phone No:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=190)
        self.party_phone_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        self.party_phone_entry.place(x=250, y=190)
        self.party_alterphone_label=Label(add_book, text='Alternative Phone no:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=230)
        self.party_alterphone_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        self.party_alterphone_entry.place(x=250, y=230)
        self.party_label=Label(add_book, text='Occasion:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=270)
        self.event_choosen = ttk.Combobox(add_book,font=(12), width=23)
        self.event_choosen['values'] = ('MARRIAGE','HALDI & SANGEET','ENGAGEMENT', 'ANNIERSARY', 'BIRTHDAY', 'FAMILY GET-TOGETHER','OFFICE EVENT', 'FAREWELL', 'OTHER')
        self.event_choosen.place(x=250, y=270)
        self.event_choosen.current(0)
        self.party_label=Label(add_book, text='Person:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=310)
        self.party_person_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        self.party_person_entry.place(x=250, y=310)
        self.Advance_label=Label(add_book, text='Advance:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=350)
        self.Advance_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        self.Advance_entry.place(x=250, y=350)

        self.Date_of_booking_label=Label(add_book, text='Booking For Date:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=390)
        #Date_of_booking_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15),state=DISABLED, bd=3).place(x=250, y=390)
        #cal=Calendar(add_book, selectmode='day', weekendbackground='white', showweeknumbers=False, weekendforeground='black')
        self.cal=DateEntry(add_book,selectmode='day',year=today.year,date_pattern='dd/MM/yyyy',weekendbackground='white', month=today.month,showweeknumbers=False, weekendforeground='black', day=today.day,width=24, font=(15))
        self.cal.place(x=250, y=390)
        self.Address_label=Label(add_book, text='Address:', bg='White', font=('arail', 12, 'bold')).place(x=50, y=430)
        self.Address_entry=Entry(add_book, width=25, relief=SUNKEN,font=(15), bd=3)
        self.Address_entry.place(x=250, y=430)
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
        self.watchman_no_charges_spin = Spinbox(add_book, from_ = 0, to =9, textvariable=self.no_guard, command=self.guardcount, width=2,font=(15))
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
        self.discount__label=Label(add_book, text='Discount:', bg='White', font=('arail', 12, 'bold')).place(x=600, y=390)
        self.discount_entry=Entry(add_book, textvariable=self.discount, width=25, relief=SUNKEN, font=(15), bd=3)
        self.discount_entry.place(x=800, y=390)
        self.cal_total_label=Label(add_book, text='TOTAL:', bg='White', font=('arail', 16, 'bold')).place(x=600, y=500)
        self.grand_total_entry=Entry(add_book, width=15,textvariable=self.grandtotal, state=DISABLED,relief=SUNKEN,font=(16), bd=3)
        self.grand_total_entry.place(x=800, y=500)
        self.add_btn=Button(add_book, text='ADD BOOKING', width=15,     font=('arail', 10, 'bold'),height=2, fg='white', bg='green', command=lambda:[self.send(),add_book.destroy()]).place(x=320,y=730)
        self.add_btn=Button(add_book, text='RESET', width=15, height=2, font=('arail', 10, 'bold'),fg='Black', bg='yellow', command=self.reset).place(x=520,y=730)
        self.add_btn=Button(add_book, text='CLOSE', width=15, height=2, font=('arail', 10, 'bold'),fg='white', bg='red', command=add_book.destroy).place(x=720,y=730)
        self.cal_button=Button(add_book, text='Calculate', bg='Green', fg='White', font=(15), width=15, command=self.total).place(x=990, y=493)
        
        add_book.mainloop()
    

    def send(self):
        self.today_1=date.today().strftime('%d-%m-%y')
        self.date=self.today_1
        self.bill=self.party_bill_no_entry.get()
        self.partyn=self.party_name_entry.get()
        self.phoe=self.party_phone_entry.get()
        self.phone2=self.party_alterphone_entry.get()
        self.event=self.event_choosen.get()
        self.party_person=self.party_person_entry.get()
        self.advance=int(self.Advance_entry.get())
        self.calendar=self.cal.get()
        self.add=self.Address_entry.get()
        self.rent=int(self.lawn_rent_entry.get())
        self.decoration=int(self.decoration_entry.get())
        self.stage=int(self.gate_entry.get())
        self.watchmen=int(self.watchman__charges_spin.get())
        self.no_guard=int(self.watchman_no_charges_spin.get())
        self.clean=int(self.cleaning__charges_spin.get())
        self.water=int(self.water__charges_spin.get())
        self.electric=int(self.electric__charges_spin.get())
        self.total=int(self.grand_total_entry.get())
        
        d1.order_booking_event(self.date,self.bill,self.partyn.upper(),self.phoe,self.phone2,self.event,self.party_person,self.advance,self.calendar,self.add,self.rent,self.decoration,self.stage,self.watchmen,self.no_guard,self.clean,self.water,self.electric, self.total)
        b=self.a
       # print(type(b))
        c=int(b)+1
       # print(type(c))
        d1.alter_bill_no(b,c)
       


    def guardcount(self):
        
        self.no=int(self.watchman_no_charges_spin.get())
        self.amt=int('300')
        self.guard.set(self.no*self.amt)
    def total(self):
        self.rent=int(self.lawn_rent_entry.get())
        self.decoration=int(self.decoration_entry.get())
        self.stage=int(self.gate_entry.get())
        self.watchmen=int(self.watchman__charges_spin.get())
        self.no_guard=int(self.watchman_no_charges_spin.get())
        self.clean=int(self.cleaning__charges_spin.get())
        self.water=int(self.water__charges_spin.get())
        self.electric=int(self.electric__charges_spin.get())
        
        self.minus=int(self.discount_entry.get())

        self.add=self.rent+self.decoration+self.stage+self.clean+self.water+self.electric+self.watchmen
        self.grand_total=self.add-self.minus
        self.grandtotal.set(self.grand_total)





    def cancel_tree_view(self):

        MsgBox = tk.messagebox.askquestion ('Cancel Booking','You Want to Cancel Booking',icon = 'warning')
        if MsgBox == 'yes':
            curItem = self.tree_note.focus()
            temp=self.tree_note.item(curItem, 'values')
            #print(temp)
            bill_no=temp[0]
            selected_item = self.tree_note.selection()
            self.tree_note.delete(selected_item)
            d1.delete_order(bill_no)
        else:
            tk.messagebox.showinfo('Return')
           
    def search(self):
        query = bill_entry.get()
        selections = []
        
        for child in self.tree_note.get_children():
            if query in self.tree_note.item(child,'values'):
                send=self.tree_note.item(child)['values']
                selections.append(child)
        self.tree_note.selection_set(selections)
        
    def Cancel_booking(self):
        global bill_entry
        self.cancel_book=tk.Toplevel()
        today= date.today()
        self.cancel_book.geometry('800x800')
        self.cancel_book.title('CANCELLING')
        image1 = Image.open("Images/search_logo.png")
        resize_image=image1.resize((80,80), Image.LANCZOS)
        test = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(image=test)
        label1.image = test
        back_frame=Frame(self.cancel_book, width=780, height=780, bg='black').place(x=10,y=10)
        main_frame=Frame(self.cancel_book, width=760, height=760, bg='grey').place(x=20,y=20)
        heading_frame=Frame(self.cancel_book, width=350, height=80, bg='White', relief=RAISED, bd=5).place(x=25,y=25)
        search_frame=Frame( self.cancel_book, width=395, height=80, bg='White', relief=RAISED, bd=5).place(x=380,y=25)
        bill_label=Label(self.cancel_book, text='Bill No:', bg='white', font=(20)).place(x=400,y=35)
        bill_entry=Entry(self.cancel_book, width=16,font=(25))
        bill_entry.place(x=500, y=35)

        date_label=Label(self.cancel_book, text='Date:', bg='white', font=(20)).place(x=400,y=70)
        cal=DateEntry(self.cancel_book,selectmode='day',year=today.year,date_pattern='dd/MM/yyyy',weekendbackground='white', month=today.month,showweeknumbers=False, weekendforeground='black', day=today.day,width=14, font=(15))
        cal.place(x=500, y=70)
        btn_search=Button(self.cancel_book, image=test, width=50, height=50, relief=FLAT ,bg='White',command=self.search).place(x=700, y=35)

        down_frame=Frame(self.cancel_book, width=750, height=600, bg='White', relief=RAISED, bd=5).place(x=25,y=110)
        down_frame=Frame(self.cancel_book, width=750, height=60, bg='White', relief=RAISED, bd=5).place(x=25,y=710)
        #down_frame=Frame(cancel_book, width=460, height=150, bg='White', relief=RAISED, bd=5).place(x=20,y=20)
        label_heading=Label(self.cancel_book, text='Cancellation', bg='white',font=('arial', 30, 'bold')).place(x=70, y=40)
        #treeview_frame=Frame(cancel_book, width=1020, height=570, bg='white',bd=8, relief= RIDGE).place(x=500, y=200)
        self.column_notice=('#1','#2','#3','#4','#5')
        self.tree_note=ttk.Treeview(self.cancel_book, columns=self.column_notice, show='headings', height=27)
        self.tree_note.column('#1',anchor=CENTER, width=100)
        self.tree_note.column('#2',anchor=CENTER, width=120)
        self.tree_note.column('#3',anchor=CENTER, width=270)
        self.tree_note.column('#4',anchor=CENTER, width=110)
        self.tree_note.column('#5',anchor=CENTER, width=100)  
        self.tree_note.heading('#1', text='Bill No')
        self.tree_note.heading('#2', text='Booking Date')
        self.tree_note.heading('#3', text='Party Name')
        self.tree_note.heading('#4', text='Phone No')
        self.tree_note.heading('#5', text='Advance')
        self.tree_note.bind('<<TreeviewSelect>>')
        self.tree_note.place(x=30, y=120)
        for x in d1.fetch_order_event():
            r1=x['bill No']
            r2=x['Booking for date']
            r3=x['Party Name']
            r4=x['Phone']
            r5=x['advance']
            self.tree_note.insert("",tk.END, value=[r1,r2,r3,r4,r5])

        reset_btn=Button(self.cancel_book, width=15, text='Cancel', font=(8), command=self.cancel_tree_view).place(x=35, y=720)
        reset_btn=Button(self.cancel_book, width=15, text='Exit',bg='red', font=(8),command=self.cancel_book.destroy).place(x=590, y=720)
        return self.tree_note
        self.cancel_book.mainloop()

    def delete_worker(self):
            curItem = self.tree_note.focus()
            temp=self.tree_note.item(curItem, 'values')
            name=temp[0]
            phone=temp[2]
            #print(name, phone)
            selected_item = self.tree_note.selection()
            self.tree_note.delete(selected_item)
            d1.Delete_worker(name, phone)

    def add_worker(self):
        self.tree_note.insert('', 'end',values=(self.Worker_name.get(),self.Worker_work.get(),self.Worker_phone.get(), self.Worker_salary.get()))
        d1.add_worker(self.Worker_name.get(), self.Worker_salary.get(),self.Worker_work.get(),self.Worker_phone.get())
        
    def working_staff(self):
        data=d1.Fetch_workers_data()
        self.working_staff=tk.Tk()
        self.working_staff.geometry('700x780')
        self.working_staff.title('STAFF')
        self.worker_name_s=StringVar()
        self.worker_phone_s=StringVar()
        self.worker_salary_s=StringVar()
        self.worker_work_s=StringVar()
        back_frame=Frame(self.working_staff, width=680, height=780, bg='Black').place(x=10, y=10)
        front_frame=Frame(self.working_staff, width=650, height=750).place(x=25, y=25)
        heading_frame=Frame(self.working_staff, width=630, height=100, bg='white', relief=RIDGE, bd=5).place(x=35, y=40)
        heading_label=Label(self.working_staff, text='WORKING STAFF', bg='white',font=('arail', 40, 'bold')).place(x=140, y=60)
        main_frame=Frame(self.working_staff, width=630, height=510, bg='white', relief=RIDGE, bd=5).place(x=35, y=145)
        btn_frame=Frame(self.working_staff, width=630, height=100, bg='white', relief=RIDGE, bd=5).place(x=35, y=655)
        frame_form=Frame(self.working_staff, width=500, height=290, bg='cyan').place(x=100, y=350)
        column_notice=('#1','#2','#3','#4')
        self.tree_note=ttk.Treeview(self.working_staff, columns=column_notice, show='headings', height=8)
        self.tree_note.column('#1',anchor=CENTER, width=230)
        self.tree_note.column('#2',anchor=CENTER, width=150)
        self.tree_note.column('#3',anchor=CENTER, width=100)
        self.tree_note.column('#4',anchor=CENTER, width=100)
        self.tree_note.heading('#1', text='Name')
        self.tree_note.heading('#2', text='Work')
        self.tree_note.heading('#3', text='Phone No')
        self.tree_note.heading('#4', text='Salary')
        self.tree_note.bind('<<TreeviewSelect>>')
        self.tree_note.place(x=45, y=155)
        for data in d1.Fetch_workers_data():
            data1=data['Name']
            data2=data['work']
            data3=data['phone']
            data4=data['salary']
            #print(data1)
            self.tree_note.insert("",tk.END,values=[data1,data2,data3,data4])

        lbl=Label(self.working_staff, text='Name:', font=('arial', 12, 'bold')).place(x=120, y=370)
        self.Worker_name=Entry(self.working_staff, textvariable=self.worker_name_s,font=(12))
        self.Worker_name.place(x=270,y=370)

        lbl=Label(self.working_staff, text='Work:', font=('arial', 12, 'bold')).place(x=120, y=420)
        self.Worker_work=Entry(self.working_staff, textvariable=self.worker_work_s,font=(12))
        self.Worker_work.place(x=270,y=420)

        lbl=Label(self.working_staff, text='Phone:', font=('arial', 12, 'bold')).place(x=120, y=470)
        self.Worker_phone=Entry(self.working_staff, textvariable=self.worker_phone_s,font=(12))
        self.Worker_phone.place(x=270,y=470)

        lbl=Label(self.working_staff, text='Salary:', font=('arial', 12, 'bold')).place(x=120, y=520)
        self.Worker_salary=Entry(self.working_staff, textvariable=self.worker_salary_s,font=(12))
        self.Worker_salary.place(x=270,y=520)

        add_btn=Button(self.working_staff, width=15, text='Add', font=(8),command=self.add_worker).place(x=50, y=700)
        delete_btn=Button(self.working_staff, width=15, text='Delete', font=(8), command=self.delete_worker).place(x=260, y=700)
        exit_btn=Button(self.working_staff, width=15, text='Exit',bg='red', font=(8),command=self.working_staff.destroy).place(x=460, y=700)
        self.working_staff.mainloop()
    def Developer(self):
        Developer=tk.Toplevel()
        Developer.geometry('800x800')
        Developer.title('Developed By:')
        Developer['bg']='black'
        image1 = Image.open("Images/developer.jpg")

        resize_image=image1.resize((785,785), Image.LANCZOS)
        test = ImageTk.PhotoImage(resize_image)
        panel = tk.Label(Developer,image=test)
        panel.image = test
        panel.place(x=5,y=5)
        Developer.mainloop()

    def send_setting(self):
        for data in d1.fetch_settings():
            fetch_lawn_rent=data['Lawn Rent']
            fetch_lawn_decoration=data['Lawn Decorations']
            fetch_lawn_gate=data['Lawn Gate']
            fetch_lawn_watchman=data['Watchman']
            fetch_lawn_watchman_no=data['nos watchman']
            fetch_lawn_cleaning=data['cleaning charges']
            fetch_lawn_electric=data['electric charges']
            fetch_lawn_water=data['water charges']
            fetch_lawn_whatsapp=data['Whatsapp no']
            fetch_lawn_email=data['Email']
            fetch_lawn_password=data['password']
        d1.Alter_settings(fetch_lawn_rent,fetch_lawn_decoration,fetch_lawn_gate,fetch_lawn_watchman,fetch_lawn_watchman_no,fetch_lawn_cleaning,fetch_lawn_electric,fetch_lawn_water,fetch_lawn_whatsapp,fetch_lawn_email,fetch_lawn_password,self.lawn__charges_spin.get(),self.decoration__charges_spin.get(),self.gate__charges_spin.get(),self.watchman__charges_spin.get(),self.watchman_no__charges_spin.get(),self.cleaning__charges_spin.get(),self.electric__charges_spin.get(),self.water__charges_spin.get(),self.whatsno_entry.get(),self.Email_entry.get(),self.passs_entry.get())
    def setting(self):
        global lawn__charges_spin,decoration__charges_spin,gate__charges_spin,watchman__charges_spin,watchman_no__charges_spin,cleaning__charges_spin,electric__charges_spin,water__charges_spin,whatsno_entry,Email_entry,passs_entry
        self.setting_win=tk.Tk()
        self.setting_win.geometry('800x680')
        self.setting_win.title('SETTING')
        self.setting_win['bg']='black'
        for data in d1.fetch_settings():
            fetch_lawn_rent=data['Lawn Rent']
            fetch_lawn_decoration=data['Lawn Decorations']
            fetch_lawn_gate=data['Lawn Gate']
            fetch_lawn_watchman=data['Watchman']
            fetch_lawn_watchman_no=data['nos watchman']
            fetch_lawn_cleaning=data['cleaning charges']
            fetch_lawn_electric=data['electric charges']
            fetch_lawn_water=data['water charges']
            fetch_lawn_whatsapp=data['Whatsapp no']
            fetch_lawn_email=data['Email']
            fetch_lawn_password=data['password']
            
        
        
        self.lawn=StringVar(self.setting_win)
        self.decoration=StringVar(self.setting_win)
        self.gate=StringVar(self.setting_win)
        self.watchme=StringVar(self.setting_win)
        self.no=StringVar(self.setting_win)
        self.cleaning=StringVar(self.setting_win)
        self.electric=StringVar(self.setting_win)
        self.water=StringVar(self.setting_win)
        self.whatsapp=StringVar(self.setting_win)
        self.emialid=StringVar(self.setting_win)
        self.password=StringVar(self.setting_win)

        self.lawn.set(fetch_lawn_rent)
        self.decoration.set(fetch_lawn_decoration)
        self.gate.set(fetch_lawn_gate)
        self.watchme.set(fetch_lawn_watchman)
        self.no.set(fetch_lawn_watchman_no)
        self.cleaning.set(fetch_lawn_cleaning)
        self.electric.set(fetch_lawn_electric)
        self.water.set(fetch_lawn_water)
        self.whatsapp.set(fetch_lawn_whatsapp)
        self.emialid.set(fetch_lawn_email)
        self.password.set(fetch_lawn_password)


        self.tc = ttk.Notebook(self.setting_win)
        self.t1 = ttk.Frame(self.tc)
        self.tc.add(self.t1, text ='Booking Amount Setting')
        self.tc.pack(expand = 1, fill ="both")
        self.frame_main=Frame(self.t1, width=780, height=650, bg='black').place(x=10, y=10)
        self.btn_frame=Frame(self.t1, width=760, height=520, bg='white', relief=SUNKEN, bd=5).place(x=20, y=30)
        self.lbl=Label(self.t1, text="Lawn rent:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=50)
        self.lawn__charges_spin = Spinbox(self.t1,textvariable=self.lawn, from_ = 0, to =99999, increment=50, width=5,font=(15))
        self.lawn__charges_spin.place(x=250, y=55)
        self.lbl=Label(self.t1, text="Lawn Decoration:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=100)
        self.decoration__charges_spin = Spinbox(self.t1,textvariable=self.decoration, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.decoration__charges_spin.place(x=250, y=105)
        self.lbl=Label(self.t1, text="Gate + Stage:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=150)
        self.gate__charges_spin = Spinbox(self.t1,textvariable=self.gate, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.gate__charges_spin.place(x=250, y=155)
        self.lbl=Label(self.t1, text="Watchman:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=200)
        self.watchman__charges_spin = Spinbox(self.t1,textvariable=self.watchme, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.watchman__charges_spin.place(x=250, y=205)
        self.lbl=Label(self.t1, text="No.:", font=('Arail', 15, 'bold'), bg='white').place(x=350, y=200)
        self.watchman_no__charges_spin = Spinbox(self.t1,textvariable=self.no, from_ = 0, to =9,increment=1, width=5,font=(15))
        self.watchman_no__charges_spin.place(x=450, y=205)
        self.lbl=Label(self.t1, text="Cleaning Charges:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=250)
        self.cleaning__charges_spin = Spinbox(self.t1,textvariable=self.cleaning, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.cleaning__charges_spin.place(x=250, y=255)
        self.lbl=Label(self.t1, text="Electric Charges:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=300)
        self.electric__charges_spin = Spinbox(self.t1,textvariable=self.electric, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.electric__charges_spin.place(x=250, y=305)
        self.lbl=Label(self.t1, text="Water Charges:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=350)
        self.water__charges_spin = Spinbox(self.t1,textvariable=self.water, from_ = 0, to =9999, increment=50, width=5,font=(15))
        self.water__charges_spin.place(x=250, y=355)
        self.lbl=Label(self.t1, text="Whatsapp Number:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=400)
        self.whatsno_entry=Entry(self.t1,textvariable=self.whatsapp,font=('Arail', 15, 'bold'), width=25)
        self.whatsno_entry.place(x=250, y=400)
        self.lbl=Label(self.t1, text="Email ID:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=450)
        self.Email_entry=Entry(self.t1,textvariable=self.emialid,font=('Arail', 15, 'bold'), width=25)
        self.Email_entry.place(x=250, y=450)
        self.lbl=Label(self.t1, text="Password:", font=('Arail', 15, 'bold'), bg='white').place(x=30, y=500)
        self.passs_entry=Entry(self.t1,textvariable=self.password, font=('Arail', 15, 'bold'),width=25)
        self.passs_entry.place(x=250, y=500)
        self.btn_frame=Frame(self.t1, width=760, height=70, bg='white', relief=SUNKEN, bd=5).place(x=20, y=560)
        self.Exit_button=Button(self.t1, text='Exit',bg='Red',fg='White',height=2, width=15,font=('arial', 10, 'bold'),command=self.setting_win.destroy)
        self.Exit_button.place(x=620, y=575)
        self.Update_button=Button(self.t1, text='Update',bg='Green',fg='White',height=2, width=15,command=lambda:[self.send_setting(),self.setting_win.destroy()],font=('arial', 10, 'bold'))
        self.Update_button.place(x=470, y=575)
        self.setting_win.mainloop()

    def get_date(self):
        d=self.dd_entry.get()
        m=self.mm_entry.get()
        y=self.yy_entry.get()
        get_d=d+'/'+m+'/'+y
        for i in d1.fetch_date_event_booked_or_not():
            date=i['Booking for date']
            
            if date==get_d:
                a='BOOKED'

                self.show_result.set(a)
                break
            elif get_d=='':
                a='no input'
                self.show_result.set(a)
            else:
                a='NO BOOKING'
                self.show_result.set(a)
    def date_reset(self):
        self.dd_entry.delete(0, END)
        self.mm_entry.delete(0, END)
        self.yy_entry.delete(0, END)
        return


   
    def __init__(self):
        date_temp_empty_list=[]
        name_temp_empty_list=[]
        for d in d1.fetch_date_event():
            date_show=d['Booking for date']
            name=d['Party Name']
            date_temp_empty_list.append(date_show)
            name_temp_empty_list.append(name)
        for i in date_temp_empty_list:
            events={i:('london','Program')}
        today= date.today()
        self.main_window=Tk()
        self.dd=StringVar()
        self.mm=StringVar()
        self.yy=StringVar()
        self.show_result=StringVar()
        url = "https://www.geeksforgeeks.org"
        timeout = 1
        try:
            request=requests.get(url, timeout=timeout)
            image1 = Image.open("Images/wifi.png")
            resize_image=image1.resize((50,40), Image.LANCZOS)
            test = ImageTk.PhotoImage(resize_image)

            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=1450,y=780)

        # catching exception
        except (requests.ConnectionError, requests.Timeout) as exception:
            image1 = Image.open("Images/no_wifi.png")
            resize_image=image1.resize((50,40), Image.LANCZOS)
            test = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=1450,y=780)
        width1= self.main_window.winfo_screenwidth()#responsive window
        height1=self.main_window.winfo_screenheight()
        self.main_window.geometry('%dx%d'%(width1, height1))
        self.main_window.title('Daata Decorations & Bichayat')
        self.main_window.iconbitmap('Images/food.ico')
        frame1=Frame(self.main_window, width=width1, height=100, bg='blue').place(x=1,y=10)
        lbs=Label(self.main_window, text='DAWAT LAWN & GARDEN', font=('courier', 60, 'bold'), bg='blue', fg='White').place(x=300, y=10)
        inquiry_frame=Frame(self.main_window, width=490, height=640, bg='white',bd=8, relief= RIDGE).place(x=2, y=130)
        inquirylbl_frame=Frame(self.main_window, width=450, height=56, bg='yellow', relief=RIDGE, bd=3).place(x=20, y=140)
        inquiry_label=Label(self. main_window, text='BOOKING CALENDAR',font=('arail', 25, 'bold'), bg='Yellow').place(x=60, y=145)
        self.cal=Calendar(self.main_window, selectmode='none',showweeknumbers=False,weekendbackground='white', weekendforeground='black')
        self.cal.pack(side=LEFT,padx=20, ipadx=10,pady=20, ipady=130)
        for i in date_temp_empty_list:
            events={i:('london','Program')}
            for k in events.keys():
                #print(k)
                date1=datetime.datetime.strptime(k,"%d/%m/%Y").date()
                self.cal.calevent_create(date1, events[k][0], events[k][1])
            self.cal.tag_config('Program', background='green', foreground='white')
        frame_date_search=Frame(self.main_window,  width=460, height=100,bg='grey', relief=SUNKEN, bd=5).place(x=15, y=650)
        lbs=Label(self.main_window, text='Date:', bg='grey', font=('arial', 15, 'bold')).place(x=20, y=660)
        self.dd_entry=Entry(self.main_window, width=3,textvariable=self.dd,bg='white', font=('arial', 15, 'bold'))
        self.dd_entry.place(x=80, y=660)
        lbs=Label(self.main_window, text='/', bg='grey',font=('arial', 20, 'bold')).place(x=125, y=655)
        self.mm_entry=Entry(self.main_window,width=3, textvariable=self.mm,bg='white', font=('arial', 15, 'bold'))
        self.mm_entry.place(x=150, y=660)
        lbs=Label(self.main_window, text='/', bg='grey',font=('arial', 20, 'bold')).place(x=195, y=655)
        self.yy_entry=Entry(self.main_window, textvariable=self.yy, width=7, bg='white', font=('arial', 15, 'bold'))
        self.yy_entry.place(x=220, y=660)
        lbs=Label(self.main_window, text='=', bg='grey',font=('arial', 20, 'bold')).place(x=305, y=660)

        self.result_entry=Entry(self.main_window, textvariable=self.show_result, width=12,state=DISABLED, bg='White',relief=RAISED, font=('arial', 15, 'bold'))
        self.result_entry.place(x=330, y=660)
        self.ddbutton=Button(self.main_window, text='SEARCH',bg='green',fg='white',width=16,font=('arial', 10, 'bold'), command=self.get_date)
        self.ddbutton.place(x=80, y=715)
        self.ddbutton=Button(self.main_window, text='CLEAR', bg='white',width=16,fg='black',font=('arial', 10, 'bold'),command=self.date_reset)
        self.ddbutton.place(x=330, y=715)
        button_frame=Frame(self.main_window, width=710, height=70, bg='white',bd=8, relief= RIDGE).place(x=500, y=130)
        self.button=Button(self.main_window, text='Add Booking',bg='orange',fg='black',height=2, width=15,font=('arial', 10, 'bold'),command=self.add_booking)
        self.button.place(x=510, y=142)
        self.button=Button(self.main_window, text='Cancel Booking',bg='orange',height=2, width=15,fg='black',font=('arial', 10, 'bold'),command=self.Cancel_booking)
        self.button.place(x=650, y=142)
        self.button=Button(self.main_window, text='Working Stuff',bg='orange',fg='Black',height=2, width=15,font=('arial', 10, 'bold'),command= self.working_staff)
        self.button.place(x=790, y=142)
        self.button=Button(self.main_window, text='Billing',bg='orange',height=2,state=DISABLED, width=15,fg='black',font=('arial', 10, 'bold'))
        self.button.place(x=930, y=142)
        self.button=Button(self.main_window, text='Setting',bg='orange',fg='black',height=2, width=15,font=('arial', 10, 'bold'),command= self.setting)
        self.button.place(x=1070, y=142)
        about_frame=Frame(self.main_window, width=300, height=70, bg='white',bd=8, relief= RIDGE).place(x=1220, y=130)
        self.button=Button(self.main_window, text='Developer',bg='orange',fg='black',height=2, width=16,font=('arial', 10, 'bold'), command=self.Developer)
        self.button.place(x=1230, y=142)
        self.button=Button(self.main_window, text='Exit',bg='red',fg='white',height=2, width=15,command=self.main_window.destroy,font=('arial', 10, 'bold'))
        self.button.place(x=1380, y=142)


        self.treeview_frame=Frame(self.main_window, width=1020, height=570, bg='white',bd=8, relief= RIDGE).place(x=500, y=200)
        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12,'bold'), foreground='blue')
        self.column_notice=('#1','#2','#3','#4','#5', '#6', '#7', '#8','#9')
        self.tree_note=ttk.Treeview(self.main_window,style="mystyle.Treeview", columns=self.column_notice, show='headings', height=26)
        self.tree_note.column('#1',anchor=CENTER, width=70)
        self.tree_note.column('#2',anchor=CENTER, width=200)
        self.tree_note.column('#3',anchor=CENTER, width=120)
        self.tree_note.column('#4',anchor=CENTER, width=100)
        self.tree_note.column('#5',anchor=CENTER, width=150)
        self.tree_note.column('#6',anchor=CENTER, width=70)
        self.tree_note.column('#7',anchor=CENTER, width=95)
        self.tree_note.column('#8',anchor=CENTER, width=90)
        self.tree_note.column('#9',anchor=CENTER, width=100)
        self.tree_note.heading('#1', text='Bill No')
        self.tree_note.heading('#2', text='Party Name')
        self.tree_note.heading('#3', text='Booking Date')
        self.tree_note.heading('#4', text='Phone No')
        self.tree_note.heading('#5', text='Occasion')
        self.tree_note.heading('#6', text='Person')
        self.tree_note.heading('#7', text='Advance')
        self.tree_note.heading('#8', text='Pending')
        self.tree_note.heading('#9', text='Deal Amount')
        self.tree_note.bind('<<TreeviewSelect>>')
        self.tree_note.place(x=510, y=212)

        for x in d1.fetch_order_event():
            r1=x['bill No']
            r2=x['Party Name']
            r3=x['Booking for date']
            r4=x['Phone']
            r5=x['occasion']
            r6=x['person']
            r7=x['advance']
            r8=x['total']
            r_total=int(r8)-int(r7)
            self.tree_note.insert("",tk.END, value=[r1,r2,r3,r4,r5,r6,r7,r_total, r8])
        #frame2=Frame(self.maipn_window, width=500, height=100, bg='blue').place(x=1,y=30)
        lbs1=Label(self.main_window, text='DAATA BICHAYAT & DECORATION WORKS', font=('courier', 25, 'bold'), bg='blue', fg='White').place(x=450, y=780)

        self.main_window.mainloop()

if __name__ == "__main__":
    dawat_Lawn=Daata_Decorations()
    