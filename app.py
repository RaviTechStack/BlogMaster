from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    l = [1, 2 , 3,4,5]
    return render_template("index.html", number = l)

@app.route("/blog")
def detailBlog():
    l = [1, 2 , 3]
    return render_template("showBlog.html", number = l)

@app.route("/profile")
def Profile():
    l = [1, 2 ]
    return render_template("profile.html", number = l)

if __name__ == "__main__":
    app.run(debug=True)