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
   
    def __init__(self):
        

        self.main_window=Tk()
        

        self.main_window.overrideredirect(True)
       
        #main_window.wm_state('iconic')

        width1= self.main_window.winfo_screenwidth()#responsive window
        height1=self.main_window.winfo_screenheight()
        self.main_window.geometry('%dx%d'%(width1, height1))
        self.main_window.title('Daata Decorations & Bichayat')
        self.main_window.iconbitmap('food.ico')
        frame1=Frame(self.main_window, width=width1, height=100, bg='blue').place(x=1,y=30)
        lbs=Label(self.main_window, text='DAWAT LAWN & GARDEN', font=('courier', 60, 'bold'), bg='blue', fg='White').place(x=300, y=30)
        #photo=PhotoImage(file='close.png')
        image1 = Image.open("close.png")
        resize_image=image1.resize((20,22), Image.ANTIALIAS)
        test=ImageTk.PhotoImage(resize_image)
        self.btn=Button(self.main_window, text='Exit',image=test,bg='White',fg='red', font=50,command=self.main_window.destroy)
        self.btn.place(x=1500,y=0)
        self.btn.bind('<Enter>', self.on_enter)
        self.btn.bind('<Leave>', self.on_leave)
        inquiry_frame=Frame(self.main_window, width=490, height=650, bg='white',bd=8, relief= RIDGE).place(x=2, y=140)
        inquirylbl_frame=Frame(self.main_window, width=450, height=56, bg='yellow', relief=RIDGE, bd=3).place(x=10, y=150)
        inquiry_label=Label(self. main_window, text='INQUIRY',font=('arail', 25, 'bold'), bg='Yellow').place(x=200, y=155)
        self.cal=Calendar(self.main_window, selectmode='day')
        self.cal.pack(side=LEFT,padx=20, pady=20, ipady=110)
        #frame2=Frame(self.maipn_window, width=500, height=100, bg='blue').place(x=1,y=30)
        lbs1=Label(self.main_window, text='DAATA BICHAYAT & DECORATION WORKS', font=('courier', 25, 'bold'), bg='blue', fg='White').place(x=450, y=800)
        self.main_window.resizable(0,0)
        self.main_window.mainloop()

if __name__ == "__main__":
    dawat_Lawn=Daata_Decorations()