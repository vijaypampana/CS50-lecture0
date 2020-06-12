from flask import Flask, render_template
import json

app = Flask(__name__)   #A new web application is a flask application, app is a variable which can be used in the below file ex @app.route

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/jsonBeautifier")
def jsonBeautifier():
    return render_template("jsonBeautifier.html")

@app.route("/xmlBeautifier")
def xmlBeautifier():
    return "Welcome to XML Beautifier Page"

@app.route("/createUser")
def createUser():
    return "Welcome to Create Automated User Page"