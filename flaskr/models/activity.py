"""This file contains the activity schema"""
from flaskr.db import get_database

ACTIVITY = "activity"

db = get_database()


class Activity:
    def get_collection(self):
        if db.get_collection(ACTIVITY) is not None:
            return db.get_collection(ACTIVITY)
        else:
            return self.create_collection()

    # create_collection creates the "activity" collection in database.
    def create_collection(self):
        # Create the collection and return.
        activity_collection = db.create_collection(
            name="activity",
            validator={
                "bsonType": "object",
                "title": "activity validation",
                "required": ["steps", "active_calories_burned", "speed"],
                "properties": {
                    "steps": {
                        "bsonType": "int",
                        "description": "Number of steps up till now",
                    },
                    "active_calories_burned": {
                        "bsonType": "object",
                        "description": "Count of active calories burnt",
                        "required": ["value", "unit"],
                        "properties": {
                            "value": {
                                "bsonType": "int",
                                "minimum": 0,
                                "description": "Magnitude of Energy burn (Calories, Joules etc.)",
                            },
                            "unit": {
                                "enum": ["Kcal", "KJoules"],
                                "description": "Unit of Energy burnt",
                            },
                        },
                    },
                    "speed": {
                        "bsonType": "int",
                        "desciption": "Average speed while running",
                    },
                },
            },
        )
        return db.get_collection(ACTIVITY)
