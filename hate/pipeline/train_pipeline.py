from hate.logger import logging
from hate.components.data_ingestion import DataIngestion
from hate.config.configuration import ConfigurationManager
from pathlib import Path
from hate.components.data_transformation import DataTransformation
from hate.entity.config_entity import DataTransformationConfig,DataIngestionConfig
from hate.entity.artifact_entity import DataIngestionArtifacts,DataTransformationArtifacts

from hate.components.data_ingestion import DataIngestion
class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()

    def start_data_ingestion(self)->DataIngestionArtifacts:
        logging.info("Entered the start data_ingestion method of Trainingpipeline class")
        try:
            logging.info("Getting data")
            data_ingestion = DataIngestion (data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initate_data_ingestion()
            return data_ingestion_artifacts
        except Exception as e:
            raise e

    def start_data_transformation(self,data_ingestion_artifacts=DataIngestionArtifacts)->DataTransformationArtifacts:
        logging.info("enterned into start data_transformation method of training pipeline")
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifacts=data_ingestion_artifacts,

                data_transformation_config=self.data_transformation_config
            )

            data_transformation_artifact = data_transformation.initate_data_transformation()
            logging.info("existed the strat_data_transformation methos of training pipeline")
            return data_transformation_artifact
        except Exception as e:
            raise e

    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of training pipeline")

        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )


        except Exception as e:
            raise e



