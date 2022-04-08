from distutils.log import debug
from flask import Flask

app = Flask(__name__)
def make_bold(function):
    def wrapped_function():
        return f"<b>{function()}</b>"
    return wrapped_function

def make_emphasis(function):
    def wrapped_function():
        return f"<em>{function()}</em>"
    return wrapped_function

def make_underlined(function):
    def wrapped_function():
        return f"<u>{function()}</u>"
    return wrapped_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello there. {name}! You are {age} years old"

if __name__ == "__main__":
    app.run(debug=True)