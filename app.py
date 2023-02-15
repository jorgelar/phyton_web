from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

SECRET_KEY = "pudim"
app.config.from_object(__name__)

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

# USER MOCKS
USERNAME = "admin"
PASSWORD = "admin"

@app.route('/')
def exibir_entradas():
    #pegar posts no banco
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/inserir', methods=["POST"])
def inserir_entradas():
    novo_post = {
        "titulo": request.form['titulo'],
        "texto": request.form['texto']
    }
    posts.append(novo_post)
    request.form['titulo']
    request.form['texto']
    return redirect(url_for('exibir_entradas'))

@app.route('/login', methods=["get", "post"])
def login():
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logado'] = True
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos!"
    return render_template("login.html", erro = erro)

@app.route('/pudim')
def pudim():
    return "<h1>Eu gosto de pudim!</h1>"

@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('exibir_entradas'))