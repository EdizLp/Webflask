#this is for .... 
from flask import Blueprint

views = Blueprint('views', __name__)#this defines our blueprint

@views.route('/')#a route is the specific url and we use @ to define those. Basically when they go to a certain page run this code
# we used / as this is just the home address
def home():
    return "<h1>Test</h1>"
