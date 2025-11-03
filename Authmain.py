from _typeshed import IdentityFunction
from flask import Flask,render_template,request,redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="crazy_secret_key"

app.config["SQLAlchemy_DATABASE_URI"]="sqlite:///Database.db"
app.config["SQLAlchemy_TRACK_MPDIFICATIONS"]=False;
db=SQLAlchemy(app)

#model for user =single row
class User(db.model):
    #class variables
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), unique=True, nullable =False)
    password_hash= db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password= generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)


#routes for home page
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("/dashboard"))
    return render_template('index.html')

#Login route
@app.route("/Login", methods=["POST"])
def login():
        if request.method=="POST":
            username=request.form.get("username")
            password=request.form.get("password")
            user=User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["username"]=username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials"
        return render_template("Index.html")

#register route
@app.route("/register", method=["POST"])
def register():
    if user:
        return render_template("index.html", error="User already exists")
    else:
        new_user=User(username=username)
        new_user.set_password(password)
        db.session.commit()
        session["username"]=username
        return redirect(url_for("dashboard"))
#Dashboard route
@app.route("/dashboard")
def dashboard():
        if "username" in session:
            return render_template("dashboard.html", username=session["username"])
        else:
            return redirect(url_for('home'))

#logout route 
app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


if __name__ in '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
