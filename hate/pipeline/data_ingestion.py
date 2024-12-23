from hate.logger import logging
from hate.components.data_ingestion import DataIngestion
from hate.config.configuration import ConfigurationManager
from pathlib import Path

STAGE_NAME = "Dta ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()

            data_ingestion =DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()

            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e


# if __name__ =='__main__':
#     try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")

#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f">>stage {STAGE_NAME} completed <<<<<<<<<")
#     except Exception as e:
#         logger.exception(e)
#         raise e
