from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1>Home Page</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/<word>')
def welcome_word(word):
    return f"Welcome {word}"







if __name__ == "__main__":
    app.run(debug=True)