import os, sys
import shutil
from SmartCctvHighway.logger import logging
from SmartCctvHighway.exception import AppException
from SmartCctvHighway.entity.config_entity import DataValidationConfig
from SmartCctvHighway.entity.artifacts_entity import (DataIngestionArtifact,
                                                  DataValidationArtifact)



class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys) 
        

    
    def validate_all_files_exist(self) -> bool:
        try:
            
            validation_status = None
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            for file in self.data_validation_config.required_file_list:
                if file not in all_files:
                    validation_status = False
                else:
                    validation_status = True
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            return validation_status

        except Exception as e:
            raise AppException(e, sys)
        

    
    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact} and The state is: {status}")

            # if status:
            #     shutil.move(self.data_ingestion_artifact.feature_store_path, os.getcwd())
            #     # shutil.copytree(self.data_ingestion_artifact.feature_store_path, os.getcwd()+'car_object_raw-1')
            #    logging.info(f"Move the zip file to : {os.getcwd()}")
            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)
