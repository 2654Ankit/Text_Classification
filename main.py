from hate.logger import logging 
from hate.pipeline.data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data ingestion pipeline"

try:
    logging.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logging.exception(e)
    raise e