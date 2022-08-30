# entry point for our Python Website. Initialize flask.
from flask import Flask, render_template
# this will import the views variable from our views file.
from views import views
# create flask application. This initializes the application.
app = Flask(__name__)

# we could very easily inside of this script say app.root. Give the route we want and then say define.
# needs to be at @ sign its a decorator.
@app.route("/")
# define the route
def home():
    # return whatever it is you want to return from here usually this is HTML
    # return "This is the Home Page"
    return render_template("index.html")
# register the blueprint. and the url prefix is slash.
# That means we are going to access all of the routes from the views file from /slash
# app.register_blueprint(views, url_prefix="/")

# if we put /views this means we would access the views route
app.register_blueprint(views, url_prefix="/views")

# this will allow you access the home2 route
# app.register_blueprint(views, url_prefix="/view/home")
if __name__ == '__main__':
    # you can tell flask what port you want the website to run on. By default its port 5000.
    # The reason debug=True here because whenever you change any files inside of your flask application
    # it will automatically refresh the app.
    app.run(debug=True, port =8000)
