from flask import Flask, render_template

posts = {
    'full_name':'Svetozar Miloshevski',
    'nationality':'Macedonian',
    'email':'svetozar.milosevski@gmail.com',
    'date_of_birth':'5th January 2003'
}


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/liked")
def liked():
    return render_template('liked.html')


@app.route("/account")
def account():
    return render_template('account.html', posts=posts)

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
