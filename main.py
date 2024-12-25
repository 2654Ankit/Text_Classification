from hate.logger import logging 
# from hate.pipeline.data_ingestion import DataIngestion
# from hate.pipeline.train_pipeline import DataTrainingPipeline
from hate.pipeline.train_pipeline import TrainPipeline


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



obj = TrainPipeline()
obj.run_pipeline()