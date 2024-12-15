import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from textSummarizer.pipeline.Stage_01_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.Stage_02_Validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

# Define the stage name
STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
    try:
        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"An error occurred during {STAGE_NAME}: {e}")
        raise

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
