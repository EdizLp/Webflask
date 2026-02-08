#this is for our blueprint
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user #for logging in users, current user works with usermixin
from .models import Note
from . import db
import json #for deleting notes
views = Blueprint('views', __name__)#this defines our blueprint

@views.route('/', methods = ['GET', 'POST'])#a route is the specific url and we use @ to define those. Basically when they go to a certain page run this code
# we used / as this is just the home address
@login_required #cant get to the home page unless you're logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) <= 1:
            flash('Note is too short!', category = 'error')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category = 'success')
            
    return render_template("home.html", user = current_user)#we can reference this variable current user in our home template

@views.route('/delete-note', methods = ['POST'])
def delete_note():#this requst isnt as a form
    note = json.loads(request.data) #this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note: #if the note exists 
        if note.user_id == current_user.id: #if we own this note 
            db.session.delete(note)
            db.session.commit()

    return jsonify({}) 