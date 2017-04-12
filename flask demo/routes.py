from flask import Flask, render_template

# Main app:
app = Flask(__name__)

# Home route:
@app.route('/')
def home():
    return render_template("home.html")

# Welcome route:
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':
    app.run()
