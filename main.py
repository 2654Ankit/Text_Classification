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
# STAGE_NAME = "Data ingestion pipeline"

# try:
#     logging.info(f">>>> stage {STAGE_NAME} started <<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logging.info(f">>>stage {STAGE_NAME} completed <<<<<")

# except Exception as e:
#     logging.exception(e)
#     raise e

# STAGE_NAME = "Training pipeline"

# try:
#     logging.info(f">>>> stage {STAGE_NAME} started <<<<<")
#     data_ingestion_artifacts = self.start
#     obj = DataTrainingPipeline()

#     obj.start_data_transformation(
#         data_ingestion_artifacts=data
#     )
#     logging.info(f">>>stage {STAGE_NAME} completed <<<<<")

# except Exception as e:
#     logging.exception(e)
#     raise e



# obj = TrainPipeline()
# obj.run_pipeline()


text:str = "What is machine learning"
app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        return Response("Training sucessful!")

    except Exception as e:
        raise e

@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        print("pipelone")
        text = obj.run_pipeline(text)
        return text

    except Exception as e:
        raise e
if __name__ =="__main__":
    uvicorn.run(app,host=APP_HOST,port=APP_PORT)

