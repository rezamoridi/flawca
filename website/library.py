from flask import Blueprint, render_template

library = Blueprint('library', __name__)

@library.route('/library')
def home():
    return render_template("library.html")