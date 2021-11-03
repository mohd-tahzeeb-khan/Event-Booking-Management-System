import pymongo
from pymongo import MongoClient 
  
  
class Dawat_lawn_database():





    def order_booking_event(self,bokedondate,bill, partyname, phone1, phone2, occ, persons, advancereceive, bookingfordate, addressofparty, rent, decoration, stage, watchmen,noofwatch,cleaningcharges,watercharges,electriccharges,totalamt):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Order_booking"]#collection name
        temp_dic={
            'booked on date':bokedondate,
            'bill No':bill,
            'Party Name':partyname,
            'Phone':phone1,
            'alternate No':phone2,
            'occasion':occ,
            'person':persons,
            'advance':advancereceive,
            'Booking for date':bookingfordate,
            'address':addressofparty,
            'lawn rent':rent,
            'lawn decoration':decoration,
            'gate+stage':stage,
            'watchman':watchmen,
            'No of watchman':noofwatch,
            'cleaning charges':cleaningcharges,
            'water charges':watercharges,
            'eletric charges':electriccharges,
            'total':totalamt
        }
        Collection.insert(temp_dic)

    def cancel_orderbooking_event(self,bill, phone1,dateforbook):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Order_booking"]
        del_temp_data={
            'bill No':bill,
            'phone':phone1,
            'Booking for date':dateforbook
        }


    def fetch_order_event(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Order_booking"]

        z=Collection.find({},{'_id':0})
        return z

    def fetch_date_event(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Order_booking"]
        i=Collection.find({},{'_id':0})
        
        return i

    def bill_no_declaration(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["BillingNO"]
        

        for bill in Collection.find({},{'_id':0}):
            a=bill['bill']
            #print(a)
        return a


    def alter_bill_no(self, now, alter):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["BillingNO"]
        print(now, alter)
        myquery = { "bill":now }
        newvalues = { "$set": { "bill": alter} }
        sex=Collection.update_one(myquery, newvalues)
        print(sex)

    def delete_order(self, bill_nom):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Order_booking"]

        dic_temp_delete={'bill No':bill_nom}
        print(dic_temp_delete)
        Collection.delete_one(dic_temp_delete)
        return

    def add_worker(self, name, salary, work, phone):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Workers"]#collection name
        dic_add_worker={
            'Name':name,
            'work':work,
            'phone':phone,
            'salary':salary
        }

        Collection.insert_one(dic_add_worker)
    def Fetch_workers_data(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Workers"]
        i=Collection.find({},{'_id':0})
        
        return i

    def Delete_worker(self, name, phone):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Workers"]

        dic_temp_delete={'Name':name,'phone':phone}
        #print(dic_temp_delete)
        Collection.delete_one(dic_temp_delete)


    def Alter_settings(self,lawn_rent ,lawn_decoration,Lawn_gate,price_watchman,no_watchman,cleaning_charges,electric_charges,water_charges,whatsapp_no,email,password, lawn_rent1 ,lawn_decoration1,Lawn_gate1,price_watchman1,no_watchman1,cleaning_charges1,electric_charges1,water_charges1,whatsapp_no1,email1,password1):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Settings"]#collection name

        dic_old_alter_settings={
            'Lawn Rent':lawn_rent,
            'Lawn Decorations':lawn_decoration,
            'Lawn Gate':Lawn_gate,
            'Watchman':price_watchman,
            'nos watchman':no_watchman,
            'cleaning charges':cleaning_charges,
            'electric charges':electric_charges,
            'water charges':water_charges,
            'Whatsapp no':whatsapp_no,
            'Email':email,
            'password':password
            }

        dic_new_alter_setting={"$set":{
            'Lawn Rent':lawn_rent1,
            'Lawn Decorations':lawn_decoration1,
            'Lawn Gate':Lawn_gate1,
            'Watchman':price_watchman1,
            'nos watchman':no_watchman1,
            'cleaning charges':cleaning_charges1,
            'electric charges':electric_charges1,
            'water charges':water_charges1,
            'Whatsapp no':whatsapp_no1,
            'Email':email1,
            'password':password1
            
        }}
        print(dic_add_settings)
        Collection.insert_one(dic_add_settings)

    def fetch_settings(self):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Settings"]#collection name
        i=Collection.find({},{'_id':0})
        
        return i


        

#d1=Dawat_lawn_database()
#d1.Alter_settings(12000,3500,1500,300,1,250,600,150,7498518671,'tahzeebk80@gmail.com','@tahzeeb8.py')