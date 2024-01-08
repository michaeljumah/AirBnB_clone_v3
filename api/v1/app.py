#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from api.v1 import app_views
from flask import Flask,
from models import storage
import os

# Global Flask Application Variable: app
app = Flask(__name__)
# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    # start Flask app
    app.run(host=host, port=port, threaded=True)

