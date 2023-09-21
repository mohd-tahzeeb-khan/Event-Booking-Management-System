import pymongo
from pymongo import MongoClient
class database_setup():
    def __init__(self):
        client=MongoClient()
        databases=client.list_database_names()
        if "Dawat_lawn_2021" in databases:
            pass
        else:
            myclient = MongoClient("mongodb://localhost:27017/") #making connection 
            db = myclient["Dawat_lawn_2021"]#database name
            Collection = db["Order_booking"]#Collection name
            Data={
              "booked on date": "20/09/2023",
              "bill No": 1,
              "Party Name": "Example name",
              "Phone": {"$numberLong": "0"},
              "alternate No": {"$numberLong": "0"},
              "occasion": "Birthday",
              "person": 0,
              "advance": 0,
              "Booking for date": "21/02/2024",
              "address": "------",
              "lawn rent": 0,
              "lawn decoration": 0,
              "gate+stage": 0,
              "watchman": 0,
              "No of watchman": 0,
              "cleaning charges": 0,
              "water charges": 0,
              "eletric charges": 0,
              "total": 0
            }
            Collection.insert_one(Data)
            Collection=db["Settings"]#Collection name
            Data={
              "Lawn Rent": "0000",
              "Lawn Decorations": "00",
              "Lawn Gate": "00",
              "Watchman": "00",
              "nos watchman": "0",
              "cleaning charges": "00",
              "electric charges": "00",
              "water charges": "00",
              "Whatsapp no": "00",
              "Email": "example@try.com",
              "password": "000000"
            }
            Collection.insert_one(Data)
            Collection=db["Workers"]#Collection name
            Data={
              "Name": "Worker Name",
              "work": "Worker",
              "phone": "000000000",
              "salary": "12000"
            }
            Collection.insert_one(Data)
            Collection=db["BillingNO"]#Collection name
            Data={
              "bill": 1
            }
            Collection.insert_one(Data)