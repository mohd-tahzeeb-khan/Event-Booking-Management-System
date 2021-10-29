import pymongo
from pymongo import MongoClient 
  
  
class Dawat_lawn_database():





    def order_booking_event(self,bill, partyname, phone1, phone2, occ, persons, advancereceive, bookingfordate, addressofparty, rent, decoration, stage, watchmen,noofwatch,cleaningcharges,watercharges,electriccharges,totalamt):
        myclient = MongoClient("mongodb://localhost:27017/") #making connection 
        db = myclient["Dawat_lawn_2021"]#database name
        Collection = db["Order_booking"]#collection name
        temp_dic={
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
            'total':totalamt,
        }
        Collection.insert(temp_dic)

d1=Dawat_lawn_database()
