# from flask import Blueprint, render_template
# from flask_login import login_required, current_user

# market = Blueprint('market', __name__)

# @market.route('/market', methods=['GET','POST'])
# def market_page():
    
#     items = [
#         {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#         {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#         {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
#      ]
#     return render_template('market.html',user=current_user, items=items)
