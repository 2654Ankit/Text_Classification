from hate.logger import logging
from hate.components.data_ingestion import DataIngestion
from hate.config.configuration import ConfigurationManager
from pathlib import Path
from hate.components.data_transformation import DataTransformation
from hate.entity.config_entity import DataTransformationConfig,DataIngestionConfig,ModelTrainerConfig
from hate.entity.artifact_entity import DataIngestionArtifacts,DataTransformationArtifacts,ModelTrainerArtifacts
from hate.components.model_trainer import ModelTrainer
from hate.components.data_ingestion import DataIngestion
class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()

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

    def start_model_trainer(self,data_transformation_artifacts:DataTransformationArtifacts)->ModelTrainerArtifacts:
        logging.info("Enteed the model trainer methos of trainpipeline")

        try:
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config,data_transformation_artifact=data_transformation_artifacts)

            model_trainer_artifacts = model_trainer.initate_model_trainer()
            logging.info("Existed the start_model_trainer method od pipeline lcass")
            return model_trainer_artifacts

        except Exception as e:
            raise e



    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of training pipeline")

        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )

            model_trainer_artifacts = self.start_model_trainer(
                data_transformation_artifacts=data_transformation_artifacts
            )

        except Exception as e:
            raise e



