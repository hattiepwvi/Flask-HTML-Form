from flask import Flask, render_template, request
# flask 的 request和 python 的requests 不一样
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def receive_data():
    name = request.form['username']
    password = request.form['password']
    return render_template("login.html", name=name, password=password)


if __name__ == "__main__":
    app.run(debug=True)