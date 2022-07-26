from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
@app.route("/hello")

def hello():
    return "Hello world"

@app.route("/meucontato")
def meucontato():
    return "Marcio Alves"

@app.route("/mycontato")
def mycontato():
    return render_template('index.html')

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

            <ol>
                <li>item 1</li>
                <li>item 2</li>
                <li>item 3</li>
            </ol>
           
        </body>
    </html>
    """

