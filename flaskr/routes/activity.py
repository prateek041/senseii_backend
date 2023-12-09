"""This file contains the blueprint and views for /user/health"""
from flask import Blueprint, jsonify, request
from flaskr.models.activity import Activity

user_activity_bp = Blueprint("auth", __name__, url_prefix="/user")


@user_activity_bp.route("/activity", methods=("GET", "POST"))
def get_user_activity():
    if request.method == "GET":
        return jsonify("This is user activity")
    else:
        return jsonify("THis was post method")
