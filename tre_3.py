from flask import Flask, render_template,request
import re
import math
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("tre_30.html")

@app.route('/Geometria', methods = ['GET'])
def geo():
    geometria = request.args.get("geometria")
    lato = float(request.args.get('lato'))
    if geometria == "Area":
        area = lato **2
        return render_template('tre_31.html',Lato = lato, Area = area)
    else:
        diagonale = lato * math.sqrt(2)
        return render_template('tre_32.html',Lato = lato, Diagonale = diagonale)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)