import os
import sys
import shutil
import roboflow
from SmartCctvHighway.logger import logging
from SmartCctvHighway.exception import AppException
from SmartCctvHighway.entity.config_entity import DataIngestionConfig
from SmartCctvHighway.entity.artifacts_entity import DataIngestionArtifact


##Download the data from internet (Github, google Drive, ...)
# class DataIngestion:
#     def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
#         try:
#             self.data_ingestion_config = data_ingestion_config
#         except Exception as e:
#            raise AppException(e, sys)
        
    

#     def download_data(self)-> str:
#         '''
#         Fetch data from the url
#         '''

#         try: 
#             dataset_url = self.data_ingestion_config.data_download_url
#             zip_download_dir = self.data_ingestion_config.data_ingestion_dir
#             os.makedirs(zip_download_dir, exist_ok=True)
#             data_file_name = os.path.basename(dataset_url)
#             zip_file_path = os.path.join(zip_download_dir, data_file_name)
#             logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")
#             urllib.request.urlretrieve(dataset_url, zip_file_path)
#             logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")
#             return zip_file_path

#         except Exception as e:
#             raise AppException(e, sys)
        

    

#     def extract_zip_file(self,zip_file_path: str)-> str:
#         """
#         zip_file_path: str
#         Extracts the zip file into the data directory
#         Function returns None
#         """
#         try:
#             feature_store_path = self.data_ingestion_config.feature_store_file_path
#             os.makedirs(feature_store_path, exist_ok=True)
#             with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#                 zip_ref.extractall(feature_store_path)
#             logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")

#             return feature_store_path

#         except Exception as e:
#             raise AppException(e, sys)
        


#     def initiate_data_ingestion(self)-> DataIngestionArtifact:
#         logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
#         try: 
#             zip_file_path = self.download_data()
#             feature_store_path = self.extract_zip_file(zip_file_path)

#             data_ingestion_artifact = DataIngestionArtifact(
#                 data_zip_file_path = zip_file_path,
#                 feature_store_path = feature_store_path
#             )

#             logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
#             logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

#             return data_ingestion_artifact

#         except Exception as e:
#             raise AppException(e, sys)


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
           raise AppException(e, sys)
        
    

    def prepare_dataset(self)-> str:
        '''
        Fetch data from the url
        ''' 
        try:
            rf = roboflow.Roboflow(api_key=self.data_ingestion_config.data_roboflow_api_key)
            project = rf.workspace(self.data_ingestion_config.data_roboflow_workspace).project(self.data_ingestion_config.data_roboflow_project_name)
            version = project.version(self.data_ingestion_config.data_roboflow_version)
            dataset = version.download(self.data_ingestion_config.data_roboflow_format)
            logging.info(f"Downloaded Roboflow dataset: {self.data_ingestion_config.data_roboflow_project_name} and extracted it in the dir: {dataset.location}")
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            # os.makedirs(feature_store_path, exist_ok=True) #replace dataset name folder with feature_store
            shutil.move(dataset.location, feature_store_path) #it will create the new folder named feature_store and store all the files inside the dataset folder
            logging.info(f"The Roboflow dataset, Moved to the new dir: {feature_store_path}")
            return feature_store_path
        except Exception as e:
            raise AppException(e, sys)
        

    


    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try: 
            feature_store_path = self.prepare_dataset()

            data_ingestion_artifact = DataIngestionArtifact(
                feature_store_path = feature_store_path
            )

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
