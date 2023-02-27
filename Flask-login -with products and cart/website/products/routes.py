from flask import redirect,render_template, url_for, flash,request
from website import db, app

@app.route('/addbrand',methods=['GET','post'])
def products():
    return render_template("products/addbrand")

