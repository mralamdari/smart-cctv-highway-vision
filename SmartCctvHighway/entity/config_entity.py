import os
from dataclasses import dataclass
from datetime import datetime
from SmartCctvHighway.constant.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)



training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 



@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )
    data_roboflow_api_key: str = DATA_ROBOFLOW_API_KEY
    data_roboflow_version: int = DATA_ROBOFLOW_VERSION
    data_roboflow_workspace: str = DATA_ROBOFLOW_WORKSPACE
    data_roboflow_project_name: str = DATA_ROBOFLOW_PROJECT_NAME
    data_roboflow_format: str = DATA_ROBOFLOW_FORMAT
    




@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES



@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    )

    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    no_epochs = MODEL_TRAINER_NO_EPOCHS

    batch_size = MODEL_TRAINER_BATCH_SIZE



@dataclass
class ModelPusherConfig:
    BUCKET_NAME: str = BUCKET_NAME
    S3_MODEL_KEY_PATH: str = S3_MODEL_NAME