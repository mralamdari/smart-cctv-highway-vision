# import sys
# from SmartCctvHighway.logger import logging
# from SmartCctvHighway.exception import AppException
from SmartCctvHighway.pipeline.training_pipeline import TrainPipeline


obj = TrainPipeline()
obj.run_pipeline()