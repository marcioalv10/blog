from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")



posts = [
    {
        "title":"O meu primeiro Post",
        "body":"Texto do Post",
        "author":"Feulo",
        "created": datetime(2022,7,25)
    },
    {
        "title":"O meu segundo Post",
        "body":"Texto do Post",
        "author":"Marcio",
        "created": datetime(2022,7,26)
    }
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)



def hello():
    return "Hello world"

@app.route("/meucontato")
def meucontato():
    return "Marcio Alves"

@app.route("/mycontato")
def mycontato():
    return render_template('index.html', email="marcio.elx@gmail")

@app.route("/contato")
def contato():
    return """<html>
        <head>
            <title>Contatos</title>

        </head>
        <body>
            <h1>Marcos</h1>   
            <h2>Tecnico em mecanica</h2> 
            <h1>Faculdade Cotemig</h1>   
            <a href= "https://www.cotemig.com">link</a>

           
        </body>
    </html>
    """

