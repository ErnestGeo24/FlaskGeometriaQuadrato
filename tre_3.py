from flask import Flask, render_template,request
import re
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("due_20.html")

@app.route('/Geometria', methods = ['GET'])
def geo():
    geometria = request.args.get("geometria")
    lato = float(request.args.get('lato'))
    if geometria == "Area":
        area = lato **2
        return render_template('result_2.html',Base = base,Altezza=altezza, Area = area)
    else:
        diagonale = math.sqrt(base ** 2 + altezza ** 2)
        return render_template('result_3.html',Base = base,Altezza=altezza, Diagonale = diagonale)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)