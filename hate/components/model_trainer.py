import os
import sys
import pickle
import pandas as pd
from hate.logger import logging
from hate.constants import *
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from hate.entity.config_entity import ModelTrainerConfig
from hate.entity.artifact_entity import ModelTrainerArtifacts,DataTransformationArtifacts
from hate.ml.model import ModelArchitecture

class ModelTrainer:
    def __init__(self,data_transformation_artifact:DataTransformationArtifacts,model_trainer_config:ModelTrainerConfig):
        self.data_transformation_artifacts = data_transformation_artifact
        self.model_trainer_config  = model_trainer_config

    def splitting_data(self,csv_path):
        try:
            logging.info("entered the splitting_data function")
            logging.info("Reading the data")
            df = pd.read_csv(csv_path,index_col=False)
            logging.info("Splitting the data into x and y")
            x = df[TWEET]
            y = df[LABEL]

            logging.info("APPLYING TRAIN TEST SPLIT ON THE DATA")
            x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=RANDOM_STATE)

            print(len(x_train),len(y_train))
            print(len(x_test),len(y_test))
            print(type(x_train),type(y_train))
            logging.info("Existed the splitting the data function")

            return x_train,x_test,y_train,y_test

        except Exception as e:
             raise e


    def tokenizing(self,x_train):
        try:
            logging.info("Applying tokenization on the data")
            tokenizer = Tokenizer(num_words=self.model_trainer_config.MAX_WORDS)
            tokenizer.fit_on_texts(x_train)
            sequences = tokenizer.texts_to_sequences(x_train)
            logging.info(f"Converting text to sequences: {sequences}")
            sequences_metrix = pad_sequences(sequences,maxlen = self.model_trainer_config.MAX_LEN)
            logging.info(f"The sequences metrix is : {sequences_metrix}")
            return sequences_metrix,tokenizer

        except Exception as e:
             raise e


    def initate_model_trainer(self)->ModelTrainerArtifacts:
        try:
            logging.info("Entered the initate_model_trainer function")
            x_train,x_test,y_train,y_test = self.splitting_data(csv_path=self.data_transformation_artifacts.transformed_data_path)
            model_architecture =ModelArchitecture()
            model = model_architecture.get_model()

            logging.info(f"x_train is : {x_train.shape}")
            logging.info(f"x_test size is {x_test.shape}")

            sequences_metrix,tokenizer = self.tokenizing(x_train)

            logging.info("entered into model training")

            model.fit(sequences_metrix,y_train,batch_size = self.model_trainer_config.BATCH_SIZE,
            epochs = self.model_trainer_config.EPOCH,
            validation_split =self.model_trainer_config.VALIDATION_SPLIT)

            logging.info("model training finished")
            with open('tokenizer.pickle','wb') as handle:
                pickle.dump(tokenizer,handle,protocol=pickle.HIGHEST_PROTOCOL)
            os.makedirs(self.model_trainer_config.TRAINED_MODEL_DIR,exist_ok=True)


            logging.info("saving the model")
            model.save(self.model_trainer_config.TRAINED_MODEL_PATH)
            x_test.to_csv(self.model_trainer_config.X_TEST_DATA_PATH)
            y_test.to_csv(self.model_trainer_config.Y_TEST_DATA_PATH)
            x_train.to_csv(self.model_trainer_config.X_TRAIN_DATA_PATH)

            model_trainer_artifacts = ModelTrainerArtifacts(
                trained_model_path=self.model_trainer_config.TRAINED_MODEL_PATH,
                x_test_path=self.model_trainer_config.X_TEST_DATA_PATH,
                y_test_path=self.model_trainer_config.Y_TEST_DATA_PATH
            )

            logging.info("Returning the ModelTrainerArtifacts")

            return model_trainer_artifacts

        except Exception as e:
            raise e

