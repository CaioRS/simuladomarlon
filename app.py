from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    lista= []

    for x in range(0,6):
        url = "https://meme-api.herokuapp.com/gimme"
        response = requests.get(url)
        dados = response.json()
        lista.append(dados)

    print (lista)
    return render_template("index.html",info=lista)



if __name__ == '__main__':
    app.run()
