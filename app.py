from statistics import mode
import sys
from xml.etree.ElementPath import ops
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    try:
        return render_template('/index.html')
    except:
        ops = str(sys.exc_info)
        return('<h1>Oops!'+ops+'occurred<h1>')



@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.method == "POST":
            Age = request.form["Age"]
            RestingBP = request.form["RestingBP"]
            Cholesterol = request.form["Cholesterol"]
            MaxHR = request.form["MaxHR"]
            Oldpeak = request.form["Oldpeak"]
            ChestPainType_ASY = request.form["ChestPainType_ASY"]
            ChestPainType_ATA = request.form["ChestPainType_ATA"]
            FastingBS_0 = request.form["FastingBS_0"]
            FastingBS_1 = request.form["FastingBS_1"]
            RestingECG_LVH = request.form["RestingECG_LVH"]
            RestingECG_Normal = request.form["RestingECG_Normal"]
            RestingECG_ST = request.form["RestingECG_ST"]
            ExerciseAngina_N = request.form["ExerciseAngina_N"]
            ExerciseAngina_Y = request.form["ExerciseAngina_Y"]
            ST_Slope_Down = request.form["ST_Slope_Down"]
            ST_Slope_Flat = request.form["ST_Slope_Flat"]
            ST_Slope_Up = request.form["ST_Slope_Up"]
            data = np.array([['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak', 'ChestPainType_ASY', 'ChestPainType_ATA',
    'FastingBS_0', 'FastingBS_1', 'RestingECG_LVH', 'RestingECG_Normal', 'RestingECG_ST'
    , 'ExerciseAngina_N', 'ExerciseAngina_Y', 'ST_Slope_Down', 'ST_Slope_Flat', 'ST_Slope_Up']])
            my_prediction = model.predict(data)
            return render_template('/submit.html',prediction=my_prediction)
    except:
        ops = str(sys.exc_info())


# @app.route("/submit", methods=["POST"])
# def submit():
#     return




if __name__ == "__main__":
    app.run(debug=True)