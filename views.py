# Creating views/routes. Routes are kind of the end point of the URLs
# setting up routes in a separate file helps not clutter the main initialization script. Blueprint
#from flask import Blueprint
# to pass a query parameter import request from flask
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

# Say whatever the name the file is. you can name it whatever you want. Is equal to Blueprint.
# then put the name of this blueprint. Just make it so that it matches this variable name makes it easier.
# now that we have created the blueprint we need to link or register to the blueprint from flask application
# the first argument that you need to pass in is __name__ then the name of the blueprint
views = Blueprint(__name__, "views")

@views.route("/")
def home():
    #return "home page"
    # the reason why this is called a template because you can pass variables and values to the template
    # that can then be rendered by it.
    return render_template("index.html", name="Joe", age=21)

# The way you access a parameter that is in the URL is use the angle brackets
# put it as a parameter for the function that is going to return whatever it is that you want.
'''@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)'''

@views.route("/home")
def home2():
    #return "home page"

 '''@views.route("/profile")
def profile():
    # use this as a dictionary to access any query parameters.
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)'''

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/json")
def get_json():
    # if you want to return json you can return a python dictionary and jsonify it.
    return jsonify({'name': 'tim', 'coolness': 10})

@views.route("/data")
#so someone's going to send us data in json format to this route.
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    # prefix with views which is the name of our template. then whatever the function name we want to redirect to.
    #return redirect(url_for("views.get_json"))
    return redirect(url_for("views.home"))
