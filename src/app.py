from flask import Flask
# pip freeze > requirements.txt !!!
app = Flask(__name__)


def be_polite(fn):
    def wrapper():
        return "Have a nice  day. "+fn()

    return wrapper


@be_polite
def greet():
    return "My name is Clément."


@be_polite
def rage():
    return "GRrrr"


@app.route('/')
def hello_world():  # put application's code here
    return greet()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
