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

#d1=Dawat_lawn_database()
#d1.fetch_date_event()
