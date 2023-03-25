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
        
        id = request.form.get('id')   
        item_check = Item.query.filter_by(id=id).first()
        
        if request.form.get('add') == 'Add':
            if item_check:
                flash("Product already exists", category="error")
            else:  
                new_item = Item(name=name, barcode=barcode, price=price, quantity=quantity, description=description)
                db.session.add(new_item)
                db.session.commit()
                flash('Item Added!', category='success')
                return redirect(url_for("products.admin_page"))
        
        id = request.form.get('id')   
        item = Item.query.filter_by(id=id).first()

        if request.form.get('remove') == 'Remove':
            db.session.delete(item)
            db.session.commit()
            flash('Item Removed!', category='success')
            return redirect(url_for("products.admin_page"))

        if  request.form.get('edit') == 'Edit':
            # db.session.delete(item)
            # db.session.commit()
            if item:
                name = request.form.get('name')
                barcode = request.form.get('barcode')
                price = request.form.get('price')
                quantity = request.form.get('quantity')
                description = request.form.get('description')
            
                item1 = Item(name=name, barcode=barcode, price=price, quantity=quantity, description=description)
                db.session.add(item1)
                db.session.commit()
                flash('Item Updated(delete+add=edit)!', category='success')
                return redirect(url_for("products.admin_page"))
            else:
                flash("Product doesnt exists", category="error")

    items = Item.query.all()
    carts = Cart.query.all()

    return render_template("admin.html", user=current_user, carts=carts, items=items)

    # {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},