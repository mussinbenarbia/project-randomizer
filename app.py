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
    
# @app.route("/add_projects")
# def add_projects():
#     mongo.db.projects.insert_many([
#         {
#             'name': "Blogging App",
#             'stack': ["vue", "python", "flask", "postgresql"],
#             'cat': "web"
#         },
#         {
#             'name': "Twitter Clone",
#             'stack': ["react", "ruby", "rails", "mongodb"],
#             'cat': "web"
#         },
#         {
#             'name': "Music Player",
#             'stack': ["kotlin"],
#             'cat': "mobile"
#         },
#         {
#             'name': "Todo App",
#             'stack': ["swift"],
#             'cat': "mobile"
#         },
#         {
#             'name': "Quiz Game",
#             'stack': ["angular"],
#             'cat': "web"
#         },
#         {
#             'name': "Dice Rolling Simulator",
#             'stack': ["svelte"],
#             'cat': "web"
#         },
#         {
#             'name': "E-Commerce Site",
#             'stack': ["svelte", "nodejs", "express", "postgresql" ],
#             'cat': "web"
#         },
#         {
#             'name': "Chat App",
#             'stack': ["react", "firebase"],
#             'cat': "web"
#         },
#     ])
#     return jsonify(message="success")

    
# @app.route("/add_technologies")
# def add_technologies():
#     mongo.db.technologies.insert_many([
#         {'name': "react", 'cat':"front"},
#         {'name': "vue", 'cat':"front"},
#         {'name': "angular", 'cat':"front"},
#         {'name': "svelte", 'cat':"front"},

#         {'name': "nodejs", 'cat':"back"},
#         {'name': "ruby", 'cat':"back"},
#         {'name': "python", 'cat':"back"},
#         {'name': "django", 'cat':"back"},
#         {'name': "rails", 'cat':"back"},
#         {'name': "express", 'cat':"back"},
        
#         {'name': "kotlin", 'cat':"mobile"},
#         {'name': "swift", 'cat':"mobile"},
        
#         {'name': "postgresql", 'cat':"db"},
#         {'name': "mongodb", 'cat':"db"},
#         {'name': "firebase", 'cat':"db"},
#         ])
#     return jsonify(message="success")