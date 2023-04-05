from flask import Flask,render_template,request
import random
app = Flask(__name__)


import datetime
@app.route('/')
def home():
    return render_template('sei_60.html')

@app.route('/data', methods = ["POST"])
def data():
    numero = random.randint(0,3)
    if numero == 0:
        figura = "images/cerchio.png"
        return render_template("sei_61.html", percorso = figura)
    elif numero == 1:
        figura = "images/rettangol.png"
        return render_template("sei_62.html", percorso = figura)
    elif numero == 2:
        figura = "images/quadrato.png"
        return render_template("sei_63.html", percorso = figura)
    elif numero == 3:
        figura = "images/pentagono.png"
        return render_template("sei_64.html", percorso = figura)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)