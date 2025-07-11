import os

ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = 'https://drive.google.com/file/d/1IIiyvRPKyTcAEgZ5pjSRN2mYEpCi4iB6/view?usp=sharing'

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "data.yaml"]



"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16




"""
MODEL PUSHER related constant start with MODEL_PUSHER var name
"""
BUCKET_NAME = "smart-traffic-cctv-2025"
S3_MODEL_NAME = "best.pt"



"""
MODEL INFERENCE related constant start with MODEL_INFERENCE var name
"""
MODEL_INFERENCE_DIR_NAME: str = "model_inferencer"

MODEL_INFERENCE_PRETRAINED_WEIGHT_NAME: str = "yolov8s.pt"

MODEL_INFERENCE_NO_EPOCHS: int = 1

MODEL_INFERENCE_BATCH_SIZE: int = 16
