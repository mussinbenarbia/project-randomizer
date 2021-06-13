from flask import Flask, jsonify, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS;
import os

app = Flask(__name__, static_folder="client/public", static_url_path="")

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
mongo = PyMongo(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/technologies")
def get_technologies():
    technologies = mongo.db.technologies
    output = []
    for tech in technologies.find():
        output.append({'name' : tech['name'], 'category' : tech['cat']})
    return jsonify(output)

@app.route("/api/projects")
def get_projects():
    projects = mongo.db.projects
    output = []
    for project in projects.find():
        output.append({'name' : project['name'], 'stack' : project['stack'], 'cat' : project['cat']})
    return jsonify(output)