from flask import Flask, render_template, request, redirect, url_for
from PyDictionary import PyDictionary
from flask_sqlalchemy import SQLAlchemy

dictionary = PyDictionary()
count = 0
history = []

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///vocabulary.db"
db = SQLAlchemy(app)

class vocabulary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(200), nullable=False)
    meaning = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Word %r>" % self.id 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/dictionary")
def mydictionary():
    return render_template("dictionary.html", f="ما هي الكلمة التي تريد معرفة معناها")

@app.route("/dictionary", methods=['POST'])
def my_dictionary_post():
    global count
    global history
    if request.method == "POST":
        text = request.form['text']
        history.append(text)
        text = dictionary.meaning(text)
        hist_r = str(history).strip('[]')
        count += 1
        return render_template("dictionary.html", d=text, num=count, f="", hist=hist_r)
    else:
        return redirect(url_for("dictionary"))



if __name__ == "__main__":
    app.run(debug=True)
