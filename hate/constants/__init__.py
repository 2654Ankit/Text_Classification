from pathlib import Path
import os
from datetime import datetime

#COMMON CONSTANTS
TIMESTAMP:str=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts",TIMESTAMP)
SOURCE_URL = "https://drive.google.com/file/d/1J8Gd0d4YwOhdkN0SALD1CBRe-argMey_/view?usp=drive_link"

LABEL = "label"
TWEET = "tweet"
ZIP_FILE_NAME = "dataset.zip"
LOCAL_FILE_PATH = os.path.join(ARTIFACTS_DIR,"dataset")
CONFIG_FILE_PATH = Path("hate/config/config.yaml")
# PARAMS_FILE_PATH = Path("params.yaml")



# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"



# Data transformation constants
DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
TRANSFORMED_FILE_NAME = "final.csv"
DATA_DIR = "data"
ID = "id"
AXIS = 1
INPLACE = True
DROP_COLUMNS = ['Unnamed: 0','count','hate_speech','offensive_language','neither']
CLASS = 'class'