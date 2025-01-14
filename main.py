from hate.logger import logging 
# from hate.pipeline.data_ingestion import DataIngestion
# from hate.pipeline.train_pipeline import DataTrainingPipeline
from hate.pipeline.train_pipeline import TrainPipeline

from fastapi import FastAPI
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
from fastapi.responses import RedirectResponse
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.constants import *
from flask import Flask,request,app,jsonify,url_for,render_template

text:str = "What is machine learning"
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')



@app.route("/train")
def train():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        return render_template("train.html",taining = " Training id done")

    except Exception as e:
        raise e

@app.route("/predict",methods=['POST'])

def predict():
    text  = request.form.get('text')
    try:
        obj = PredictionPipeline()
        print("pipelone")
        text = obj.run_pipeline(text)
        return render_template("home.html",prediction_text=text)

    except Exception as e:
        raise e


if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)

