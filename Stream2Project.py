import os
import json
import csv

from flask import Flask
from flask import render_template
from pymongo import MongoClient



# import pandas as pd
app = Flask(__name__)
MONGO_URI='mongodb://admin:pass@ds255347.mlab.com:55347/heroku_lcz40x4w'
MONGODB_HOST = 'ds255347.mlab.com'
MONGODB_PORT = 55347
DBS_NAME = 'heroku_lcz40x4w'
COLLECTION_NAME = 'projects'


@app.route("/")
def index():
    """
    A Flask view to serve the main dashboard page.
    """
    return render_template("index.html")


@app.route("/Platform.html")
def Platform():
    """
    A Flask view to serve the main dashboard page.
    """

    return render_template("Platform.html")
@app.route("/data")
def data():
    return jsonify(get_data())

@app.route("/Proposals.html")
def Proposals():
    """
    A Flask view to serve the main dashboard page.
    """
    return render_template("Proposals.html")

''' @app.route("/")
def chart():
    df = pd.read_csv('flare').drop('Open', axis=1)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True) '''

@app.route("/donorsUS/projects")
def donor_projects():
    """
    A Flask view to serve the project data from
    MongoDB in JSON format.
    """

    # # A constant that defines the record fields that we wish to retrieve.
    # FIELDS = {
    #     '_id': False, 'funding_status': False, 'school_state': True,
    #     'resource_type': True, 'poverty_level': True,
    #     'date_posted': False, 'total_donations': True
    # }

    # A constant that defines the record fields that we wish to retrieve.
    FIELDS = {
        '_id': False, 'funding_status': True, 'school_state': True,
        'resource_type': True, 'poverty_level': True,
        'date_posted': True, 'total_donations': True
    }

    # Open a connection to MongoDB using a with statement such that the
    # connection will be closed as soon as we exit the with statement
    with MongoClient(MONGO_URI) as conn:
        # Define which collection we wish to access
        collection = conn[DBS_NAME][COLLECTION_NAME]
        # Retrieve a result set only with the fields defined in FIELDS
        # and limit the the results to 55000
        projects = collection.find(projection=FIELDS, limit=20000)
        # Convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(projects))


if __name__ == "__main__":
    app.run(debug=True)
