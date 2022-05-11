from statistics import mode
import sys
from xml.etree.ElementPath import ops
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import joblib

model = joblib.load("model2.pkl")

app = Flask(__name__, template_folder=".")


@app.route("/")
def index():
    try:
        return render_template("/templates/index.html")
    except:
        return "<h1>Oops!" + ops + "occurred<h1>"



@app.route("/go-test")
def home():
    try:
        return render_template("/templates/go-test.html")
    except:
        ops = str(sys.exc_info)
        return "<h1>Oops!" + ops + "occurred<h1>"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.method == "POST":
            data = {
                key: int(value)
                for value in request.form.values()
                for key in request.form.keys()
            }
            np_array = np.array(list(data.values()))
            prediction = int(model.predict([np_array])[0])
            return render_template(
                "/submit.html", prediction=model.predict([np_array])[0]
            )
    except Exception as e:
        return {"error": str(e)}


# @app.route("/submit", methods=["POST"])
# def submit():
#     return


if __name__ == "__main__":
    app.run(debug=True)
