from flask import Blueprint, render_template, request, flash, redirect, url_for
#this file is for authentication
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)#this defines our blueprint, basically saying a different sector of my code



@auth.route('/login', methods = ['GET', 'POST'])#these are the types of requests we accept. By default its get only 
def login():
    return render_template("login.html") #this is our html, well in this case our template, you can even pass variables with Jinja 
#you can run variables to each template for them to use with jinja
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"  

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email') #If we have a post request, get the form from the request, specifically the email (the name)
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:#validate email length because that definitely says whether its valid lmao
            flash('Email must be greater than 3 characters.', category = 'error')#category name doesnt matter
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category = 'error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:  #add user to database
            new_user = User(email = email, first_name = firstName, password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category = 'success')#so u can add more categories using this category stuff
            return redirect(url_for('views.home'))#finds what url maps to the function home, could do just / but if u change it its fucked
            #(blueprintname.functionname)

    return render_template("sign_up.html")

