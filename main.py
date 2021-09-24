from flask import Flask, render_template, request
app = Flask(__name__)
monki_arquivo = open("mamacos.json")
monki_geral = monki_arquivo.monki_numbers

@app.route("/" , methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/monkey_number', methods=['POST'])
def monkey_number():
  pais=request.form['pais'] 
  return render_template('brasil.html', Brasil= monki_brasil)


if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8080)
