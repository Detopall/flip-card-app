from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Card, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html", title="Home", username=current_user.username, user=current_user)

@views.route("/create-card", methods=["GET", "POST"])
def create_card():
    if request.method == "POST":
        description = request.form.get("description")
        front_side = request.form.get("front-side")
        back_side = request.form.get("back-side")
        if (not checkForValidCard(description, front_side, back_side)):
            flash("Not all fields are filled. Try again.")
        else:
            new_card = Card(description=description, front_side=front_side, back_side=back_side, user_id=current_user.id)
            db.session.add(new_card)
            db.session.commit()
            flash("Card created!", category="success")
    return render_template("create-card.html", title="Create Card", username=current_user.username, user=current_user)

def checkForValidCard(description, front_side, back_side):
    # return true if all fields are not empty
    return len(description) != 0 and len(front_side) != 0 and len(back_side) != 0

@views.route("/study")
def study():
    return render_template("study.html", title="Study", username=current_user.username, user=current_user)

