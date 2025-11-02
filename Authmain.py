from flask import Flask,render_template,request,redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="crazy_secret_key"

app.config["SQLAlchemy_DATABASE_URI"]="sqlite:///Database.db"
app.config["SQLAlchemy_TRACK_MPDIFICATIONS"]=False;
db=SQLAlchemy(app)

#routes for home page
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("/dashboard"))
    return render_template('index.html')





if __name__ in '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
