from flask import Flask,render_template,request,redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import json
import os

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

def extract_locations(feature_collection):
    locations = []
    for feature in feature_collection["features"]:
        props = feature.get("properties", {})

        name = (
            props.get("FACILITY_NAME") or
            props.get("PLACE_NAME") or
            props.get("TITLE") or
            "Unknown Location"
        )

        address = (
            props.get("FULL_ADDRESS") or
            props.get("ADDRESS") or
            props.get("LOCATION") or
            "No address available"
        )

        city = props.get("CITY", "")
        state = props.get("STATE", "")
        zip_code = props.get("ZIP", "")

        full_address = f"{address}, {city}, {state} {zip_code}".strip(", ")

        category = (
            props.get("CLASSIFICATION") or
            props.get("TYPE") or
            "General"
        )

        locations.append({
            "name": name,
            "address": full_address,
            "category": category
        })

    return locations


def load_json():
    data_dir = os.path.join("static", "data")
    all_locations = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".geojson"):
            path = os.path.join(data_dir, filename)

            with open(path, "r") as f:
                raw = json.load(f)
                all_locations.extend(extract_locations(raw))

    return all_locations   

#routes for home page
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login_page")
def login_page():
    # Show login/register form here
    return render_template("login_raw.html")

@app.route("/stars")
def stars_page():
    # Show login/register form here
    return render_template("stars.html")

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
        return render_template("rewards_raw.html", error="User already exists")
    
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
            return render_template("rewards_raw.html", username=session["username"])
        else:
            return redirect(url_for('home'))

#logout route 
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

@app.route("/locations")
def locations_page():
    locations = load_json()
    return render_template("locations.html", locations=locations)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
