from flask import Flask, render_template, request

app = Flask(__name__)

vocabulary = ['apple', 'banana', 'cherry']

@app.route('/', methods=["GET"])
def home():

    new_word = request.form.get('word')
    vocabulary.append(new_word)
    return render_template("home.html", vocabulary=vocabulary)

if __name__ == '__main__':
    app.run(debug=True)
