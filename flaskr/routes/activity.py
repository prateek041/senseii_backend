"""This file contains the blueprint and views for /user/health"""
from flask import Blueprint, jsonify, request
from flaskr.models.activity import Activity
from bson import json_util

user_activity_bp = Blueprint("user", __name__, url_prefix="/user")


# get the Activity collection
activity_collection = Activity().get_collection()


@user_activity_bp.route("/activity", methods=("GET", "POST"))
def create_user_activity():
    if request.method == "GET":
        return jsonify("This is the get route")
    # if request.method == "GET":
    #     result = activity_collection.find({})
    #     document = list(result)[0]
    #     returnjson.loads(json_util.dumps(document))
    #     return jsonify("hello")
    elif request.method == "POST":
        test_activity = {
            "steps": 2,
            "active_calories_burned": {
                "value": 10,
                "unit": "Kcal",
            },
            "speed": 10,
        }
        post_id = activity_collection.insert_one(test_activity).inserted_id
        return jsonify("This was post method")
