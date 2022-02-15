from flask_app import app                    
from flask import render_template,redirect,request,session,flash
from flask_app.models.post_model import Post
from flask_app.models.user_model import User  

# @app.route('/dashboard')
# def welcome():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={ 
#         "user":User.get_by_id(id=session['user_id']),
#         "posts": Post.get_all()
#     }
#     return render_template('my_profile.html',**data)

# @app.route('/post/new')
# def new():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     return render_template("create_post.html")

# @app.post('/add')
# def add():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     if not Post.validate_car(request.form):
#         return redirect('/post/new')
#     data ={
#         **request.form,
#         'user_id':session['user_id']
#     }
#     Post.save(data)
#     return redirect('/dashboard')