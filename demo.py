from hate.logger import logging
from hate.exception import CustomException
import sys
# logging.info("welcome to projects")

# try:
#     a= 7/"0"
# except Exception as e:
#     raise CustomException(e,sys) from e

import os
import zipfile
import gdown
from hate import logger
from hate.config.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            
            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config

    



class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self) ->str:
        # Fetch the data from the url

        try:
            dataset_url  = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)




try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    print(data_ingestion_config)
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()

except Exception as e:
    raise e
