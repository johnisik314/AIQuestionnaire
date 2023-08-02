
from pymongo import *
import json

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myClient.database_sample

collection = db.sample_collection

with open("data.json") as inputFile:
    file_data = json.load(inputFile)

collection.insert_many(file_data)