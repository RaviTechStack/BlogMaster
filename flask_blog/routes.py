from flask import  render_template, request, flash, redirect, url_for, send_from_directory
from flask_blog import app, db, bcrypt, login_manager
import os
from sqlalchemy.sql.expression import func
from werkzeug.utils import secure_filename
from flask_blog.model import Blog, User
from flask_login import login_user, current_user, logout_user, login_required



if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.mkdir(app.config["UPLOAD_FOLDER"])

if not os.path.exists(app.config["PROFILE_UPLOAD_FOLDER"]):
    os.mkdir(app.config["PROFILE_UPLOAD_FOLDER"])

ALLOWED_EXTENSIONS = ["png", "jpg", "webp", "jpeg"]

@app.template_filter('nl2br')
def nl2br(value):
    return value.replace('\n', '<br>\n')

app.jinja_env.filters['nl2br'] = nl2br

def check(value, listItems):
    if value.lower() in listItems.blog_title.lower() or value in listItems.blog_category.lower() or value in listItems.author.firstname.lower() or value in listItems.author.username.lower():
        return True
    

@app.route("/")
def home():
    blog = Blog.query.all()[0:4]
    Allblog = Blog.query.all()
    randomBlog = Blog.query.order_by(func.random()).limit(3).all()
    l = [1, 2 , 3,4,5]
    return render_template("index.html", number = l, blog= blog, allBlog = Allblog, random = randomBlog)

@app.route("/search", methods=['GET', 'POST'])
def searchResult():
    if request.method == "GET":
        keyword = request.args.get("search")
        print(keyword)
        Allblog = Blog.query.all()
        searchRes = []
        for blg in Allblog:
            if check(keyword, blg):
                searchRes.append(blg)
            else:
                pass
        print(searchRes)
    return render_template("searchResult.html", blogs = searchRes)

@app.route("/signup", methods=['GET', 'POST'])
def signupBlog():
    if request.method == "POST":
        if current_user.is_authenticated:
            return redirect("/")
        username = request.form.get("username")
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        phone = request.form.get("phone")
        profile_pic = request.files.get("profilepic")
        cover_pic = request.files.get("coverpic")
        password = request.form.get("password")
        secure_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if (profile_pic and allowed_file(profile_pic.filename)) and (cover_pic and allowed_file(cover_pic.filename)):
                profile_picname = secure_filename(profile_pic.filename)
                cover_picname = secure_filename(cover_pic.filename)
                profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_picname))
                cover_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], cover_picname))
        
        user = User(firstname= firstname, lastname=lastname, email=email, username= username, phone= phone,profile_pic=profile_picname, cover_pic= cover_picname, password = secure_password )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("SignUp.html") 

@app.route("/login", methods=['GET', 'POST'])
def loginBLog():
    if current_user.is_authenticated:
            return redirect("/")
    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password") 
        user = User.query.filter_by(username = username).first()
        if user and bcrypt.check_password_hash(user.password , password):
            login_user(user)
            return redirect("/")
        else:
            return "Error in submitting"
    return render_template("login.html")


@app.route("/logout")
@login_required
def logoutUser():

    logout_user()
    return redirect("/login")



@app.route("/blog/<id>")
@login_required
def detailBlog(id):
    showBlog = Blog.query.filter_by(blog_id = id).first()
    relatedBlog = Blog.query.filter_by(blog_category = showBlog.blog_category)
    return render_template("showBlog.html", blog = showBlog, related = relatedBlog)

@app.route("/profile/<id>")
def Profile(id):
    l = [1, 2 ]
    user = User.query.filter_by(id=id).first()
    userBlog = Blog.query.filter_by(blog_user = id)
    return render_template("profile.html", postBlog =userBlog, user=user)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        blog_title = request.form.get("title")
        blog_content = request.form.get("content")
        blog_highlight = request.form.get("highlight")
        blog_category = request.form.get("category")
        file = request.files.get("blogPic")
        
        
        if file.filename == '':
            return "Please Select the valid File"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new_blog = Blog(blog_title= blog_title, blog_content= blog_content, blog_img=filename, blog_highlights = blog_highlight, blog_category =blog_category, blog_user = current_user.id )
            db.session.add(new_blog)
            db.session.commit()
            return redirect("/")
    return render_template("addBlog.html", blog = None)

@app.route("/update/<id>", methods=['GET', 'POST'])
def updatePost(id):
    updateBlog = Blog.query.filter_by(blog_id = id).first()
    if request.method == 'POST':
        blog_title = request.form.get("title")
        blog_content = request.form.get("content")
        blog_highlight = request.form.get("highlight")
        blog_category = request.form.get("category")
        file = request.files.get("blogPic")
        
        
        if file.filename == '':
            updateBlog.blog_title = request.form.get("title")
            updateBlog.blog_content = request.form.get("content")
            updateBlog.blog_highlight = request.form.get("highlight")
            updateBlog.blog_category = request.form.get("category")
            db.session.commit()
            return redirect(f"/profile/{current_user.id}")
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            updateBlog.blog_title = request.form.get("title")
            updateBlog.blog_content = request.form.get("content")
            updateBlog.blog_highlight = request.form.get("highlight")
            updateBlog.blog_category = request.form.get("category")
            updateBlog.blog_img = filename
            
            db.session.commit()
           

            return redirect(f"/profile/{current_user.id}")
    return render_template("addBlog.html", blog= updateBlog)

@app.route("/delete/<id>", methods=['GET', 'POST'])
def deletePost(id):
    deleteBlog = Blog.query.filter_by(blog_id = id).first()
    if deleteBlog.author.id == current_user.id:
        db.session.delete(deleteBlog)
        db.session.commit()
        return redirect(f"/profile/{current_user.id}")
    return "Invalid Action"
    

@app.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"])



