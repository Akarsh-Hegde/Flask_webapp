from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Item, User

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/market', methods=['GET','POST'])
def market_page():
    
    items = Item.query.all()
    return render_template('market.html', user=current_user, items=items)
