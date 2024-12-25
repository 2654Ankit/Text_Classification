from hate.entity.config_entity import DataIngestionConfig
from hate.entity.artifact_entity import DataIngestionArtifacts
from hate.logger import logging
import gdown
import os
import zipfile
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config


    def download_file(self)->str:
        try:
            dataset_url = self.data_ingestion_config.source_URL
            zip_download_dir = self.data_ingestion_config.zip_file_path
            os.makedirs(self.data_ingestion_config.data_ingestion_artifacts_dir,exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]

            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e

    def extract_zip_file(self):
        unzip_path = self.data_ingestion_config.zip_file_dir
        # os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.data_ingestion_config.zip_file_path,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
        logging.info("Existed the extract_zip_file mehod")

        return self.data_ingestion_config.data_artifacts_dir,self.data_ingestion_config.new_data_artifacts_dir

    def initate_data_ingestion(self)->DataIngestionArtifacts:
        logging.info("Entered the initate data_ingestion method class")

        try:
            self.download_file()
            logging.info("fetched the data from drive")
            imbalance_data_file_path,raw_data_file_path = self.extract_zip_file()

            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalance_data_file_path=imbalance_data_file_path,
                raw_data_file_path=raw_data_file_path
            )
            logging.info(f"data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts
            

        except Exception as e:
            raise e
