from flask import Blueprint
#this file is for authentication

auth = Blueprint('auth', __name__)#this defines our blueprint, basically saying a different sector of my code

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"#this is our html
@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

