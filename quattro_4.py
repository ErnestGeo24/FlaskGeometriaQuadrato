from flask import Flask, render_template,request
import re
import math
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("quattro_40.html")

@app.route('/Geometria', methods = ['POST'])
def geo():
    geometria = request.form.getlist("geometria")
    lato = float(request.form['lato'])
    if "Area" in geometria and "Diagonale" in geometria:
        area = lato **2
        diagonale = lato * math.sqrt(2)
        return render_template('quattro_41.html',Lato = lato, Area = area, Diagonale = diagonale)
    elif "Area" in geometria:
        area = lato **2
        return render_template('quattro_42.html',Lato = lato, Area = area)
    elif "Diagonale" in geometria:
        diagonale = lato * math.sqrt(2)
        return render_template('quattro_43.html',Lato = lato, Diagonale = diagonale)
    else:
        return render_template("quattro_44.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)