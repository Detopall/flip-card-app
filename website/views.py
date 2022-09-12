from unicodedata import category
from flask import Blueprint, render_template, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Card, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    return "<h1> This works </h1>"