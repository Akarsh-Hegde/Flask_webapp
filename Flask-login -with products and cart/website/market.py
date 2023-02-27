from flask import Blueprint, render_template
from flask_login import login_required, current_user

market = Blueprint('market', __name__)

@market.route('/market', methods=['GET','POST'])
def market_page():
    
    items = Item.query.all()
    return render_template('market.html',user=current_user, items=items)
