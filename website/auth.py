from flask import Blueprint, render_template
#this file is for authentication

auth = Blueprint('auth', __name__)#this defines our blueprint, basically saying a different sector of my code



@auth.route('/login')
def login():
    return render_template("login.html", text = "testing", user = "Ediz") #this is our html, well in this case our template, you can even pass variables with Jinja 

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"  

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

