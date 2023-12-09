"""This file contains the activity schema"""
from flaskr.db import get_database

ACTIVITY = "activity"

db = get_database()


class Activity:
    def get_collection(self):
        if ACTIVITY in db.list_collection_names():
            print(f"Found Collection {ACTIVITY}")
            return db.get_collection(ACTIVITY)
        else:
            print(f"Not Found Collection {ACTIVITY}")
            return self.create_collection()

    # create_collection creates the "activity" collection in database.
    def create_collection(self):
        # Create the collection and return.
        return db.activity
