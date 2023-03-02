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

        id = request.form.get('id')   
        item = Item.query.filter_by(id=id).first()
        cart = Cart.query.filter_by(user_id=current_user.id, name= item.name).first()

        if cart:
            cart.quantity += 1
            db.session.commit()
            flash('Item updates!', category='success')
            return redirect(url_for("views.cart_page"))
        else:
            new_cart_item = Cart(name=item.name, barcode=item.barcode, price=item.price, description=item.description, user_id=current_user.id)
            db.session.add(new_cart_item)
            db.session.commit()
            flash('Item Purchased!', category='success')
            return redirect(url_for("views.cart_page"))

    items = Item.query.all()
    return render_template('market.html', user=current_user, items=items)


@views.route('/cart', methods=['GET','POST'])
def cart_page():
    if request.method == "POST":

        id = request.form.get('id')   
        cart_item = Cart.query.filter_by(id=id).first()

        if request.form.get('remove') == 'Remove':
            db.session.delete(cart_item)
            db.session.commit()
            flash('Item Removed!', category='success')
            return redirect(url_for("views.cart_page"))

        elif  request.form.get('buy') == 'Buy Now':

            db.session.delete(cart_item)
            db.session.commit()
            flash('Item Bought!', category='success')
            return redirect(url_for("views.cart_page"))
    carts = Cart.query.filter(Cart.user_id==current_user.id)
    return render_template('cart.html', user=current_user, carts=carts)

    