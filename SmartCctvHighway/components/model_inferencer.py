import os,sys
# import yaml
import shutil
from SmartCctvHighway.utils.main_utils import read_yaml_file
from SmartCctvHighway.logger import logging
from SmartCctvHighway.exception import AppException
from SmartCctvHighway.entity.config_entity import (ModelTrainerConfig, 
                                                   DataIngestionConfig)
from SmartCctvHighway.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        model_data_config: DataIngestionConfig,
        
    ):
        self.model_trainer_config = model_trainer_config
        self.model_data_config = model_data_config
        
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:    
            os.system('yolo settings sync=False')
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"""yolo 
                        train 
                        task=detect 
                        model={self.model_trainer_config.weight_name} 
                        data={self.model_data_config.feature_store_file_path}/data.yaml 
                        epochs={self.model_trainer_config.no_epochs}
                        batch={self.model_trainer_config.batch_size}
                        imgsz=640
                        --plots
                        project={self.model_trainer_config.model_trainer_dir}""")
            shutil.copy2(os.path.join(self.model_trainer_config.model_trainer_dir, 'train','weights','best.pt'), self.model_trainer_config.model_trainer_dir)
            os.system("rm -rf data.yaml")
            shutil.rmtree(os.path.join(self.model_trainer_config.model_trainer_dir, 'train'))
            # shutil.rmtree(os.path.join(self.model_trainer_config.model_trainer_dir, 'test'))
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=f"{self.model_trainer_config.model_trainer_dir}/best.pt",
            )
            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise AppException(e, sys)


