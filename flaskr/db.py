from pymongo import MongoClient

def get_database():
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.senseii_db
    return db