import re             
from flask_app import app
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.user_model import User
from flask_app.models.info_model import Info


@app.post('/register/info')
def save():
    Info.save_info(request.form)
    
    return redirect("/profile")



@app.route('/edit/info')
def edit_info():
    return render_template('update_profile.html')

@app.post('/update/info')
def update_info():
    Info.update(request.form)

    return redirect("/profile")
    