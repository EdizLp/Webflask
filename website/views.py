#this is for .... 
from flask import Blueprint, render_template

views = Blueprint('views', __name__)#this defines our blueprint

@views.route('/')#a route is the specific url and we use @ to define those. Basically when they go to a certain page run this code
# we used / as this is just the home address
def home():
    return render_template("home.html")
