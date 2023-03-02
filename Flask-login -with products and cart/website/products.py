from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import db
from .models import Item, User, Cart
from flask_login import login_required, current_user

products = Blueprint('products', __name__)


@products.route('/admin', methods=['GET', 'POST'])
@login_required
def admin_page():
    if request.method == "POST":
        name = request.form.get('name')
        barcode = request.form.get('barcode')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        description = request.form.get('description')

        item = Item.query.filter_by(name=name).first()
        if item:
            flash("Product already exists", category="error")
        else:
            new_item = Item(name=name, barcode=barcode, price=price, quantity=quantity, description=description)
            db.session.add(new_item)
            db.session.commit()
            flash('Item Added!', category='success')
            return redirect(url_for("views.home"))
    carts = Cart.query.all()
    items = Item.query.all()

    return render_template("admin.html", user=current_user, carts=carts, items=items)

    # {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},