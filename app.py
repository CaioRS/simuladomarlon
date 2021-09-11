from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.get(url)
    dados = response.json()
    return render_template("index.html",info=dados)


if __name__ == '__main__':
    app.run()
