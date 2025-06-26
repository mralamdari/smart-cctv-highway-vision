# import os,sys
# import yaml
# from SmartCctvHighway.logger import logging
# from SmartCctvHighway.exception import AppException
# from SmartCctvHighway.entity.config_entity import (ModelTrainerConfig, 
#                                                    DataIngestionConfig)
# from SmartCctvHighway.entity.artifacts_entity import ModelTrainerArtifact

# print(ModelTrainerConfig.model_trainer_dir)
# print(DataIngestionConfig.feature_store_file_path)
# print(os.path.exists(f'{DataIngestionConfig.feature_store_file_path}\data.yaml'), DataIngestionConfig.feature_store_file_path)
# # artifacts\06_26_2025_18_19_21\data_ingestion\feature_store\traffic_images_dataset_v1\data.yaml
# class ModelTrainer:
#     def __init__(
#         self,
#         model_trainer_config: ModelTrainerConfig,
#     ):
#         self.model_trainer_config = model_trainer_config


    
#     def initiate_model_trainer(self,) -> ModelTrainerArtifact:
#         logging.info("Entered initiate_model_trainer method of ModelTrainer class")

#         try:    
#             os.system(f'%cd ')
#             os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
#             os.system(f'!yolo train task=detect model={self.model_trainer_config.weight_name} data=../data.yaml epochs={self.model_trainer_config.no_epochs} batch={self.model_trainer_config.batch_size} imgsz=640 --plots project={self.model_trainer_config.model_trainer_dir}')

#             os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
#             os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
#             os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
#             os.system("rm -rf yolov5/runs")
#             os.system("rm -rf train")
#             os.system("rm -rf test")
#             os.system("rm -rf data.yaml")

#             model_trainer_artifact = ModelTrainerArtifact(
#                 trained_model_file_path="yolov5/best.pt",
#             )

#             logging.info("Exited initiate_model_trainer method of ModelTrainer class")
#             logging.info(f"Model trainer artifact: {model_trainer_artifact}")

#             return model_trainer_artifact


#         except Exception as e:
#             raise AppException(e, sys)




from SmartCctvHighway.logger import logging
from SmartCctvHighway.exception import AppException
from SmartCctvHighway.entity.config_entity import DataValidationConfig
from SmartCctvHighway.entity.config_entity import DataIngestionConfig
from SmartCctvHighway.entity.artifacts_entity import DataIngestionArtifact



# @dataclass
# class DataIngestionConfig:
#     data_ingestion_dir: str = os.path.join(
#         training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
#     )

#     feature_store_file_path: str = os.path.join(
#         data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
#     )
#     data_download_url: str = DATA_DOWNLOAD_URL
    



aa = DataIngestionConfig()
# aa = DataIngestionArtifact
print(aa)

import os
validation_status = None
print(222222222222222222222, aa.feature_store_file_path)
all_files = os.listdir(aa.feature_store_file_path)
for file in DataValidationConfig.required_file_list:
    if file in all_files:
        validation_status = True
        print(111111111)
    else:
        print(22222222222)
        validation_status = False
with open(DataValidationConfig.valid_status_file_dir, 'w') as f:
    f.write(f"Validation status: {validation_status}")
