#!/usr/bin/python3
""" An index file for our Flask API
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    """ A function to return status of the API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def obj_stats():
    """returns the number of each object"""

    my_dict = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(my_dict)
