from flask import Flask, render_template, request

main = Flask(__name__)


@main.route("/")
def index():
    return "Hello World!"

@main.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("hello.html")


if __name__ == "__main__":
    main.run()
