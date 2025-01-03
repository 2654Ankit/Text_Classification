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


# model trainer constants
MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"
TRAINED_MODEL_DIR = "trained_model"
TRAINED_MODEL_NAME = "model.h5"
X_TEST_FILE_NAME = "x_test.csv"
Y_TEST_FILE_NAME = "y_test.csv"

X_TRAIN_FILE_NAME = "x_train.csv"

RANDOM_STATE = 42
EPOCH = 1
BATCH_SIZE = 128
VALIDATION_SPLIT = 0.2


# Model Architecture Constants
MAX_WORDS = 50000
MAX_LEN = 300
LOSS = 'binary_crossentropy'
METRICS = ['accuracy']
ACTIVATION = 'sigmoid'


# Model evaluation constant

MODEL_EVALUATION_ARTIFACTS_DIR = 'ModelEvaluationArtifacts'
BEST_MODEL_DIR = 'best_model'
MODEL_EVALUATION_FILE_NAME = 'loss.csv'
MODEL_NAME = 'model.h5'
APP_HOST = '0.0.0.0'
APP_PORT=8080