from flask import Flask,render_template,request,redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app=Flask(
    __name__,
    template_folder="./templates",
    static_folder="./static",
    static_url_path=""
)

app.secret_key="crazy_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///Database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#model for user =single row
class User(db.Model):
    #class variables
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), unique=True, nullable =False)
    password_hash= db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)


#routes for home page
@app.route("/")
def home():
<<<<<<< HEAD
    return render_template('index.html')

@app.route("/login_page")
def login_page():
    # Show login/register form here
    return render_template("login_raw.html")

@app.route("/stars")
def stars_page():
    # Show login/register form here
    return render_template("stars.html")
=======
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template('index.html')
>>>>>>> main

#Login route
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session["username"] = username
        return redirect(url_for("dashboard"))
    else:
        return render_template("index.html", error="Invalid Credentials")

#register route
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password: 
        return render_template("index.html", error="Please fill all fields")
    
    #Check if user exists already 
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
<<<<<<< HEAD
        return render_template("rewards_raw.html", error="User already exists")
=======
        return render_template("index.html", error="User already exists")
>>>>>>> main
    
    #Create and save new user 
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    session["username"] = username 
    return redirect(url_for("dashboard"))


#Dashboard route
@app.route("/dashboard")
def dashboard():
        if "username" in session:
<<<<<<< HEAD
            return render_template("rewards_raw.html", username=session["username"])
=======
            return render_template("Dashboard.html", username=session["username"])
>>>>>>> main
        else:
            return redirect(url_for('home'))

#logout route 
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
