from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Item, User, Cart

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/market', methods=['GET','POST'])
def market_page():

    if request.method == "POST":

        name = request.form.get('name')   
        barcode = request.form.get('barcode')
        price = request.form.get('price')
        description = request.form.get('description')
        
        new_cart_item = Cart(name=name, barcode=barcode, price=price, description=description)
        print(new_cart_item)
        db.session.add(new_cart_item)
        db.session.commit()
        flash('Item Purchased!', category='success')
        return redirect(url_for("views.cart_page"))

    items = Item.query.all()
    return render_template('market.html', user=current_user, items=items)


@views.route('/cart', methods=['GET','POST'])
def cart_page():

    carts = Cart.query.all()
    return render_template('cart.html', user=current_user, carts=carts)
