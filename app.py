from flask import Flask
from flask import render_template
import numpy as np
import pickle
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calk", methods=["POST"])
def calk():
    request.form("calk")
    with open("predict_population.pickle", mode="rb") as fp:
        model = piclie.load(fp)
        reqsult = model.
    # print(calk)
    return render_template("calk.html")


if __name__ == "__main__":  # ファイル直接実行の時
    app.run(debug=True)
