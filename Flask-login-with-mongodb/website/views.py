from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .auth import session
from bson import ObjectId

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    # check if current user is set in session
    if "_id" in session:
        user = db.user.find_one({"_id": session["_id"]}) 
        # render dashboard for current user
        return render_template("home.html", user = user)
    else:
        # redirect to login page if current user is not set in session
        flash("Please login to continue", category="error")
        return redirect(url_for("auth.login"))


@views.route('/market', methods=['GET','POST'])
def market_page():
    if "_id" in session:
        user = db.user.find_one({"_id": session["_id"]}) 
    
    product = db.product.find()

    if request.method == "POST":
        id = request.form.get('id')
        item = db.product.find_one({"_id": id}) 

        cart = db.cart.find_one({"user_id": session["_id"], "name": item["pname"]})
        
        if cart:
            cart["quantity"] += 1
            db.cart.update_one({"_id": cart["_id"]}, {"$set": cart})
            flash('Item updates!', category='success')
            return redirect(url_for("views.cart_page"))
        else:
            new_cart_item = {
            "name": item["pname"],
            "price": item["price"],
            "description": item["description"],
            "user_id": session["_id"],
            "quantity": 1
            }
            db.cart.insert_one(new_cart_item)
            flash('Item Purchased!', category='success')
            return redirect(url_for("views.cart_page"))
        
        # return render_template('market.html', product=product, user = user)
    
    return render_template('market.html', product=product, user = user)


@views.route('/cart', methods=['GET','POST'])
def cart_page():
    if "_id" in session:
        user = db.user.find_one({"_id": session["_id"]})
    cart = db.cart.find()
    if request.method == "POST":
        id = request.form.get('id')

        if request.form.get('remove') == 'Remove':
            db.cart.delete_one({"_id": ObjectId(id)})
            flash('Item Removed!', category='success')
            return redirect(url_for("views.cart_page"))
        elif request.form.get('buy') == 'Buy Now':
            cart_item = db.cart.find_one({"_id": ObjectId(id)})
            item = db.product.find_one({"pname": cart_item["name"]}) 
            
            # db.product.delete_one({"_id": id})

            item["quantity"] -= cart_item["quantity"]
            db.product.update_one({"_id": item["_id"]}, {"$set": item})

            db.cart.delete_one({"_id": ObjectId(id)})
            flash('Item Bought!', category='success')
            return redirect(url_for("views.cart_page"))

    return render_template('cart.html', user = user, cart = cart)

    