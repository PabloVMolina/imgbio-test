from flask import *

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

# Hello (access):
@app.route('/hello')
def hello():
    return render_template("hello.html")

# Log in:
@app.route('/log', methods=['GET', 'POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            return redirect(url_for('hello'))
    return render_template("log.html", error=error)

if __name__ == '__main__':
    app.run()
