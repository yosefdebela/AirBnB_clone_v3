#!/usr/bin/python3

"""The main flask app file"""
import sys
sys.path.extend(['/home/yos/stack@alx/AirBnB_clone_v3'])
import os
from os import getenv

from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from views import app_views
from dotenv import load_dotenv
load_dotenv()
sys.path.extend(os.environ['path2'])


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origin": "0.0.0.0"}})


@app.teardown_appcontext
def clean_up(exception=None):
    """eliminates current Session"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """handles 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True, debug=True)
