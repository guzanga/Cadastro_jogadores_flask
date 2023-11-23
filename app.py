from flask import Flask, render_template, request, redirect

app = Flask(__name__)
class CardJogadores:
    def __init__(self, nome,jogo , posicao , rank):
        self.nome= nome
        self.jogo= jogo
        self.posicao = posicao
        self.rank = rank

lista = []

@app.route('/jogadores')
def jogadores():
    return render_template("index.html", ListaJogadores=lista)

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html",)


# como aqui usa metodos devo colocar o metodo que a rota ira utilzar
@app.route('/criar', methods=["POST"])
def criar():
    nome = request.form['nome']
    jogo = request.form['jogo']
    posicao = request.form['posicao']
    rank = request.form['rank']
    obj= CardJogadores( nome, jogo, posicao, rank)
    lista.append(obj)
    return redirect("/jogadores")

if __name__ == '__main__':
    app.run()
