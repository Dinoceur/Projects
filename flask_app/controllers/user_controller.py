from flask_app import app    
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.user_model import User
from flask_app.models.info_model import Info



@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')
    return render_template('login.html')



@app.route('/profile')
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "user":User.get_one_users(id=session['user_id']),
        "info": Info.get_one_profile(id=session['user_id'])
    }
    return render_template("my_profile.html", **data)


@app.post('/register/user')
def register_user():
    if not User.validate_registration(request.form):
        return redirect('/register')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    
    return redirect("/initial/info")

@app.route('/initial/info')
def initial_info():
    return render_template('initial_info.html')

@app.post('/login/user')
def login_user():
    user = User.get_by_email(request.form)
    
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect("/login")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect("/profile")



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# @app.route('create-post', methods=['GET', 'POST'])
# def create_post():
#     if request.method == 'POST':
#         link = request.form.get('link')
#         content = request.form.get('content')
#         data = Posts(by=current_user.username, link=link, content=content)
#         db.session.add(data)
#         db.session.commit()
#         return redirect(url_for('app.posts'))
#     return render_template('createpost.html')

# @app.route('/posts')
# def posts():
#     posts = Posts.query.all()
#     return render_template('my_profile.html', posts=posts[::-1])