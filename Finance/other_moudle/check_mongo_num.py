import pymongo
import time

client=pymongo.MongoClient('localhost',27017)
COL=client['Finance']
DOC=COL['DFCFW10_4']

while True:
    print DOC.find().count()
    time.sleep(2)