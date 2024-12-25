import os
import re
import sys
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from hate.logger import logging

from hate.entity.config_entity import DataTransformationConfig
from hate.entity.artifact_entity import (DataIngestionArtifacts,DataTransformationArtifacts)
class DataTransformation:
    def __init__(self,data_transformation_config: DataTransformationConfig,data_ingestion_artifacts: DataIngestionArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts

    def imbalanced_data_cleaning(self):
        try:
            logging.info("Entered into the imbalanced_data_cleaning function")
            
            imbalance_data = pd.read_csv(self.data_ingestion_artifacts.imbalance_data_file_path)

            imbalance_data.drop(self.data_transformation_config.ID,axis=self.data_transformation_config.AXIS,inplace=self.data_transformation_config.INPLACE)
            logging.info(f"Existed the imbalance data_cleaning function and returned imbalanced data {imbalance_data}")
            return imbalance_data

        except Exception as e:
            raise e

    def raw_data_cleaning(self):
        try:
            logging.info("Entered into raw data cleaning function")
            raw_data = pd.read_csv(self.data_ingestion_artifacts.raw_data_file_path)
            raw_data.drop(self.data_transformation_config.DROP_COLUMNS,axis=self.data_transformation_config.AXIS,inplace=self.data_transformation_config.INPLACE)

            raw_data[raw_data[self.data_transformation_config.CLASS]==0][self.data_transformation_config.CLASS]=1

            # replace 0 to 1
            raw_data[self.data_transformation_config.CLASS].replace({0:1},inplace=True)

            #replace 2 to 0
            raw_data[self.data_transformation_config.CLASS].replace({2:0},inplace=True)

            #change the name of class to label
            raw_data.rename(columns={self.data_transformation_config.CLASS:self.data_transformation_config.LABEL},inplace=True)
            logging.info(f"existed the raw data cleaning function and returned the raw data {raw_data}")
            return raw_data

        except Exception as e:
            raise e

    def concat_dataframe(self):
        try:
            logging.info("Entered into the concat_dataframe function")

            frame = [self.raw_data_cleaning(),self.imbalanced_data_cleaning()]
            df = pd.concat(frame)
            print(df.head())
            # logging.info(f"returned the concated data {df}")
            return df

        except Exception as e:
            raise e



    def cocat_data_cleaning(self,words):    
        try:
            logging.info("enterned the concat_data_cleaning function")
            stemmer = nltk.SnowballStemmer("english")
            stopword = set(stopwords.words("english"))
            
            words = str(words).lower()
            words = re.sub('\[.*?\]','',words)
            words = re.sub('https?://\S+|www\.\S+','',words)
            words = re.sub('<.*?>+','',words)
            words = re.sub('[%s]' % re.escape(string.punctuation),'',words)
            words = re.sub('\n','',words)
            words = re.sub('\w*\d\w*','',words)
            words = [word for word in words.split(' ') if words not in stopword]
            words = " ".join(words)
            words = [stemmer.stem(word) for word in words.split(' ')]
            words = " ".join(words)

            return words

        except Exception as e:
            raise e


    
    def initate_data_transformation(self)-> DataTransformationArtifacts:
        try:
            logging.info("entered inthe initate_data_transformation methos of Data transformation")

            self.imbalanced_data_cleaning()
            logging.info("entered into raw data cleaning function")
            self.raw_data_cleaning()
            df = self.concat_dataframe()
            
            logging.info("entered into cocat_data_cleaning funnction")
            df[self.data_transformation_config.TWEET] = df[self.data_transformation_config.TWEET].apply(self.cocat_data_cleaning)
            print(df.head(10))

            os.makedirs(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,exist_ok=True)

            df.to_csv(self.data_transformation_config.TRANSFORMED_DATA_FILE,index=False,header=True)

            data_transformation_artifact = DataTransformationArtifacts(
                transformed_data_path=self.data_transformation_config.TRANSFORMED_DATA_FILE
            )

            logging.info("returning the DataTransformationArtifact")
            return data_transformation_artifact

        except Exception as e:
            raise e


