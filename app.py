from flask import Flask, render_template, request
import flask
from light import *
from heavy import *

app = Flask(__name__, template_folder='template')

@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == 'GET':
        return flask.render_template('index.html')
    elif request.method == 'POST':
        #Carregando método
        peso = (flask.request.form.get('confirm'))
        
        #Quantidade paises
        quantPaises = 21;

        if peso == 'light':
            #Carregando paises
            origem = (flask.request.form.get('country-origin'))
            destino = (flask.request.form.get('country-destiny'))
        
            #Colocando limite
            limite = (int)(flask.request.form.get('limit'))
            
            #Colocando paises em uppercase
            origem = origem.upper()
            destino = destino.upper()

            amplitude = lig.amplitude(origem,destino)

            profundidade = lig.profundidade(origem,destino)

            profunLimitada = lig.prof_limitada(origem, destino, limite)
            
            bidirecional = lig.bidirecional(origem,destino)

            aprofIterativo = lig.aprof_iterativo(origem, destino, quantPaises)

            return render_template('index.html', amplitude=amplitude, profundidade=profundidade, profunLimitada=profunLimitada, bidirecional=bidirecional, aprofIterativo=aprofIterativo, peso=peso)
        elif peso == 'heavy':
            #Carregando paises
            origem = (flask.request.form.get('country-origin'))
            destino = (flask.request.form.get('country-destiny'))
            
            #Colocando paises em uppercase
            origem = origem.upper()
            destino = destino.upper()

            custUniformWay, custUniformValor = hea.custo_uniforme(origem, destino)

            greedyWay, greedyValor = hea.greedy(origem, destino)

            aEstrelaWay, aEstrelaValor = hea.a_estrela(origem, destino)

            return render_template('index.html', custUniformWay=custUniformWay, custUniformValor=custUniformValor, greedyWay=greedyWay, greedyValor=greedyValor, aEstrelaWay=aEstrelaWay, aEstrelaValor=aEstrelaValor, peso=peso)

if __name__ == "__main__":
    app.run(debug=True)