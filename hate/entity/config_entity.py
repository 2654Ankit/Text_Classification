from dataclasses import dataclass
from pathlib import Path
import os
import gdown
from hate.constants import *



@dataclass
class DataIngestionConfig:
    def __init__(self):
       
        self.source_URL= SOURCE_URL
        self.zip_file_name= ZIP_FILE_NAME
        self.data_ingestion_artifacts_dir : str = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_INGESTION_ARTIFACTS_DIR)
        self.data_artifacts_dir : str = os.path.join(self.data_ingestion_artifacts_dir,DATA_INGESTION_IMBALANCE_DATA_DIR)
        self.new_data_artifacts_dir :str = os.path.join(self.data_ingestion_artifacts_dir,DATA_INGESTION_RAW_DATA_DIR)
        self.zip_file_dir = os.path.join(self.data_ingestion_artifacts_dir)
        self.zip_file_path = os.path.join(self.data_ingestion_artifacts_dir,self.zip_file_name)

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_TRANSFORMATION_ARTIFACTS_DIR)    
        self.TRANSFORMED_DATA_FILE = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,TRANSFORMED_FILE_NAME)
        self.ID = ID
        self.AXIS = AXIS
        self.INPLACE = INPLACE
        self.DROP_COLUMNS = DROP_COLUMNS
        self.CLASS = CLASS
        self.LABEL=  LABEL
        self.TWEET = TWEET
