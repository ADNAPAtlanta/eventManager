import pyrebase
from firebase import firebase
import os
import requests
import time
import calendar
import datetime
try:
    # for Python2
    from Tkinter import *
    from tkinter import filedialog
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import filedialog

    config = {
  "apiKey": " AIzaSyCkLEL05gnfbuGaWYVlOmXbkZWb_95CYBE",
  "authDomain": "school-events-3b62e.firebaseapp.com",
  "databaseURL": "https://school-events-3b62e.firebaseio.com",
  "storageBucket": "school-events-3b62e.appspot.com",

}


#Database refresher
def refreshDatabase():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    events = db.child("Events").order_by_child("dateNum").get()
    todaysDate = time.strftime("%m/%d/%Y")
    print("today's date it " + todaysDate)
    dateNum = time.mktime(datetime.datetime.strptime(todaysDate, "%m/%d/%Y").timetuple())
    print("Todays timecode is " + str(dateNum))
    for event in events.each():
        
        if float(event.val().get("dateNum")) < float(dateNum):
            db.child("Events").child(event.key()).remove()
            db.child(event.val().get("category")).child(event.key()).remove()
            storage.child(event.val().get("category")).delete(event.val().get("picture"))
            print(event.key() + " removed")
            #print(float(event.val().get("dateNum")))
            #print(event.val().get("picture"))
#Category Listers
def listCategoriesCulture():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    events = db.child("cultural").get()
    for event in events.each():
        print(event.key())
    
def listCategoriesAcademic():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    events = db.child("academic").get()
    for event in events.each():
        print(event.key())
def listCategoriesFun():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    events = db.child("fun").get()
    for event in events.each():
        print(event.key())
def listCategoriesSocial():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    events = db.child("social").get()
    for event in events.each():
        print(event.key())
def listCategoriesGreek():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    events = db.child("greek").get()
    for event in events.each():
        print(event.key())

#List Buildings
def listBuildings():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    buildings = db.child("Buildings").get()
    for building in buildings.each():
        print(building.key())

#List Organizations
def listOrganizations():
    firebasePyre = pyrebase.initialize_app(config)
    database = firebasePyre.database()
    storage = firebasePyre.storage()
    Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)
    db = firebasePyre.database()
    organizations = db.child("Organizations").get()
    for organization in organizations.each():
        print(organization.key())

def showTime():
    todaysDate = time.strftime("%m/%d/%Y")
    print("today's date it " + todaysDate)
    dateNum = time.mktime(datetime.datetime.strptime(todaysDate, "%m/%d/%Y").timetuple())
    print("Todays timecode is " + str(dateNum))


    
print(refreshDatabase())







