from trainingModel import trainModel,trainValidation
from predictFromModel import prediction_validation,prediction 
import os
import pandas as pd
from application_logger import logging
from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/file",methods=["GET","POST"])
@cross_origin()
def file():
    try:
        if request.method == 'POST' and request.files:
                #self.log.log(self.file_object,f"File recived...")
            file = request.files['File']
            file.save(f"Recived_file/{file.filename}")
               #self.log.log(self.file_object,f"Files saved..")
            return render_template('index.html', output = f"{file.filename} \t File uploaded successfuly...")
    except Exception as e:
            #self.log.log(self.file_object,f"Error while reciving file..:: {e}")
        raise Exception
@app.route("/predict",methods=["GET","POST"])
@cross_origin()
def predict():
    try:
        for i in os.listdir('Recived_file'):
            if i!='Bad_file':
                file = i
            #self.log.log(self.file_object,"-----------Prediction validation entered-------")
        p = prediction_validation(file=file)
        p.prediction_val()
            #self.log.log(self.file_object,"-----------Prediction validation exited-------")
            #self.log.log(self.file_object,"-----------Prediction entered-------")
        pp = prediction(file=file)
        pp.predictFromModel()
            #self.log.log(self.file_object,"-----------Prediction exited-------")
        return render_template('index.html', prediction_output = "Prediction done successfuly and prediction file saved at :: Prediction_output/Predictions.csv")
    except Exception as e:
            #self.log.log(self.file_object,f"<<<<Error occured :: {e}>>>>")
        raise Exception
    
@app.route("/train",methods=["GET","POST"])
@cross_origin()
def train(file='day.csv'):
    try:
            #self.log.log(self.file_object,"-----------Training started----------")
        t_val = trainValidation(file=file)
        t_val.train_validation()
            #self.log.log(self.file_object,"-----------Training validation exited-------")
        t_train = trainModel()
        t_train.trainingModel()
            #self.log.log(self.file_object,"-----------Training model exited-------")
        return render_template('index.html',train_output = "Model saved at models directory...")
    except Exception as e:
            #self.log.log(self.file_object,f"Error in train :: {e}")
        raise Exception
        

if __name__ == '__main__':
    app.run(debug=True)