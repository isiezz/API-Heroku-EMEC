from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("mamacos.json", 'r') as file:
  monki_arquivo = json.load(file)

@app.route("/" , methods=['GET', 'POST'])
def index():
  chaves = monki_arquivo.keys()
  return render_template('index.html', chaves=chaves)

@app.route('/mamacos/<string:pais>', methods=['GET'])
def monkey_number(pais):
  resultado = monki_arquivo[pais]
  # Tratar erros com Try em Dicionario
  return render_template('pais.html', resultado=resultado, pais=pais)


if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8080)
