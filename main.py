from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/" , methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/monkey_number', methods=['GET', 'POST'])
def monkey_number():
  brasil=request.form['brasil'] 
  return render_template('brasil.html', Brasil= 118)


if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8080)