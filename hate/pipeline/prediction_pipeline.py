import os
import io
import sys
import keras
import pickle
from PIL import Image
from hate.logger import logging
from hate.constants import *
from keras.utils import pad_sequences
from hate.components.data_transformation import DataTransformation
from hate.entity.config_entity import DataTransformationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts,ModelTrainerArtifacts

class PredictionPipeline:
    def __init__(self):
        self.model_name = MODEL_NAME
        self.model_path = os.path.join("artifacts",
        "PreditModel")
        self.model_trainer_artifacts = ModelTrainerArtifacts
        self.data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig,data_ingestion_artifacts=DataIngestionArtifacts)
        print("hii")
    def predict(self,text):
        logging.info("Running the prediction function")
        print("hello")

        try:
            load_model = keras.models.load_model("artifacts/01_03_2025_17_56_15/ModelTrainerArtifacts/model.h5")

            with open("tokenizer.pickle","rb") as handle:
                load_tokenizer = pickle.load(handle)

            text = self.data_transformation.cocat_data_cleaning(text)

            text = [text]
            print("text is ",text)
            seq = load_tokenizer.texts_to_sequences(text)
            padded = pad_sequences(seq,maxlen=300)
            print(seq)
            pred = load_model.predict(padded)
            print("pred",pred)

            if pred >0.5:
                print("hate and abusive")
                return "hate and abusive"
            else:
                print("no hate")
                return "no hate"

        except Exception as e:
            raise e
    def run_pipeline(self,text):
        logging.info("entered into run_pipeline method of prepictionpipeline class")

        try:
            predicted_text = self.predict(text)
            logging.info("existed from run_pipeline of prediction pipeline class")

            return predicted_text

        except Exception as e:
             raise e