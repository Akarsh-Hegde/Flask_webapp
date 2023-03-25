from flask import Blueprint,render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])
@views.route('/index', methods=['GET','POST'])
# @login_required
def home():
    # return render_template("home.html", user=current_user)
    return render_template("index.html", user=current_user)


@views.route('/generic', methods=['GET','POST'])
def generic():
    return render_template("generic.html", user=current_user)


@views.route('/elements', methods=['GET','POST'])
def element():
    return render_template("elements.html", user=current_user)