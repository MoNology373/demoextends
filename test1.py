from flask import Flask, request, render_template, url_for, session
from werkzeug.utils import redirect


app = Flask(__name__)


# @app.template_filter('reverse')
# def reverse_filter(s):
# return s[::-1]
# filter lọc hiển thị mảng ngược lại
# arr = [6, 5, 4, 7, 8, 9]
@app.route("/index")
def index():
    return render_template("index.html")


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "mc2eu8r2f2;f2]./"

@app.route('/')
def user():
    if 'username' in session:
        return redirect(url_for("index", name = session['username']))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return "You're already logged in"
    else:
        if request.method == 'POST':
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            if session['username'] == "admin" and session['password'] == "123":
                return redirect(url_for('index', name=session['username']))
            else:
                return redirect(url_for("loginFailed", name="idiot"))
    return render_template("login.html")
    #     <form method="post">
    #         <p><input type=text name=username>
    #         <p><input type=submit value=Login>
    #     </form>
    # '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# @app.route("/login", methods=['post', 'get'])
# def login():
#     if request.method == 'POST':
#         username = request.form["username"]
#         password = request.form["password"]
#         if username == "admin" and password == "123":
#             return redirect(url_for("loginSuccess", name=username))
#         else:
#             return redirect(url_for("loginFailed", name="idiot"))
#     return render_template("login.html")
#
#
# @app.route("/login-success")
# def loginSuccess():
#     return render_template("login-succeeded.html")
#
#
@app.route("/login-failed", methods=['post', 'get'])
def loginFailed():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['username'] == "admin" and session['password'] == "123":
            return redirect(url_for('index', name=session['username']))
        else:
            return redirect(url_for("loginFailed", name="idiot"))
    return render_template("login-failed.html")


# @app.template_filter("even")
# def select_even(arr):
# return [a for a in arr if a>0 and a%2 == 0]

if __name__ == "__main__":
    app.run()
