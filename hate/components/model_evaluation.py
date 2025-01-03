import os
import sys
import keras
import pickle
import numpy as pd
import pandas as pd
from hate.logger import logging
from keras.utils import pad_sequences
from hate.constants import *
from sklearn.metrics import confusion_matrix
from hate.entity.config_entity import ModelEvaluationConfig
from hate.entity.artifact_entity import ModelEvaluationArtifacts,ModelTrainerArtifacts,DataIngestionArtifacts,DataTransformationArtifacts



class ModelEvaluation:
    def __init__(self,model_evaluation_config:ModelEvaluationConfig,model_trainer_artifacts:ModelTrainerArtifacts,data_transformation_artifats:DataTransformationArtifacts):
        """
        param model_evaluation_config: Configuration for model evaluation
        """

        self.model_evaluation_config = model_evaluation_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.data_transformation_artifats = data_transformation_artifats

    def evaluate(self):
        try:
            logging.info("Entering into the evaluate function of moelevaluation class")
            print(self.model_trainer_artifacts.x_test_path)

            x_test=pd.read_csv(self.model_trainer_artifacts.x_test_path,index_col=0)
            print(x_test)
            y_test= pd.read_csv(self.model_trainer_artifacts.y_test_path,index_col=0)

            with open("tokenizer.pickle",'rb') as handle:
                tokenizer = pickle.load(handle)

            load_model = keras.models.load_model(self.model_trainer_artifacts.trained_model_path)

            x_test = x_test['tweet'].astype(str)

            x_test = x_test.squeeze()
            y_test = y_test.squeeze()

            test_sequences = tokenizer.texts_to_sequences(x_test)
            test_sequences_matrix = pad_sequences(test_sequences,maxlen=MAX_LEN)

            print(f'------------{test_sequences_matrix}----------')
            print(f'-----------{x_test.shape}----------')
            print(f'--------------------{y_test.shape}----------')

            accuracy = load_model.evaluate(test_sequences_matrix,y_test)

            logging.info(f"the test accuracy is {accuracy}")

            lstm_prediction = load_model.predict(test_sequences_matrix)

            res = []
            for prediction in lstm_prediction:
                if prediction[0] <0.5:
                    res.append(0)

                else:
                    res.append(1)

            print(confusion_matrix(y_test,res))
            logging.info(f"the confusion matrix is {confusion_matrix(y_test,res)}")

            return accuracy

        except Exception as e:
            raise e

    def initate_model_evaluation(self)->ModelEvaluationArtifacts:

        logging.info("Initate model evaluation")
        try:
            logging.info("loading currently trained model")
            # trained_model = keras.models.load_model(self.model_trainer_artifacts.trained_model_path)

            # with open("tokenizer.pickle",'rb') as handle:
            #     load_tokenizer  = pickle.load(handle)

            
            trained_model_aaccuracy = self.evaluate()
            return trained_model_aaccuracy

        except Exception as e:
             raise e

            
