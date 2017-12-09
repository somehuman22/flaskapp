from app import app, db
from flask import render_template, request, redirect, flash
from app.models import Post

@app.route('/')
def index():
    return render_template('index.html', posts=Post.query.all())

@app.route('/posts/<id>')
def show_post(id):
    return render_template('show_post.html', post=Post.query.get(id))

@app.route('/new/post', methods=['POST','GET'])
def new_post():
    if request.method == 'POST':
         data = request.form
         np = Post(title=data['title'], body=data['body'])
         db.session.add(np)
         db.session.commit()
         return redirect('/')
    else:
        return render_template('new_post.html')

@app.route('/delete/post/<id>')
def delete_post(id):
    post = Post.query.get(id)
    flash("You are about to delete Post #" + str(post.id) + ".")
    db.session.delete(post)
    db.session.commit()
    return redirect('/')