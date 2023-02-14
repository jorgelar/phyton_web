from flask import Flask, render_template

app = Flask(__name__)

#POSTS MOCK
posts = [
    {
        "Titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "Titulo": "Post 2",
        "texto": "Meu segundo Post"
    },
    {
        "Titulo": "Post 3",
        "texto": "Meu terceiro Post"
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/pudim')
def pudim():
    return "<h1>Eu gosto de pudim!</h1>"
