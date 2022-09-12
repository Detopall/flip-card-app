from unicodedata import category
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Card, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html", title="Home", username=current_user.username, user=current_user)

@views.route("/create-card")
@login_required
def create_card():
    return render_template("create-card.html", title="Create Card", username=current_user.username, user=current_user)

@views.route("/study")
@login_required
def study():
    return render_template("study.html", title="Study", username=current_user.username, user=current_user)

