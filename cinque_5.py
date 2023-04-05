from flask import Flask,render_template,request
import math
app = Flask(__name__)


import datetime
@app.route('/')
def home():
    return render_template('cinque_50.html')

@app.route('/data', methods = ["GET"])
def data():
    figura_selezionata = request.args.get('figure')
    if figura_selezionata == 'cerchio':
        figura = "images/cerchio.png"
    elif figura_selezionata == 'rettangolo':
        figura = "images/rettangol.png"
    elif figura_selezionata == 'quadrato':
        figura = "images/quadrato.png"
    elif figura_selezionata == 'pentagono':
        figura = "images/pentagono.png"
    return render_template("cinque_51.html", percorso = figura)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)